---
description: Dashboard multi-cliente — mostra stato e cose da fare per tutti i clienti
agent: plan
---

Dashboard completa di tutti i clienti. Nessun argomento richiesto.

## Procedura

### 1. Enumera clienti

Leggi la directory `clients/`. Includi solo sottocartelle che contengano `phases/`.
Escludi `_template`, file nascosti, o qualunque entry non-directory.
Ordina alfabeticamente.

### 2. Per ogni cliente — raccolta dati (isolamento OBBLIGATORIO)

> **Regola AGENTS.md**: ogni cliente è lavorato in totale isolamento.
> Nessun dato, path, o osservazione di un cliente deve comparire nella sezione di un altro.

Per ogni `<slug>` trovato, esegui le seguenti letture:

**Contesto**
- `clients/<slug>/.framework-version` → versione template

**Fasi one-shot**
- `clients/<slug>/phases/01-presales/outputs/TODO.md` → frontmatter `status`, `date`
- `clients/<slug>/phases/01-presales/outputs/mail.md` → frontmatter `status`, `date`
- `clients/<slug>/phases/02-strategy/` → per ogni sotto-cartella anno:
  - `outputs/strategy.md` → `status`, `date`
  - `outputs/TODO.md` → `status`, `date`
  - `outputs/mail.md` → `status`, `date`

**Fasi ricorrenti mensili** — per ogni sotto-cartella datata `YYYY-MM` (ordina decrescente, prendi le ultime 3):
- `clients/<slug>/phases/03-ped/<YYYY-MM>/outputs/ped.md` → `status`, `date`
- `clients/<slug>/phases/03-ped/<YYYY-MM>/outputs/posts.md` → `status`, `date`
- `clients/<slug>/phases/03-ped/<YYYY-MM>/outputs/results.md` → `status`, `date`
- `clients/<slug>/phases/03-ped/<YYYY-MM>/outputs/TODO.md` → `status`, `date`
- `clients/<slug>/phases/03-ped/<YYYY-MM>/outputs/mail.md` → `status`, `date`
- (stessa struttura per `04-campaigns/<YYYY-MM>`)

**Reports** — per ogni sotto-cartella datata `YYYY-MM-DD` (ultime 3):
- `clients/<slug>/phases/05-reports/<YYYY-MM-DD>/outputs/report.md` → `status`, `date`
- `clients/<slug>/phases/05-reports/<YYYY-MM-DD>/outputs/mail.md` → `status`, `date`

### 3. Calcola alert per ogni cliente

Usa la data odierna come riferimento. Soglie:

| Tipo alert | Condizione | Simbolo |
|---|---|---|
| Draft vecchio | `status: draft` + `date` o `last_updated` > 30 giorni fa | 🔴 |
| In-review scaduto | `status: in-review` + data > 7 giorni fa (silenzio-assenso) | 🟡 |
| PED mese corrente mancante | nessuna cartella `YYYY-MM` corrente in `03-ped/` | ⚠️ |
| Campaigns mese corrente mancante | nessuna cartella `YYYY-MM` corrente in `04-campaigns/` | ⚠️ |
| Report mancante | mese precedente chiuso senza cartella in `05-reports/` | ⚠️ |
| Touch-point pending | artefatto `approved` ma `mail.md` assente o `draft` nella stessa cartella | 📧 |

Se un file non esiste, trattalo come assente (non come errore) e segnalalo come ⚠️ solo se ci si aspetterebbe che esista (es. 03-ped del mese corrente).

### 4. Output — formato per ogni cliente

Stampa una sezione per ogni cliente nel seguente formato:

```
════════════════════════════════════════════════
<SLUG>  (template: <framework-version>)
════════════════════════════════════════════════
Prossima azione: <descrizione breve della cosa più urgente da fare>

Stato fasi recenti:
| Fase         | Periodo    | Artefatto    | Status     | Data       | Note   |
|--------------|------------|--------------|------------|------------|--------|
| ...          | ...        | ...          | ...        | ...        | ...    |

Alert:
🔴 ...
🟡 ...
⚠️ ...
📧 ...
(se nessun alert: ✅ nessun alert — tutto in ordine)
```

Colonna **Note** nella tabella: aggiungi solo se rilevante (es. `⚠️ 15gg`, `MANCANTE`). Lasciala vuota altrimenti.

Nella tabella includi: tutti gli artefatti delle ultime 2 cartelle mensili per 03-ped, 04-campaigns, 05-reports + strategy attiva + presales se incompleto.

"Prossima azione" deve essere una frase concisa e azionabile, es.:
- "Creare PED 2026-06 → `/start-phase <slug> 03-ped 06-2026`"
- "Inviare mail di approvazione strategy → `/send-mail <slug> 02-strategy`"
- "Attendere feedback cliente su campaign in-review (silenzio-assenso scade il GG/MM)"
- "Tutto in ordine — ciclo mensile regolare"

### 5. Sommario finale cross-cliente

Dopo tutte le sezioni cliente, stampa:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOMMARIO  (<N> clienti)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 Draft vecchi:          <N>
🟡 Silenzio-assenso:      <N>
⚠️  Cadenze mancanti:     <N>
📧 Touch-point pending:   <N>
─────────────────────────────────────────────
TOT alert:                <N>
```

### 6. Regole di isolamento (CRITICHE)

- Il testo della sezione di `clients/A` non deve mai menzionare, citare, confrontare o fare riferimento a `clients/B`.
- Il sommario finale può riportare solo conteggi numerici aggregati, non dettagli specifici.
- Se uno slug è ambiguo o la cartella non esiste, segnala l'anomalia e continua con gli altri.
- Nessuna scrittura di file. Questo comando è **sola lettura**.
- Per agire sugli alert usa i comandi esistenti: `/gap-check`, `/start-phase`, `/new-month`, `/send-mail`, `/status`.
