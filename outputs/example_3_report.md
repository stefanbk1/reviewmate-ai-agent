# PR Review Report

**JIRA task:** REPORT-330 - Izveštaj o prodaji za menadžera
**Prioritet:** High
**Status:** To Do
**Ocena pokrivenosti:** 3/10
**Preporuka:** request changes

## Kratak zaključak

GitHub Pull Request delimično ispunjava acceptance criteria iz JIRA zadatka REPORT-330. Implementirana je funkcionalnost koja prikazuje ukupan prihod i broj porudžina, što je u skladu sa zahtevima. Međutim, nedostaju ključne funkcionalnosti kao što su filtriranje izveštaja po kategoriji proizvoda, ograničenje pristupa samo za korisnike sa rolom menadžera, kao i mogućnost izvoza izveštaja u CSV format. Zbog ovih nedostataka, izveštaj nije potpuno funkcionalan i zahteva dodatne izmene pre nego što može biti prihvaćen. Preporučuje se da se fokusirate na implementaciju preostalih kriterijuma.

## Analiza acceptance criteria

| # | Acceptance criterion | Status | Objašnjenje |
|---|---|---|---|
| 1 | Menadžer može da izabere vremenski period izveštaja. | delimično ispunjeno | PR sadrži deo potrebne implementacije, ali nedostaju pojedini elementi ili nisu dovoljno jasno vidljivi u diff-u. |
| 2 | Izveštaj prikazuje ukupan prihod, broj porudžbina i prosečnu vrednost porudžbine. | ispunjeno | U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom. |
| 3 | Izveštaj može da se filtrira po kategoriji proizvoda. | nije ispunjeno | U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion. |
| 4 | Samo korisnici sa rolom menadžera mogu da pristupe izveštaju. | nije ispunjeno | U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion. |
| 5 | Izveštaj može da se izveze u CSV formatu. | nije ispunjeno | U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion. |

## Rizici

- Kriterijum je samo delimično pokriven i zahteva ručnu proveru: Menadžer može da izabere vremenski period izveštaja.
- Kriterijum nije pokriven: Izveštaj može da se filtrira po kategoriji proizvoda.
- Kriterijum nije pokriven: Samo korisnici sa rolom menadžera mogu da pristupe izveštaju.
- Kriterijum nije pokriven: Izveštaj može da se izveze u CSV formatu.

## Predlog dodatnih testova

- Dodati test koji proverava: Menadžer može da izabere vremenski period izveštaja.
- Dodati test koji proverava: Izveštaj može da se filtrira po kategoriji proizvoda.
- Dodati test koji proverava: Samo korisnici sa rolom menadžera mogu da pristupe izveštaju.
- Dodati test koji proverava: Izveštaj može da se izveze u CSV formatu.

## Napomena

Ovo je prototip koji koristi mockovane JIRA i GitHub podatke. U budućoj verziji, isti workflow može da se poveže sa JIRA API-jem i GitHub API-jem.
