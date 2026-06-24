import re
from typing import Dict, List


KEYWORD_GROUPS = {
    "email": ["email", "mail", "send_email", "adresa"],
    "lozinka": ["password", "lozinka", "new_password", "change_password"],
    "token": ["token", "expires", "expiration", "istekao", "timedelta", "30"],
    "korpa": ["cart", "korpa", "add_item", "add_to_cart"],
    "kolicina": ["quantity", "količina", "kolicina"],
    "zalihe": ["stock", "inventory", "stanje", "dostupan", "nije na stanju"],
    "cena": ["price", "total", "ukupna", "revenue", "cena"],
    "poruka": ["message", "poruka", "success", "uspešno", "uspesno"],
    "period": ["date", "period", "from", "to", "start", "end", "vremenski"],
    "izvestaj": ["report", "izveštaj", "izvestaj", "sales_report"],
    "filter": ["filter", "filtrira", "category", "kategorija", "kategorij"],
    "rola": ["role", "rola", "rolom", "manager", "menadžer", "menadzer", "permission", "access", "pristup"],
    "csv": ["csv", "export", "izveze", "izvoz"],
    "porudzbine": ["order", "orders", "porudžbina", "porudzbina"],
    "prosek": ["average", "avg", "prosek", "prosecna", "prosečna"],
}


def normalize(text: str) -> str:
    return text.lower().replace("š", "s").replace("đ", "dj").replace("ž", "z").replace("č", "c").replace("ć", "c")


def extract_words(text: str) -> List[str]:
    return re.findall(r"[a-zA-Z0-9_]+", normalize(text))


def infer_relevant_groups(criterion: str) -> List[str]:
    normalized = normalize(criterion)
    relevant = []
    for group, keywords in KEYWORD_GROUPS.items():
        for keyword in keywords:
            if normalize(keyword) in normalized:
                relevant.append(group)
                break

    # Reč "izveštaj" je previše opšta. Ako postoje konkretniji kriterijumi
    # kao period, filter, rola ili CSV, oslanjamo se na njih.
    if "izvestaj" in relevant and len(relevant) > 1:
        relevant = [group for group in relevant if group != "izvestaj"]

    if not relevant:
        words = extract_words(criterion)
        relevant = [word for word in words if len(word) >= 6][:3]
    return relevant


def score_criterion_against_diff(criterion: str, pr_diff: str) -> Dict[str, str]:
    diff_normalized = normalize(pr_diff)
    groups = infer_relevant_groups(criterion)

    matched_groups = []
    missing_groups = []

    for group in groups:
        keywords = KEYWORD_GROUPS.get(group, [group])
        found = any(normalize(keyword) in diff_normalized for keyword in keywords)
        if found:
            matched_groups.append(group)
        else:
            missing_groups.append(group)

    if not groups:
        status = "nije moguće proveriti"
    elif len(matched_groups) == len(groups):
        status = "ispunjeno"
    elif len(matched_groups) > 0:
        status = "delimično ispunjeno"
    else:
        status = "nije ispunjeno"

    explanation = build_explanation(status, matched_groups, missing_groups)
    return {
        "criterion": criterion,
        "status": status,
        "matched_keywords": ", ".join(matched_groups) if matched_groups else "-",
        "missing_keywords": ", ".join(missing_groups) if missing_groups else "-",
        "explanation": explanation,
    }


def build_explanation(status: str, matched: List[str], missing: List[str]) -> str:
    if status == "ispunjeno":
        return "U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom."
    if status == "delimično ispunjeno":
        return "PR sadrži deo potrebne implementacije, ali nedostaju pojedini elementi ili nisu dovoljno jasno vidljivi u diff-u."
    if status == "nije ispunjeno":
        return "U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion."
    return "Na osnovu dostupnog diff-a nije moguće pouzdano proceniti ovaj kriterijum."


def calculate_recommendation(findings: List[Dict[str, str]]) -> str:
    statuses = [item["status"] for item in findings]
    if all(status == "ispunjeno" for status in statuses):
        return "approve"
    if "nije ispunjeno" in statuses:
        return "request changes"
    return "needs manual review"


def calculate_quality_score(findings: List[Dict[str, str]]) -> int:
    points = 0
    for item in findings:
        if item["status"] == "ispunjeno":
            points += 2
        elif item["status"] == "delimično ispunjeno":
            points += 1
    max_points = max(len(findings) * 2, 1)
    return round((points / max_points) * 10)


def generate_risks(findings: List[Dict[str, str]]) -> List[str]:
    risks = []
    for item in findings:
        if item["status"] == "nije ispunjeno":
            risks.append(f"Kriterijum nije pokriven: {item['criterion']}")
        elif item["status"] == "delimično ispunjeno":
            risks.append(f"Kriterijum je samo delimično pokriven i zahteva ručnu proveru: {item['criterion']}")
        elif item["status"] == "nije moguće proveriti":
            risks.append(f"Nije moguće proveriti kriterijum samo na osnovu PR diff-a: {item['criterion']}")
    if not risks:
        risks.append("Nisu pronađeni veliki rizici na osnovu dostupnih mockovanih podataka.")
    return risks
