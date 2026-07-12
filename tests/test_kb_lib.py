from __future__ import annotations

import json
import os
import socket

import pytest

import kb_lib
from kb_lib import load_datasets, normalize_alias, public_http_url_issues, read_frontmatter, time_summary


def test_all_dataset_records_are_loadable() -> None:
    records, failures = load_datasets()
    assert failures == []
    assert len(records) >= 20
    assert all(record.id for record in records)


def test_alias_normalization_handles_common_separators() -> None:
    assert normalize_alias("China Family Panel Studies / CFPS") == "chinafamilypanelstudiescfps"


def test_time_summary_preserves_ongoing_release_context() -> None:
    records, failures = load_datasets()
    assert not failures
    cfps = next(record for record in records if record.id == "cfps")
    assert "2022" in time_summary(cfps)
    assert "ongoing" in time_summary(cfps)


def test_frontmatter_is_a_mapping() -> None:
    record = read_frontmatter(__import__("pathlib").Path("datasets/cfps.md"))
    assert isinstance(record.data, dict)
    json.dumps(record.data, ensure_ascii=False, default=str)


def test_stale_lock_does_not_evict_a_live_local_process(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(kb_lib, "LEDGER_DIR", tmp_path)
    lock_path = tmp_path / ".live.lock"
    lock_path.write_text(
        json.dumps({"token": "other", "pid": os.getpid(), "host": socket.gethostname()}),
        encoding="utf-8",
    )
    old = os.path.getmtime(lock_path) - 7200
    os.utime(lock_path, (old, old))
    with pytest.raises(RuntimeError, match="live process"):
        with kb_lib.workspace_lock("live", stale_seconds=1):
            pass
    assert lock_path.exists()


def test_public_url_guard_rejects_script_credentials_and_private_networks() -> None:
    assert public_http_url_issues("javascript:alert(1)") == ["missing-host", "non-http-scheme"]
    assert "userinfo-not-allowed" in public_http_url_issues("https://user:pass@example.test/data")
    assert "sensitive-query-parameter" in public_http_url_issues("https://example.test/data?token=secret")
    assert "non-public-ip" in public_http_url_issues("http://127.0.0.1/data")
    assert public_http_url_issues("https://example.test/data") == []
