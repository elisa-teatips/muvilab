---
description: Migra una cartella cliente legacy nel formato framework
agent: build
---

Migra cartella legacy in `clients/<slug>/`. Argomenti: `<source-path> <slug>` → `$ARGUMENTS`.

Procedura:
1. Parse. Verifica `<source-path>` esiste e `clients/<slug>/` NON esiste.
2. Esegui `/new-client <slug>` per scaffold.
3. Chiedi all'utente conferma della mappatura prima di muovere file (presenta tabella source→dest basata sulla struttura legacy individuata).
4. Esegui copia/spostamento secondo mappatura confermata. Mai cancellare il source senza esplicita conferma.
5. Per file datati (PED, campagne, report) distribuisci in cartelle `phases/<fase>/<periodo>/outputs/` rispettando convenzioni.
6. Aggiungi frontmatter mancante agli `.md` migrati (`status: approved` se sono artefatti storici già spediti al cliente).
7. Output: report file migrati + lista TODO residui (file ambigui, mappatura incerta).

Regole AGENTS.md: il source path può essere esterno a `clients/` ma destination è SOLO `clients/<slug>/`. Mai toccare altri clienti.
