from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

sys.dont_write_bytecode = True

from kb_lib import ROOT, atomic_write_text, load_datasets, public_http_url_issues  # noqa: E402


URL_PATTERN = re.compile(r"https?://[^\s<>\"'）)\]】]+")
TRAILING = ".,;:!?，。；：！？、"


class SafeRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001, ANN201
        issues = public_http_url_issues(newurl, resolve_dns=True)
        if issues:
            raise URLError(f"blocked redirect target: {','.join(issues)}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def url_fingerprint(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def safe_open(request: Request, timeout: float):  # noqa: ANN201
    issues = public_http_url_issues(request.full_url, resolve_dns=True)
    if issues:
        raise URLError(f"blocked URL: {','.join(issues)}")
    return build_opener(SafeRedirectHandler()).open(request, timeout=timeout)


def collect_urls() -> list[str]:
    values: set[str] = set()
    records, failures = load_datasets()
    if failures:
        raise RuntimeError("cannot check links while a dataset record is unparsable")
    for record in records:
        text = record.path.read_text(encoding="utf-8")
        values.update(match.rstrip(TRAILING) for match in URL_PATTERN.findall(text))
    return sorted(values, key=str.casefold)


def check(url: str, timeout: float) -> dict[str, object]:
    issues = public_http_url_issues(url, resolve_dns=False)
    if issues:
        return {"url_fingerprint": url_fingerprint(url), "result": "blocked", "issues": issues}
    request = Request(url, method="HEAD", headers={"User-Agent": "econ-dataknowhow-link-check/1.0"})
    try:
        with safe_open(request, timeout=timeout) as response:
            return {"url": url, "status": response.status, "final_url": response.geturl(), "result": "ok"}
    except HTTPError as exc:
        if exc.code != 405:
            return {"url": url, "status": exc.code, "result": "http-error", "error": str(exc.reason)}
        fallback = Request(
            url,
            method="GET",
            headers={"User-Agent": "econ-dataknowhow-link-check/1.0", "Range": "bytes=0-1024"},
        )
        try:
            with safe_open(fallback, timeout=timeout) as response:
                return {"url": url, "status": response.status, "final_url": response.geturl(), "result": "ok"}
        except Exception as fallback_exc:  # network diagnostics are deliberately best effort
            return {"url": url, "status": exc.code, "result": "error", "error_type": type(fallback_exc).__name__}
    except (URLError, TimeoutError, OSError) as exc:
        return {"url": url, "result": "error", "error_type": type(exc).__name__}


def main() -> int:
    parser = argparse.ArgumentParser(description="Best-effort external link freshness check; never edits canonical records.")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--max-urls", type=int, default=150)
    parser.add_argument("--output", type=Path, default=ROOT / "ledgers" / "link-check.json")
    parser.add_argument("--strict", action="store_true", help="return non-zero when any checked URL is not successful")
    args = parser.parse_args()
    urls = collect_urls()[: max(args.max_urls, 0)]
    results = [check(url, args.timeout) for url in urls]
    payload = {
        "schema_version": 1,
        "checked_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "checked_count": len(results),
        "results": results,
    }
    atomic_write_text(args.output, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    failures = sum(1 for item in results if item.get("result") != "ok")
    print(f"checked={len(results)} failures={failures} output={args.output}")
    return 1 if args.strict and failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
