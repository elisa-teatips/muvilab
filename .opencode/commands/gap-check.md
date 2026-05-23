---
description: Verifica presenza input minimi per una fase; segnala gap
agent: plan
---

Esegui gap-check per la fase indicata. Argomenti: `<slug> <fase> [<periodo>]` → `$ARGUMENTS`.

Procedura:
1. Parse. Slug e fase obbligatori; periodo richiesto per `03-ped`/`04-campaigns`/`05-reports`.
2. Verifica esistenza `clients/<slug>/`. Se no → STOP.
3. Costruisci checklist per fase secondo `playbook.md §4`:
   - **02-strategy**: `context/brand.md`, `context/contracts/contract.md`, `context/competitor-analysis/`, `context/baseline-audit/`, eventuali `feedbacks.md`
   - **03-ped**: `02-strategy/<anno>/outputs/strategy.md` approvato, ped mese precedente, `results.md` mesi precedenti, `feedbacks.md` del mese, `context/accesses.md`
   - **04-campaigns**: stessa logica con campagne precedenti + analytics access
   - **05-reports**: `results.md` di ped + campaigns del periodo
4. Per ogni voce: ✅ presente / ❌ mancante (con path).
5. Se cliente ha `.framework-version` e fase è la PRIMA in assoluto (no storico) → flag MVI.
6. Output tabella + raccomandazione:
   - Tutti ✅ → "ok, procedi con `/start-phase`"
   - Qualcuno ❌ → bozza `mail.md` "mancano X,Y,Z; non posso garantire il risultato" da scrivere in `clients/<slug>/phases/<fase>/[<periodo>/]outputs/mail.md` con `status: in-review`

Regole AGENTS.md: solo `<slug>` indicato. Solo letture, eventuale scrittura `mail.md`.
