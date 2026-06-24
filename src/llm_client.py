import os
from typing import Dict, List


def build_llm_prompt(jira_ticket: Dict, findings: List[Dict[str, str]], pr_diff: str) -> str:
    criteria_text = "\n".join([f"- {item['criterion']} => {item['status']}" for item in findings])
    return f"""
Ti si AI agent koji pomaže Product Owner-u, Project Manager-u i QA timu.
Tvoj zadatak je da ukratko objasniš da li GitHub Pull Request ispunjava acceptance criteria iz JIRA zadatka.

JIRA task: {jira_ticket.get('key')} - {jira_ticket.get('title')}
Opis: {jira_ticket.get('description')}

Rezultat automatske provere kriterijuma:
{criteria_text}

PR diff:
{pr_diff[:6000]}

Napiši kratak zaključak na srpskom jeziku u 4-6 rečenica. Nemoj izmišljati stvari koje se ne vide iz dostupnih podataka.
""".strip()


def demo_llm_summary(jira_ticket: Dict, findings: List[Dict[str, str]]) -> str:
    """
    Lokalni demo analizator.
    Ovo nije pravi LLM, već fallback da bi se prototip mogao pokrenuti bez API ključa.
    Ako se uključi USE_REAL_LLM=true i postavi API ključ, koristi se pravi LLM poziv.
    """
    statuses = [item["status"] for item in findings]
    missing = [item for item in findings if item["status"] == "nije ispunjeno"]
    partial = [item for item in findings if item["status"] == "delimično ispunjeno"]

    if all(status == "ispunjeno" for status in statuses):
        return (
            f"PR za JIRA zadatak {jira_ticket.get('key')} uglavnom pokriva sve definisane acceptance criteria. "
            "Na osnovu dostupnog diff-a, implementacija deluje usklađeno sa zahtevima. "
            "Preporuka je da QA dodatno proveri ponašanje kroz testove, ali nema očiglednih blokera."
        )

    if missing:
        return (
            f"PR za JIRA zadatak {jira_ticket.get('key')} ne pokriva sve acceptance criteria. "
            f"Najveći problem je kriterijum: {missing[0]['criterion']} "
            "Zbog toga PR ne bi trebalo automatski odobriti bez dorade ili dodatnog objašnjenja developera. "
            "Preporuka je request changes ili barem ručni review od strane PO/QA osobe."
        )

    if partial:
        return (
            f"PR za JIRA zadatak {jira_ticket.get('key')} delimično pokriva acceptance criteria. "
            "Postoje elementi implementacije koji odgovaraju zahtevima, ali nisu svi kriterijumi jasno dokazani kroz diff. "
            "Preporuka je ručna provera i eventualno dodavanje testova ili dopuna implementacije."
        )

    return "Na osnovu dostupnih podataka nije moguće dati pouzdan zaključak. Potreban je ručni review."


def real_llm_summary(jira_ticket: Dict, findings: List[Dict[str, str]], pr_diff: str) -> str:
    """
    Opcioni pravi LLM poziv preko LangChain OpenAI integracije.
    Koristi se samo ako je USE_REAL_LLM=true i postoji OPENAI_API_KEY.
    """
    use_real_llm = os.getenv("USE_REAL_LLM", "false").lower() == "true"
    api_key = os.getenv("OPENAI_API_KEY")

    if not use_real_llm or not api_key:
        return demo_llm_summary(jira_ticket, findings)

    try:
        from langchain_openai import ChatOpenAI

        model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        llm = ChatOpenAI(model=model_name, temperature=0)
        prompt = build_llm_prompt(jira_ticket, findings, pr_diff)
        response = llm.invoke(prompt)
        return response.content
    except Exception as error:
        return (
            "Pravi LLM poziv nije uspeo, pa je korišćen lokalni demo zaključak. "
            f"Razlog: {error}\n\n" + demo_llm_summary(jira_ticket, findings)
        )
