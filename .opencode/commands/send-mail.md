---
description: Compila mail.md 5-blocchi e marca artefatto in-review
agent: build
---

Compila il touch-point mail della fase. Argomenti: `<slug> <fase> [<periodo>]` → `$ARGUMENTS`.

Procedura:
1. Parse. Periodo obbligatorio per fasi periodiche.
2. Path base: `clients/<slug>/phases/<fase>/[<periodo>/]outputs/`.
3. Delega a `@mail-drafter` per produrre `mail.md` con i 5 blocchi obbligatori (playbook §3):
   1. **Ricevuto** — link relativi ai file in `inputs/`
   2. **Deciso/Prodotto** — link agli output (artefatto, TODO)
   3. **Approvatori** — nomi espliciti (chiedere all'utente se non chiari da `context/brand.md`)
   4. **Modalità approvazione** — default silenzio-assenso, deadline (chiedi se non specificata)
   5. **Gap di contesto** — esito gap-check riassunto
4. Aggiorna frontmatter dell'artefatto principale: `status: in-review`, `last_updated: <oggi>`.
5. Output: anteprima mail + path file.

Regole AGENTS.md: solo `<slug>` indicato.
