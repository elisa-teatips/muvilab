---
description: Avvia una fase per il cliente; carica context, gap-check, delega al subagent
agent: build
---

Avvia fase. Argomenti: `<slug> <fase> [<periodo>]` → `$ARGUMENTS`.

Procedura:
1. Parse. Periodo obbligatorio per `03-ped`/`04-campaigns`/`05-reports`.
2. Verifica esistenza cartella fase (crea con `/new-month` se mancante e fase periodica).
3. Esegui gap-check inline (logica come `/gap-check`). Se gap critico → STOP, scrivi `mail.md` di alert e termina.
4. Carica:
   - `clients/<slug>/AGENTS.md`
   - `clients/<slug>/context/brand.md`, `context/contracts/contract.md`
   - artefatti precedenti rilevanti per la fase
5. Delega al subagent corretto:
   - `02-strategy` → `@strategist`
   - `03-ped` → `@ped-creator`
   - `04-campaigns` → `@campaign-planner`
   - `05-reports` → `@reporter`
   - `01-presales` → procedi direttamente (no subagent dedicato)
6. Il subagent produce draft artefatto con frontmatter `status: draft`.
7. Suggerisci passaggio successivo: revisione utente → `/send-mail <slug> <fase> [<periodo>]` per touch-point e `status: in-review`.

Regole AGENTS.md: dichiara slug usato in ogni messaggio. Mai cross-client.
