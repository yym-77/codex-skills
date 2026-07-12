#!/usr/bin/env python3
"""Read-only safety scan for explicitly named Markdown growth records."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_SUFFIXES = {".md", ".markdown"}
VALID_SOURCE_CLASSES = {"public", "personal", "work-derived"}

RULES = [
    ("PRIVATE_KEY", "block", re.compile(r"-----BEGIN .*PRIVATE KEY-----")),
    ("PRIVATE_IPV4", "block", re.compile(r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b")),
    ("INTERNAL_HOST", "block", re.compile(r"(?i)https?://[^\s/]*(?:\.internal|\.corp|\.lan|\.local)(?:[/\s]|$)")),
    ("WINDOWS_USER_PATH", "block", re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\r\n]+\\")),
    ("UNIX_USER_PATH", "block", re.compile(r"(?:/home/[^/\s]+/|/Users/[^/\s]+/)")),
    ("PUBLIC_REPOSITORY", "review", re.compile(r"(?i)https?://(?:www\.)?(?:github\.com|gitlab\.com|gitee\.com)/[^\s)]+")),
]


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result: dict[str, object] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value == "true":
            result[key] = True
        elif value == "false":
            result[key] = False
        else:
            result[key] = value.strip("\"'")
    return result


def scan(path: Path, require_sync_metadata: bool) -> list[tuple[str, str, int]]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("Only explicitly named regular files are accepted")
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        raise ValueError("Only Markdown files are accepted")
    if path.stat().st_size > MAX_FILE_SIZE:
        raise ValueError("File exceeds 5 MiB")

    text = path.read_text(encoding="utf-8-sig", errors="strict")
    findings: list[tuple[str, str, int]] = []
    for rule_id, severity, pattern in RULES:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append((rule_id, severity, line))

    if require_sync_metadata:
        meta = parse_frontmatter(text)
        if meta.get("sync_allowed") is not True:
            findings.append(("SYNC_ALLOWED", "block", 1))
        if meta.get("redaction_checked") is not True:
            findings.append(("REDACTION_CHECKED", "block", 1))
        source_class = meta.get("source_class")
        if source_class not in VALID_SOURCE_CLASSES:
            findings.append(("SOURCE_CLASS", "block", 1))
        if source_class == "work-derived" and meta.get("confidentiality") != "restricted-derived":
            findings.append(("WORK_CONFIDENTIALITY", "block", 1))

    return sorted(set(findings), key=lambda item: (item[2], item[0]))


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan explicit Markdown records before persistence or synchronization")
    parser.add_argument("files", nargs="+")
    parser.add_argument("--require-sync-metadata", action="store_true")
    parser.add_argument("--fail-on-review", action="store_true")
    args = parser.parse_args()

    blocking = False
    for raw in args.files:
        findings = scan(Path(raw), args.require_sync_metadata)
        for rule_id, severity, line in findings:
            print(f"[{severity.upper()}] {raw}:{line} {rule_id}")
            blocking = blocking or severity == "block" or args.fail_on_review

    print("A clean scan does not grant permission to publish or share the material.")
    return 1 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
