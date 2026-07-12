from __future__ import annotations

from check_links import check


def test_link_checker_blocks_private_and_script_targets_without_network() -> None:
    private = check("http://127.0.0.1/latest/meta-data", timeout=0.01)
    script = check("javascript:alert(1)", timeout=0.01)
    assert private["result"] == "blocked"
    assert "non-public-ip" in private["issues"]
    assert script["result"] == "blocked"
    assert "non-http-scheme" in script["issues"]
    assert "url" not in private
    assert "url" not in script
