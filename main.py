import argparse
from pathlib import Path

from dotenv import load_dotenv

from src.agent import run_review


BASE_DIR = Path(__file__).resolve().parent


def parse_args():
    parser = argparse.ArgumentParser(description="ReviewMate AI Agent - PR vs JIRA acceptance criteria checker")
    parser.add_argument(
        "--example",
        default="example_1",
        help="Naziv primera iz data/examples foldera. Primer: example_1, example_2, example_3",
    )
    return parser.parse_args()


def main():
    load_dotenv()
    args = parse_args()

    example_dir = BASE_DIR / "data" / "examples" / args.example
    jira_path = example_dir / "jira_ticket.json"
    pr_diff_path = example_dir / "pr_diff.diff"
    output_path = BASE_DIR / "outputs" / f"{args.example}_report.md"

    result = run_review(
        jira_path=str(jira_path),
        pr_diff_path=str(pr_diff_path),
        output_path=str(output_path),
    )

    print("\n=== ReviewMate AI Agent ===\n")
    print(f"Primer: {args.example}")
    print(f"JIRA task: {result['jira_ticket'].get('key')} - {result['jira_ticket'].get('title')}")
    print(f"Ocena pokrivenosti: {result['quality_score']}/10")
    print(f"Preporuka: {result['recommendation']}")
    print(f"Izveštaj sačuvan u: {output_path}")
    print("\n--- Kratak zaključak ---")
    print(result["llm_summary"])


if __name__ == "__main__":
    main()
