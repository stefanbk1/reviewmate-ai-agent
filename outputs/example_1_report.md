# PR Review Report

**JIRA task:** AUTH-101 - Resetovanje zaboravljene lozinke
**Prioritet:** High
**Status:** In Progress
**Ocena pokrivenosti:** 9/10
**Preporuka:** needs manual review

## Kratak zaključak

GitHub Pull Request ispunjava većinu kriterijuma iz JIRA zadatka AUTH-101 za resetovanje zaboravljene lozinke. Korisnik može da unese email adresu, a sistem šalje link za resetovanje lozinke ako email postoji. Link važi 30 minuta, a nova lozinka mora imati najmanje 8 karaktera, što je takođe ispunjeno. Međutim, kriterijum koji se odnosi na mogućnost prijave korisnika sa novom lozinkom je delimično ispunjen, jer nije jasno iz PR-a da li je implementirana funkcionalnost za prijavu nakon promene lozinke. Potrebno je dodatno testiranje ili implementacija kako bi se osiguralo da korisnik može uspešno da se prijavi sa novom lozinkom.

## Analiza acceptance criteria

| # | Acceptance criterion | Status | Objašnjenje |
|---|---|---|---|
| 1 | Korisnik može da unese email adresu na formi za resetovanje lozinke. | ispunjeno | U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom. |
| 2 | Ako email postoji u sistemu, sistem šalje link za resetovanje lozinke. | ispunjeno | U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom. |
| 3 | Link za resetovanje lozinke važi 30 minuta. | ispunjeno | U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom. |
| 4 | Nova lozinka mora da ima najmanje 8 karaktera. | ispunjeno | U PR izmenama postoje elementi koji ukazuju da je kriterijum pokriven implementacijom. |
| 5 | Nakon uspešne promene lozinke korisnik može da se prijavi novom lozinkom. | delimično ispunjeno | PR sadrži deo potrebne implementacije, ali nedostaju pojedini elementi ili nisu dovoljno jasno vidljivi u diff-u. |

## Rizici

- Kriterijum je samo delimično pokriven i zahteva ručnu proveru: Nakon uspešne promene lozinke korisnik može da se prijavi novom lozinkom.

## Predlog dodatnih testova

- Dodati test koji proverava: Nakon uspešne promene lozinke korisnik može da se prijavi novom lozinkom.

## Napomena

Ovo je prototip koji koristi mockovane JIRA i GitHub podatke. U budućoj verziji, isti workflow može da se poveže sa JIRA API-jem i GitHub API-jem.
