# ReviewMate AI Agent

ReviewMate AI Agent je prototip AI agenta koji proverava da li GitHub Pull Request odgovara acceptance criteria iz JIRA zadatka.

Prototip koristi mockovane podatke, odnosno lokalne fajlove koji simuliraju JIRA task i GitHub PR diff. Cilj je da se pokaže workflow agenta bez komplikovanja oko autentifikacije, API tokena i podešavanja realnih JIRA/GitHub naloga.

## Tema projekta

**AI agent za proveru usklađenosti Pull Request-a sa JIRA acceptance criteria**

Agent prima:

- JIRA task u JSON formatu;
- acceptance criteria;
- mockovani GitHub Pull Request diff.

Agent vraća:

- ocenu pokrivenosti acceptance criteria;
- status za svaki kriterijum;
- rizike;
- predlog dodatnih testova;
- preporuku: `approve`, `request changes` ili `needs manual review`.

## Zašto agent nije običan chatbot?

Agent nije običan chatbot zato što ima unapred definisan proces rada:

1. učitava JIRA task;
2. učitava PR diff;
3. poredi acceptance criteria sa izmenama u kodu;
4. generiše rizike i preporuku;
5. pravi strukturisan Markdown izveštaj.

Workflow je implementiran pomoću LangGraph biblioteke kroz više node-ova.

## Struktura projekta

```text
reviewmate-ai-agent/
├── data/
│   └── examples/
│       ├── example_1/
│       │   ├── jira_ticket.json
│       │   └── pr_diff.diff
│       ├── example_2/
│       │   ├── jira_ticket.json
│       │   └── pr_diff.diff
│       └── example_3/
│           ├── jira_ticket.json
│           └── pr_diff.diff
├── outputs/
├── src/
│   ├── agent.py
│   ├── heuristics.py
│   ├── llm_client.py
│   ├── loaders.py
│   └── report.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Instalacija

U terminalu pokrenuti:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Zatim instalirati biblioteke:

```bash
pip install -r requirements.txt
```

## Pokretanje

Pokretanje prvog primera:

```bash
python main.py --example example_1
```

Pokretanje drugog primera:

```bash
python main.py --example example_2
```

Pokretanje trećeg primera:

```bash
python main.py --example example_3
```

Generisani izveštaji se čuvaju u folderu `outputs`.

## LLM komponenta

Projekat ima dva režima rada:

1. **Demo režim** – koristi lokalni demo analizator kako bi projekat mogao da se pokrene bez API ključa.
2. **Real LLM režim** – koristi pravi LLM preko LangChain integracije ako se podesi API ključ.

Za uključivanje realnog LLM režima potrebno je napraviti `.env` fajl na osnovu `.env.example` i podesiti:

```env
USE_REAL_LLM=true
OPENAI_API_KEY=ovde_unesi_svoj_api_kljuc
OPENAI_MODEL=gpt-4o-mini
```

Za potrebe seminarskog rada, bitno je objasniti da je LLM komponenta deo workflow-a koji generiše zaključak, dok ostali koraci agenta kontrolišu obradu i format izlaza.

## Workflow

LangGraph workflow se sastoji od sledećih node-ova:

1. `load_inputs` – učitava JIRA task i PR diff;
2. `analyze_criteria` – proverava svaki acceptance criterion;
3. `evaluate_result` – računa ocenu, rizike i preporuku;
4. `llm_summary` – generiše kratak zaključak;
5. `build_report` – pravi finalni Markdown izveštaj.

## Test primeri

### Example 1: Resetovanje lozinke

PR uglavnom pokriva acceptance criteria. Očekivana preporuka je `approve` ili blizu toga.

### Example 2: Dodavanje proizvoda u korpu

PR delimično pokriva acceptance criteria. Nedostaju količina, provera stanja zaliha i ažuriranje ukupne cene. Očekivana preporuka je `request changes`.

### Example 3: Izveštaj o prodaji

PR pokriva samo osnovne podatke izveštaja. Nedostaju vremenski period, filter, prava pristupa i CSV export. Očekivana preporuka je `request changes`.

## Ograničenja

- Prototip koristi mockovane podatke.
- Analiza diff-a je pojednostavljena.
- Rezultat mora da pregleda čovek pre stvarne upotrebe.
- Agent ne može potpuno da razume poslovni kontekst bez dodatnih podataka.
- U realnom sistemu potrebno je povezivanje sa JIRA API-jem i GitHub API-jem.

## Mogućnosti unapređenja

- povezivanje sa JIRA API-jem;
- povezivanje sa GitHub API-jem;
- automatsko komentarisanje PR-a;
- automatsko kreiranje QA checklist-e;
- bolja analiza koda;
- dodavanje web interfejsa;
- čuvanje istorije analiza.
