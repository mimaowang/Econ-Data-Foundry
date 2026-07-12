from __future__ import annotations

from check_secrets import scan, scan_text


def test_secret_scan_detects_key_without_exposing_value(tmp_path) -> None:
    value = "sk-" + "a" * 32
    path = tmp_path / "config.txt"
    path.write_text(f"API_KEY={value}\n", encoding="utf-8")
    findings, scanned = scan(tmp_path)
    assert scanned == 1
    assert len(findings) == 1
    assert findings[0]["kind"] == "api-key"
    assert value not in str(findings)


def test_secret_scan_ignores_documentation_placeholders() -> None:
    assert scan_text("API_KEY=sk-example-placeholder-xxxxxxxxxxxxxxxxxxxx") == []
