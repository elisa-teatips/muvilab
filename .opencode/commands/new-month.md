---
description: Crea nuova istanza periodica per una fase (ped/campaigns/reports)
agent: build
---

Crea nuova istanza di fase periodica.

Argomenti attesi: `<slug> <fase> <periodo>` → ricevuti come `$ARGUMENTS`.

Fasi valide e formato periodo:
- `03-ped` → `YYYY-MM`
- `04-campaigns` → `YYYY-MM`
- `05-reports` → `YYYY-MM-DD`

Procedura:
1. Parse `$ARGUMENTS` in slug/fase/periodo. Se manca anche solo uno → STOP, chiedi.
2. Verifica esistenza `clients/<slug>/`. Se non esiste → STOP.
3. Verifica fase ∈ {`03-ped`,`04-campaigns`,`05-reports`}. Altrimenti STOP (le altre fasi non sono periodiche).
4. Valida formato periodo per la fase scelta.
5. Verifica che `clients/<slug>/phases/<fase>/<periodo>/` NON esista già.
6. Copia `_template/phases/<fase>/_template/` → `clients/<slug>/phases/<fase>/<periodo>/`.
7. Aggiorna frontmatter di tutti gli output: `client: <slug>`, `period: <periodo>`, `status: draft`, `last_updated: <oggi>`.
8. Output: path nuova cartella + suggerimento di lanciare `/gap-check <slug> <fase> <periodo>`.

Regole AGENTS.md: opera SOLO sul cliente `<slug>` indicato.
