from pathlib import Path
from typing import Dict, List


def build_markdown_report(
    jira_ticket: Dict,
    findings: List[Dict[str, str]],
    risks: List[str],
    recommendation: str,
    quality_score: int,
    llm_summary: str,
) -> str:
    lines = []
    lines.append("# PR Review Report")
    lines.append("")
    lines.append(f"**JIRA task:** {jira_ticket.get('key')} - {jira_ticket.get('title')}")
    lines.append(f"**Prioritet:** {jira_ticket.get('priority')}")
    lines.append(f"**Status:** {jira_ticket.get('status')}")
    lines.append(f"**Ocena pokrivenosti:** {quality_score}/10")
    lines.append(f"**Preporuka:** {recommendation}")
    lines.append("")
    lines.append("## Kratak zaključak")
    lines.append("")
    lines.append(llm_summary)
    lines.append("")
    lines.append("## Analiza acceptance criteria")
    lines.append("")
    lines.append("| # | Acceptance criterion | Status | Objašnjenje |")
    lines.append("|---|---|---|---|")
    for index, item in enumerate(findings, start=1):
        criterion = item["criterion"].replace("|", "\\|")
        explanation = item["explanation"].replace("|", "\\|")
        lines.append(f"| {index} | {criterion} | {item['status']} | {explanation} |")
    lines.append("")
    lines.append("## Rizici")
    lines.append("")
    for risk in risks:
        lines.append(f"- {risk}")
    lines.append("")
    lines.append("## Predlog dodatnih testova")
    lines.append("")
    for item in findings:
        if item["status"] != "ispunjeno":
            lines.append(f"- Dodati test koji proverava: {item['criterion']}")
    if all(item["status"] == "ispunjeno" for item in findings):
        lines.append("- Dodati regresione testove za sve acceptance criteria pre merge-a.")
    lines.append("")
    lines.append("## Napomena")
    lines.append("")
    lines.append(
        "Ovo je prototip koji koristi mockovane JIRA i GitHub podatke. "
        "U budućoj verziji, isti workflow može da se poveže sa JIRA API-jem i GitHub API-jem."
    )
    lines.append("")
    return "\n".join(lines)


def save_report(report: str, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
