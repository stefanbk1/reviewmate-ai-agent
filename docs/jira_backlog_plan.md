# Predlog JIRA backlog-a za ReviewMate AI Agent

## Epic 1: Analiza i definisanje zahteva

### Story: Definisanje ulaza agenta
Kao product owner, želim da definišem format JIRA taska i PR diff-a kako bi agent mogao da ih analizira.

Taskovi:
- Definisati strukturu `jira_ticket.json` fajla.
- Definisati strukturu `pr_diff.diff` fajla.
- Pripremiti 3 primera ulaznih podataka.

### Story: Definisanje strukturisanog izlaza
Kao project manager, želim da agent generiše strukturisan izveštaj kako bih brzo video da li PR ispunjava acceptance criteria.

Taskovi:
- Definisati statuse: ispunjeno, delimično ispunjeno, nije ispunjeno, nije moguće proveriti.
- Definisati format Markdown izveštaja.
- Definisati preporuke: approve, request changes, needs manual review.

## Epic 2: Implementacija LangGraph workflow-a

### Story: Učitavanje mockovanih podataka
Kao korisnik agenta, želim da agent učita JIRA task i PR diff iz lokalnih fajlova.

Taskovi:
- Implementirati loader za JSON.
- Implementirati loader za diff fajl.
- Dodati proveru grešaka za nepostojeće fajlove.

### Story: Analiza acceptance criteria
Kao QA inženjer, želim da agent proveri svaki acceptance criterion pojedinačno.

Taskovi:
- Implementirati node `analyze_criteria`.
- Implementirati osnovnu analizu pokrivenosti.
- Sačuvati rezultat za svaki kriterijum.

### Story: Generisanje finalnog izveštaja
Kao project manager, želim finalni report sa rizicima i preporukom.

Taskovi:
- Implementirati računanje ocene pokrivenosti.
- Implementirati generisanje rizika.
- Implementirati Markdown report.

## Epic 3: LLM komponenta

### Story: Generisanje zaključka pomoću LLM-a
Kao product owner, želim kratak zaključak na prirodnom jeziku kako bih brzo razumeo stanje PR-a.

Taskovi:
- Dodati LLM node u workflow.
- Pripremiti prompt za LLM.
- Omogućiti fallback demo režim bez API ključa.

## Epic 4: Testiranje i dokumentacija

### Story: Testiranje na 3 primera
Kao QA inženjer, želim da testiram agenta na više primera kako bih proverio da li radi u različitim situacijama.

Taskovi:
- Testirati primer gde je PR skoro kompletan.
- Testirati primer gde PR delimično ispunjava kriterijume.
- Testirati primer gde PR ne ispunjava bitne kriterijume.

### Story: Dokumentovanje pokretanja
Kao student, želim jasno uputstvo za pokretanje projekta kako bih mogao da ga demonstriram.

Taskovi:
- Napisati README.
- Dodati komande za instalaciju.
- Dodati komande za pokretanje primera.

Validacija je napravljena na osnovu 3 mock primera:AUTH-101,CART-205,REPORT-303
