# PR Review Report

**JIRA task:** SHOP-215 - Dodavanje proizvoda u korpu
**Prioritet:** Medium
**Status:** In Review
**Ocena pokrivenosti:** 3/10
**Preporuka:** request changes

## Kratak zaključak

GitHub Pull Request za JIRA zadatak SHOP-215 delimično ispunjava postavljene acceptance kriterijume. Korisnik može da doda proizvod u korpu, ali nije implementirana mogućnost izbora količine proizvoda, niti je obezbeđeno da se ne može dodati proizvod koji nije na stanju. Takođe, ukupna cena u korpi se delimično ažurira, što ukazuje na to da deo funkcionalnosti nije potpuno razvijen. Poruka o uspešnom dodavanju proizvoda se pravilno prikazuje korisniku. U celini, Pull Request zahteva dodatne izmene kako bi se ispunili svi kriterijumi iz JIRA zadatka.

## Analiza acceptance criteria

| # | Acceptance criterion | Status | Objašnjenje |
|---|---|---|---|
| 1 | Korisnik može da doda dostupan proizvod u korpu. | nije ispunjeno | U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion. |
| 2 | Korisnik može da izabere količinu proizvoda. | nije ispunjeno | U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion. |
| 3 | Sistem ne dozvoljava dodavanje proizvoda koji nije na stanju. | nije ispunjeno | U PR izmenama nisu pronađeni elementi koji jasno pokrivaju ovaj acceptance criterion. |
| 4 | Ukupna cena u korpi se automatski ažurira. | delimično ispunjeno | PR sadrži deo potrebne implementacije, ali nedostaju pojedini elementi ili nisu dovoljno jasno vidljivi u diff-u. |
| 5 | Korisniku se prikazuje poruka nakon uspešnog dodavanja proizvoda. | ispunjeno | U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom. |

## Rizici

- Kriterijum nije pokriven: Korisnik može da doda dostupan proizvod u korpu.
- Kriterijum nije pokriven: Korisnik može da izabere količinu proizvoda.
- Kriterijum nije pokriven: Sistem ne dozvoljava dodavanje proizvoda koji nije na stanju.
- Kriterijum je samo delimično pokriven i zahteva ručnu proveru: Ukupna cena u korpi se automatski ažurira.

## Predlog dodatnih testova

- Dodati test koji proverava: Korisnik može da doda dostupan proizvod u korpu.
- Dodati test koji proverava: Korisnik može da izabere količinu proizvoda.
- Dodati test koji proverava: Sistem ne dozvoljava dodavanje proizvoda koji nije na stanju.
- Dodati test koji proverava: Ukupna cena u korpi se automatski ažurira.

## Napomena

Ovo je prototip koji koristi mockovane JIRA i GitHub podatke. U budućoj verziji, isti workflow može da se poveže sa JIRA API-jem i GitHub API-jem.
