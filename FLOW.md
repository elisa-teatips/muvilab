# Flusso operativo — Cliente tipo

Documento unico che visualizza il processo standardizzato definito nel meeting del 20/05/2026 e riflesso nella struttura `phases/`.

Ogni fase ha sempre la stessa anatomia:

- `inputs/` → contesto + `feedbacks.md` ricevuti
- `outputs/` → artefatto della fase + `mail.md` (touch-point formale) + `TODO.md` (genera la fase successiva)
- per le fasi ricorrenti (`03-ped`, `04-campaigns`, `05-reports`) c'è una sotto-cartella datata `MM-YYYY` / `YYYY-MM-DD`

Legenda: 🟦 fase · 📧 mail di touch-point · 🔁 loop ricorrente · ⚠️ gap-check · 📁 path nel repo

---

## 1. Diagramma end-to-end

```mermaid
flowchart TD
    %% ============ INGAGGIO ============
    CLIENT([Cliente nuovo / ingaggio])
    CLIENT --> P1

    %% ============ 01 PRESALES ============
    subgraph S1["🟦 01-presales — one-shot"]
        P1[Acquisizione contesto + TODO dal presales<br/>📁 phases/01-presales/inputs/]
        P1 --> P1OUT[TODO.md<br/>📁 phases/01-presales/outputs/TODO.md]
        P1OUT --> P1MAIL[📧 mail.md<br/>«ho capito questo contesto, procedo con questi todo»<br/>📁 phases/01-presales/outputs/mail.md]
    end

    P1MAIL --> P2

    %% ============ 02 STRATEGY ============
    subgraph S2["🟦 02-strategy — annuale (revisione 6/12 mesi)"]
        P2[Input: contesto + contratto + TODO presales + feedback<br/>📁 phases/02-strategy/inputs/]
        P2 --> P2GAP{⚠️ gap-check<br/>contesto sufficiente?}
        P2GAP -- no --> P2MISS[📧 mail «mancano questi dati, MVI rischio»]
        P2GAP -- sì --> P2OUT[strategy.md — PDF Canva annuale<br/>📁 phases/02-strategy/outputs/strategy.md]
        P2OUT --> P2TODO[TODO.md<br/>→ video / grafiche / ped / campagne<br/>📁 phases/02-strategy/outputs/TODO.md]
        P2TODO --> P2MAIL[📧 mail.md<br/>«strategia pronta, visione richiesta a A/B/C/D»<br/>silenzio = approvazione]
    end

    P2MAIL --> FORK{{Fork mensile}}

    %% ============ 03 PED ============
    subgraph S3["🟦 03-ped — 🔁 mensile  (cartella MM-YYYY)"]
        P3IN[Input: strategy + ped vecchi + results + feedback + contratto<br/>📁 phases/03-ped/MM-YYYY/inputs/]
        P3IN --> P3GAP{⚠️ gap-check<br/>ho ped vecchi, results,<br/>feedback, analytics?}
        P3GAP -- no --> P3MISS[📧 mail «non garantisco il risultato»]
        P3GAP -- sì --> P3OUT[ped.md + posts.md<br/>N post · numerosità · qualità · modalità]
        P3OUT --> P3MAIL[📧 mail.md → cliente<br/>richiesta validazione]
        P3MAIL --> P3VAL{Validazione cliente}
        P3VAL -- feedback --> P3FB[feedbacks.md → reitera] --> P3IN
        P3VAL -- ok --> P3TODO[TODO.md<br/>→ grafico / videomaker / pubblicazione]
        P3TODO --> P3RES[results.md<br/>raccolta KPI post-pubblicazione]
    end

    %% ============ 04 CAMPAIGNS ============
    subgraph S4["🟦 04-campaigns — 🔁 mensile  (cartella MM-YYYY)"]
        P4IN[Input: strategy + campagne vecchie + results + feedback + contratto + accesso analytics<br/>📁 phases/04-campaigns/MM-YYYY/inputs/]
        P4IN --> P4GAP{⚠️ gap-check<br/>analytics, results,<br/>feedback presenti?}
        P4GAP -- no --> P4MISS[📧 mail «non garantisco il risultato»]
        P4GAP -- sì --> P4OUT[campaign.md<br/>KPI · tipo conversione · modalità]
        P4OUT --> P4MAIL[📧 mail.md → cliente<br/>richiesta validazione]
        P4MAIL --> P4VAL{Validazione cliente}
        P4VAL -- feedback --> P4FB[feedbacks.md → reitera] --> P4IN
        P4VAL -- ok --> P4TODO[TODO.md<br/>→ setup campagna · creatività]
        P4TODO --> P4RES[results.md<br/>KPI campagna]
    end

    FORK --> P3IN
    FORK --> P4IN

    %% ============ 05 REPORTS ============
    subgraph S5["🟦 05-reports — 🔁 mensile (cartella YYYY-MM-DD)"]
        P5IN[Input: results ped + results campaigns<br/>📁 phases/05-reports/YYYY-MM-DD/inputs/]
        P5IN --> P5OUT[report.md<br/>sintesi KPI vs strategia]
        P5OUT --> P5MAIL[📧 mail.md → cliente + team]
    end

    P3RES --> P5IN
    P4RES --> P5IN

    %% ============ LOOP STRATEGICO ============
    P5MAIL --> REV{Scostamento<br/>vs strategia?}
    REV -- no → ciclo mensile --> FORK
    REV -- sì / 6-12 mesi --> P2

    %% styling
    classDef mail fill:#fff3cd,stroke:#b58105
    classDef gap fill:#f8d7da,stroke:#842029
    classDef out fill:#d1e7dd,stroke:#0f5132
    class P1MAIL,P2MAIL,P3MAIL,P4MAIL,P5MAIL,P2MISS,P3MISS,P4MISS mail
    class P2GAP,P3GAP,P4GAP gap
    class P1OUT,P2OUT,P3OUT,P4OUT,P5OUT out
```

---

## 2. Anatomia per fase

| # | Fase | Cadenza | Input principali | Decisioni / processo | Output (file) | Touch-point email |
|---|------|---------|------------------|----------------------|---------------|-------------------|
| 01 | `presales` | one-shot per cliente | contesto cliente, contratto, todo del commerciale | comprensione e formalizzazione todo | `TODO.md` | «contesto compreso, procedo con questi todo» |
| 02 | `strategy` | annuale (revisione 6/12 mesi) | contesto + contratto + `feedbacks.md` | strategia annuale (PDF Canva), parte testuale (Elisa) + parte creativa (Giovanni) | `strategy.md`, `TODO.md` | «strategia pronta, visione di A/B/C/D — silenzio = approvazione» |
| 03 | `ped/MM-YYYY` | mensile | `strategy` + ped vecchi + `results.md` + `feedbacks.md` + contratto | N post · numerosità · qualità · modalità | `ped.md`, `posts.md`, `results.md`, `TODO.md` | proposta al cliente + validazione, poi consegna a grafici/video |
| 04 | `campaigns/MM-YYYY` | mensile | `strategy` + campagne vecchie + analytics + `feedbacks.md` + contratto | KPI · tipo conversione · numerosità · modalità | `campaign.md`, `results.md`, `TODO.md` | proposta al cliente + validazione, poi setup operativo |
| 05 | `reports/YYYY-MM-DD` | mensile | `results.md` di ped + campaigns | sintesi KPI vs strategia | `report.md` | invio cliente + team, trigger eventuale revisione strategy |

---

## 3. Touch-point email (regola d'oro)

Da transcript 00:14:21 / 00:15:33: **ad ogni passaggio di fase parte una mail** che fissa lo stato, le decisioni prese e chi deve approvare. Vale come "freno di emergenza": se nessuno ferma, si procede.

```
presales ──📧──▶ strategy ──📧──▶ ped/campaigns ──📧──▶ cliente ──📧──▶ report ──📧──▶ (eventuale ri-strategia)
```

Ogni `mail.md` deve contenere:

1. **Cosa ho ricevuto** (riferimento ai file di `inputs/`)
2. **Cosa ho deciso / prodotto** (riferimento ai file di `outputs/`)
3. **Chi deve visionare / approvare** (nomi espliciti)
4. **Modalità di approvazione** (silenzio-assenso vs approvazione esplicita) + deadline
5. **Eventuali gap di contesto** (vedi §4)

---

## 4. Gap-check (⚠️) — meccanismo anti-output fallace

Da transcript 00:17:56 / 00:20:20: prima di produrre `ped.md` / `campaign.md` / `strategy.md`, controllare che siano disponibili:

- ✅ contesto cliente
- ✅ contratto / specifiche tecniche (numerosità asset, modalità)
- ✅ artefatti vecchi (ped vecchi, campagne vecchie)
- ✅ `results.md` storici
- ✅ `feedbacks.md` cliente
- ✅ accesso analytics

**Se anche solo uno manca → parte `mail.md` "mancano X, Y, Z; non posso garantire il risultato"** prima di procedere.

Caso cliente nuovo (storico vuoto): si formalizza la mitigazione del rischio (MVI) — primi 1-3 mesi senza garanzia di risultato, si raccolgono dati per cominciare a reiterare.

---

## 5. Loop temporali

| Loop | Frequenza | Innesco | Effetto |
|------|-----------|---------|---------|
| Validazione cliente (intra-fase) | per artefatto | `feedbacks.md` arrivati | rigenera `ped.md` / `campaign.md` |
| Operativo | mensile | inizio mese | nuova cartella `MM-YYYY` in `03-ped` e `04-campaigns`, nuovo `report` in `05-reports` |
| Strategico | 6 o 12 mesi, o su scostamento KPI | `report.md` fuori target | rigenera `strategy.md`, riparte il fork mensile |

---

## 6. Operatività "rumorosa" (fuori scope strategico)

Da transcript 00:21:35: attività operative quotidiane (video in ritardo, drag&drop, verifiche file) **non entrano nel diagramma strategico**. Vivono come:

- placeholder dentro `posts.md` (es. «video centro Giotto, giorno X»)
- TODO laterali delegabili a stagista / agenti specifici
- non bloccano il flusso principale

---

## 7. Mappa nodi diagramma ↔ filesystem

| Nodo | Path |
|------|------|
| `P1` inputs | `phases/01-presales/inputs/` |
| `P1OUT` | `phases/01-presales/outputs/TODO.md` |
| `P1MAIL` | `phases/01-presales/outputs/mail.md` |
| `P2` inputs | `phases/02-strategy/inputs/` (+ `feedbacks.md`) |
| `P2OUT` | `phases/02-strategy/outputs/strategy.md` |
| `P2TODO` | `phases/02-strategy/outputs/TODO.md` |
| `P2MAIL` | `phases/02-strategy/outputs/mail.md` |
| `P3IN` | `phases/03-ped/<MM-YYYY>/inputs/` |
| `P3OUT` | `phases/03-ped/<MM-YYYY>/outputs/ped.md` + `posts.md` |
| `P3RES` | `phases/03-ped/<MM-YYYY>/outputs/results.md` |
| `P3TODO` | `phases/03-ped/<MM-YYYY>/outputs/TODO.md` |
| `P3MAIL` | `phases/03-ped/<MM-YYYY>/outputs/mail.md` |
| `P4IN` | `phases/04-campaigns/<MM-YYYY>/inputs/` |
| `P4OUT` | `phases/04-campaigns/<MM-YYYY>/outputs/campaign.md` |
| `P4RES` | `phases/04-campaigns/<MM-YYYY>/outputs/results.md` |
| `P4TODO` | `phases/04-campaigns/<MM-YYYY>/outputs/TODO.md` |
| `P4MAIL` | `phases/04-campaigns/<MM-YYYY>/outputs/mail.md` |
| `P5IN` | `phases/05-reports/<YYYY-MM-DD>/inputs/` |
| `P5OUT` | `phases/05-reports/<YYYY-MM-DD>/outputs/report.md` |
| `P5MAIL` | `phases/05-reports/<YYYY-MM-DD>/outputs/mail.md` |
| Contesto globale | `context/` (incluso `context/contracts/contract.md`) |
