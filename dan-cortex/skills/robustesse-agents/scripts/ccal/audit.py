"""Advisory audit for common Claude Code settings patterns."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

DEFAULT_CANDIDATES = [
    Path(".claude/settings.json"),
    Path(".claude/settings.local.json"),
    Path.home() / ".claude" / "settings.json",
]


def _flatten(obj: Any, prefix: str = "") -> list[tuple[str, Any]]:
    out: list[tuple[str, Any]] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else key
            out.extend(_flatten(value, path))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            out.extend(_flatten(value, f"{prefix}[{index}]"))
    else:
        out.append((prefix, obj))
    return out


def audit_settings(data: dict[str, Any], source: str = "<memory>") -> dict[str, Any]:
    flat = _flatten(data)
    findings = []

    def add(severity: str, code: str, path: str, detail: str, recommendation: str):
        findings.append({"severity": severity, "code": code, "path": path, "detail": detail, "recommendation": recommendation})

    for path, value in flat:
        low_path = path.lower()
        low_val = str(value).lower()
        if "permission" in low_path and low_val in {"bypasspermissions", "dontask"}:
            add("HIGH", "BROAD_PERMISSION_MODE", path,
                f"Permission mode is set to {value!r}.",
                "Confirm this is intentional and restricted to a disposable, isolated workspace; prefer scoped allow rules and sandboxing.")
        if isinstance(value, str) and value.strip() in {"Bash(*)", "Bash( *)", "*"}:
            add("HIGH", "WILDCARD_ALLOW_RULE", path,
                f"Broad wildcard rule found: {value!r}.",
                "Replace with narrow, task-specific commands and review the effective permission hierarchy.")
        if "disablebypasspermissionsmode" in low_path and value is False:
            add("MEDIUM", "BYPASS_MODE_NOT_DISABLED", path,
                "The setting does not explicitly disable bypass-permissions mode.",
                "If appropriate for your environment, consider a managed policy that disables bypass mode.")
        if "sandbox" in low_path and value is False:
            add("MEDIUM", "SANDBOX_DISABLED", path,
                "A sandbox-related setting is explicitly false.",
                "Review whether sandboxing is appropriate; use filesystem/network boundaries where supported.")
        if "allow" in low_path and isinstance(value, str) and any(token in value for token in ("Bash(rm", "Bash(sudo", "Bash(curl", "Bash(wget")):
            add("MEDIUM", "SENSITIVE_COMMAND_ALLOW", path,
                f"Potentially sensitive command pattern is allowed: {value!r}.",
                "Check the exact pattern semantics and whether this access is necessary; prefer narrowly scoped alternatives.")

    if not findings:
        findings.append({"severity": "INFO", "code": "NO_MATCHING_PATTERNS", "path": source,
                         "detail": "No patterns from this advisory rule set were detected.",
                         "recommendation": "This is not proof of a secure configuration. Verify effective settings against the current official documentation."})
    return {"source": source, "finding_count": len(findings), "findings": findings,
            "disclaimer": "Advisory static checks only; not a complete parser or security guarantee."}


def audit_file(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"source": str(path), "finding_count": 1, "findings": [{"severity": "HIGH", "code": "INVALID_JSON", "path": str(path), "detail": f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}", "recommendation": "Correct the JSON syntax and re-run the audit."}], "disclaimer": "Advisory static checks only."}
    except OSError as exc:
        return {"source": str(path), "finding_count": 1, "findings": [{"severity": "HIGH", "code": "READ_ERROR", "path": str(path), "detail": str(exc), "recommendation": "Check the path and file permissions."}], "disclaimer": "Advisory static checks only."}
    if not isinstance(data, dict):
        data = {"_root_value": data}
    return audit_settings(data, str(path))


def discover_settings(explicit: str | None = None) -> list[Path]:
    if explicit:
        return [Path(explicit).expanduser()]
    return [p for p in DEFAULT_CANDIDATES if p.is_file()]
