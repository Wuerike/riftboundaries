import argparse
import re
from pathlib import Path
from typing import Any

from semantic_contracts import CONTRACTS_DIR, load_contract_bundle


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def token_terms(bundle: dict[str, Any]) -> set[str]:
    ontology = bundle["ontology"]
    quality_policy = bundle["quality_policy"]
    leakage = quality_policy.get("domain_leakage", {})
    terms: set[str] = set()
    for key in ("entity_kinds", "resources", "stats", "zones"):
        terms.update(str(value).strip().casefold() for value in ontology.get(key, []) or [])
    terms.update(str(value).strip().casefold() for value in quality_policy.get("relational_keywords", []) or [])
    for bucket in quality_policy.get("blind_spot_buckets", []) or []:
        terms.update(str(value).strip().casefold() for value in bucket.get("tokens", []) or [])
    ignored = {str(value).casefold() for value in leakage.get("ignored_code_terms", []) or []}
    return {term for term in terms if len(term) >= 2 and term not in {"+", "-"} and term not in ignored}


def allowed_terms(bundle: dict[str, Any]) -> set[str]:
    leakage = bundle["quality_policy"].get("domain_leakage", {})
    return {
        str(value).casefold()
        for key in ("allowed_structural_terms", "allowed_legacy_until_migrated")
        for value in leakage.get(key, []) or []
    }


def parser_files(bundle: dict[str, Any]) -> list[Path]:
    files = []
    for value in bundle["quality_policy"].get("domain_leakage", {}).get("parser_files", []) or []:
        files.append(PROJECT_ROOT / value)
    return files


def find_domain_leaks(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    blocked_terms = sorted(token_terms(bundle) - allowed_terms(bundle), key=lambda item: (-len(item), item))
    if not blocked_terms:
        return []
    leaks = []
    patterns = [(term, re.compile(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", re.I)) for term in blocked_terms]
    for path in parser_files(bundle):
        if not path.exists():
            leaks.append({"path": str(path), "line": None, "term": None, "text": "parser file not found"})
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for term, pattern in patterns:
                if pattern.search(line):
                    leaks.append(
                        {
                            "path": str(path.relative_to(PROJECT_ROOT)),
                            "line": line_number,
                            "term": term,
                            "text": line.strip(),
                        }
                    )
    return leaks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate semantic JSON contracts and guard parser scripts against new domain leakage.")
    parser.add_argument("--contracts-dir", type=Path, default=CONTRACTS_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bundle = load_contract_bundle(args.contracts_dir)
    leaks = find_domain_leaks(bundle)
    if leaks:
        print("Semantic contract validation failed: domain terms leaked into parser scripts.")
        for leak in leaks[:80]:
            print(f"{leak['path']}:{leak['line']} [{leak['term']}] {leak['text']}")
        raise SystemExit(1)
    print("Semantic contracts valid; no new domain leakage found.")


if __name__ == "__main__":
    main()
