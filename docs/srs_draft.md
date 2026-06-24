# SRS draft - ReviewMate AI Agent

## 1. Uvod

ReviewMate AI Agent je prototip AI agenta koji proverava usklađenost GitHub Pull Request-a sa acceptance criteria iz JIRA zadatka. Sistem je namenjen product owner-u, project manager-u, QA inženjeru i razvojnom timu.

## 2. Svrha sistema

Svrha sistema je da automatizuje deo procesa pregleda Pull Request-a tako što poredi implementirane izmene sa zahtevima definisanim u JIRA tasku. Agent ne zamenjuje ručni review, ali pomaže timu da ranije uoči nedostatke.

## 3. Korisnici sistema

- Product Owner: proverava da li PR ispunjava poslovne zahteve.
- Project Manager: prati kvalitet realizacije zadataka.
- QA inženjer: koristi izveštaj za planiranje testova.
- Developer: dobija povratnu informaciju o nedostajućim delovima implementacije.

## 4. Ulazni podaci

Sistem koristi sledeće ulazne podatke:

- JIRA task u JSON formatu;
- opis zadatka;
- acceptance criteria;
- prioritet i status zadatka;
- GitHub Pull Request diff u tekstualnom formatu.

## 5. Izlazni podaci

Sistem generiše Markdown izveštaj koji sadrži:

- JIRA task;
- ocenu pokrivenosti;
- preporuku;
- status svakog acceptance criterion-a;
- rizike;
- predloge dodatnih testova;
- kratak zaključak.

## 6. Funkcionalni zahtevi

FZ1: Sistem mora da učita JIRA task iz JSON fajla.

FZ2: Sistem mora da učita PR diff iz tekstualnog fajla.

FZ3: Sistem mora da analizira svaki acceptance criterion pojedinačno.

FZ4: Sistem mora da dodeli status svakom kriterijumu: ispunjeno, delimično ispunjeno, nije ispunjeno ili nije moguće proveriti.

FZ5: Sistem mora da izračuna ocenu pokrivenosti od 1 do 10.

FZ6: Sistem mora da generiše listu rizika.

FZ7: Sistem mora da predloži dodatne testove za kriterijume koji nisu potpuno pokriveni.

FZ8: Sistem mora da generiše finalni Markdown izveštaj.

FZ9: Sistem mora da koristi LangGraph workflow sa više koraka obrade.

FZ10: Sistem mora da ima LLM komponentu za generisanje zaključka.

## 7. Nefunkcionalni zahtevi

NFZ1: Sistem treba da generiše izveštaj za jedan primer za manje od 30 sekundi.

NFZ2: Izlaz mora biti strukturisan i razumljiv korisnicima bez tehničkog znanja.

NFZ3: Sistem treba da koristi isti format izveštaja pri svakom pokretanju.

NFZ4: Sistem ne treba da čuva poverljive podatke nakon obrade.

NFZ5: Sistem treba da bude moguće pokrenuti lokalno iz terminala.

NFZ6: Rezultati sistema moraju biti proverljivi kroz najmanje 3 test primera.

## 8. Ograničenja

U prvoj verziji koriste se mockovani podaci umesto direktne integracije sa JIRA API-jem i GitHub API-jem. Ova odluka je doneta kako bi se fokus stavio na workflow agenta i strukturisanu analizu.

## 9. Buduće unapređenje

U budućoj verziji mockovani fajlovi mogu se zameniti realnim API integracijama. Agent bi mogao automatski da čita JIRA issue, GitHub PR, komentariše PR i predlaže izmene statusa zadatka.
