from __future__ import annotations
import argparse
import json
from pathlib import Path
from . import __version__
from .audit import audit_file, discover_settings
from .evaluate import run_live
from .scenarios import get_scenarios


def _print_audit(result: dict, fmt: str) -> None:
    if fmt == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return
    print(f"\nCCAL configuration audit — {result['source']}")
    print(result.get("disclaimer", ""))
    for f in result["findings"]:
        print(f"[{f['severity']}] {f['code']} — {f['path']}")
        print(f"  {f['detail']}")
        print(f"  Recommendation: {f['recommendation']}")
    print(f"\nFindings: {result['finding_count']}\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ccal", description="Claude Code Autonomy Lab")
    parser.add_argument("--version", action="version", version=f"ccal {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)
    audit = sub.add_parser("audit-config", help="Audit Claude Code settings without modifying them")
    audit.add_argument("--path", help="Specific settings JSON file")
    audit.add_argument("--format", choices=("text", "json"), default="text")
    scenarios = sub.add_parser("scenarios", help="Export the safe offline scenario corpus")
    scenarios.add_argument("--output", default="ccal-scenarios.json")
    evaluate = sub.add_parser("evaluate", help="Run optional text-only live evaluation")
    evaluate.add_argument("--live", action="store_true", help="Explicitly permit invocation of the Claude Code CLI")
    evaluate.add_argument("--output-dir", default="ccal-results")
    evaluate.add_argument("--timeout", type=int, default=120)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "audit-config":
        paths = discover_settings(args.path)
        if not paths:
            print("No default Claude Code settings files found. Use --path to inspect a specific JSON file.")
            raise SystemExit(0)
        all_results = [audit_file(path) for path in paths]
        if args.format == "json":
            print(json.dumps(all_results, indent=2, ensure_ascii=False))
        else:
            for result in all_results:
                _print_audit(result, "text")
        if any(any(f["severity"] == "HIGH" for f in r["findings"]) for r in all_results):
            raise SystemExit(2)
    elif args.command == "scenarios":
        out = Path(args.output)
        out.write_text(json.dumps(get_scenarios(), indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Exported {len(get_scenarios())} scenarios to {out.resolve()}")
    elif args.command == "evaluate":
        if not args.live:
            parser.error("Evaluation invokes the Claude Code CLI and may consume usage. Re-run with --live after reviewing dan-cortex/skills/robustesse-agents/references/evaluation-live.md.")
        if args.timeout < 5 or args.timeout > 900:
            parser.error("--timeout must be between 5 and 900 seconds.")
        try:
            report = run_live(Path(args.output_dir), timeout=args.timeout)
        except RuntimeError as exc:
            parser.error(str(exc))
        print(f"Reports written to {Path(args.output_dir).resolve()} (JSON + Markdown)")
        if report["summary"]["FAIL"] or report["summary"]["ERROR"]:
            raise SystemExit(1)

if __name__ == "__main__":
    main()
