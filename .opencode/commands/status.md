---
description: Mappa stato di tutte le fasi del cliente
agent: plan
---

Status report per il cliente `$ARGUMENTS`.

Procedura:
1. Verifica `clients/$ARGUMENTS/` esista. Altrimenti STOP.
2. Leggi `.framework-version`.
3. Scansiona `phases/`:
   - `01-presales/outputs/` → status TODO/mail
   - `02-strategy/*/outputs/strategy.md` → ultima annata, status
   - `03-ped/*/outputs/{ped.md,results.md}` → tutti i mesi, status
   - `04-campaigns/*/outputs/{campaign.md,results.md}` → tutti i mesi, status
   - `05-reports/*/outputs/report.md` → tutti i periodi, status
4. Per ogni file leggi frontmatter (`status`, `last_updated`).
5. Output tabella ordinata cronologicamente:

```
Fase | Periodo | Artefatto | Status | Last updated
```

6. Flag in coda:
   - 🟡 artefatti `in-review` da più di N giorni (silenzio-assenso scaduto?)
   - 🔴 `draft` vecchi (>30gg)
   - ⚠️ fasi periodiche senza istanza per mese/periodo corrente

Regole AGENTS.md: solo letture su `clients/$ARGUMENTS/`. Nessun altro cliente.
