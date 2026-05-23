# Playbook operativo

Regole di metodo per ogni cliente social gestito dal framework.
Per il flusso visivo end-to-end vedi [FLOW.md](./FLOW.md).

---

## 1. Fasi e cadenze

| # | Fase | Cadenza | Trigger | Artefatto principale |
|---|------|---------|---------|----------------------|
| 01 | `presales` | one-shot per cliente | ingaggio | `TODO.md` |
| 02 | `strategy` | annuale (revisione 6/12 mesi o su scostamento KPI) | nuovo cliente / fine ciclo | `strategy.md` (PDF Canva linkato) |
| 03 | `ped` | mensile | inizio mese | `ped.md` + `posts.md` |
| 04 | `campaigns` | mensile | inizio mese | `campaign.md` |
| 05 | `reports` | mensile | fine mese | `report.md` |

---

## 2. Anatomia di una fase

Ogni fase ha sempre la stessa struttura:

```
phases/<fase>/[<YYYY-MM>|<YYYY-MM-DD>|<YYYY>]/
├── inputs/
│   ├── _scratch.md       ← appunti grezzi, brainstorm
│   └── feedbacks.md      ← feedback ricevuti durante la fase
└── outputs/
    ├── <artefatto>.md    ← strategy.md / ped.md / campaign.md / report.md
    ├── mail.md           ← touch-point formale di passaggio fase
    └── TODO.md           ← task generati per fase successiva
```

---

## 3. Touch-point email — regola d'oro

**Ad ogni passaggio di fase parte una mail** che fissa lo stato, le decisioni prese e chi deve approvare.

Ogni `mail.md` contiene 5 blocchi obbligatori:

1. **Ricevuto**: link ai file in `inputs/`
2. **Deciso/Prodotto**: link ai file in `outputs/`
3. **Approvatori**: nomi espliciti
4. **Modalità approvazione**: silenzio-assenso (default) o esplicita + deadline
5. **Gap di contesto**: eventuali dati mancanti

> **Silenzio-assenso**: se non c'è obiezione entro la deadline indicata, si procede.

---

## 4. Gap-check ⚠️ — anti-output fallace

Prima di produrre `strategy.md` / `ped.md` / `campaign.md` controllare presenza di:

- contesto cliente (`context/brand.md`)
- contratto / specifiche (numerosità, KPI, modalità)
- artefatti vecchi (PED/campaigns dei mesi precedenti)
- `results.md` storici
- `feedbacks.md` cliente
- accesso analytics (`context/accesses.md`)

**Se manca anche solo uno → parte `mail.md` "mancano X, Y, Z; non posso garantire il risultato"** PRIMA di procedere.

### Caso cliente nuovo (MVI)

Storico vuoto = mitigazione esplicita del rischio nei primi 1-3 mesi:

> "Nei primi mesi non possiamo garantire il risultato perché non disponiamo di dati storici. Raccoglieremo dati per iterare. Confermare se procedere."

---

## 5. Loop temporali

| Loop | Frequenza | Innesco | Effetto |
|------|-----------|---------|---------|
| Validazione intra-fase | per artefatto | `feedbacks.md` arrivati | rigenera artefatto |
| Operativo | mensile | inizio mese | nuova cartella in 03/04/05 |
| Strategico | 6 o 12 mesi, o KPI fuori target | `report.md` | rigenera `strategy.md` |

---

## 6. Operatività rumorosa (fuori scope strategico)

Attività quotidiane (video in ritardo, drag&drop, verifiche file) **non entrano nel flusso framework**. Vivono come:

- placeholder dentro `posts.md` (es. "video centro Giotto, giorno X")
- TODO laterali delegabili (stagista, agenti specifici)
- non bloccano il flusso principale

---

## 7. Convenzioni file

### Frontmatter obbligatorio

Ogni file di output deve aprire con:

```yaml
---
client: <slug>
phase: <01-presales|02-strategy|03-ped|04-campaigns|05-reports>
period: <YYYY | YYYY-MM | YYYY-MM-DD>
status: draft | in-review | approved
owner: <nome>
last_updated: <YYYY-MM-DD>
---
```

### Stati

- `draft` — in lavorazione
- `in-review` — inviato per approvazione (mail partita)
- `approved` — silenzio-assenso scaduto o approvazione esplicita

---

## 8. Versioning del template

Ogni `clients/<slug>/.framework-version` traccia la versione di `_template/` usata al momento dell'onboarding.

Quando `_template/` evolve, il framework bump `CHANGELOG.md`. Cliente esistente decide se migrare.

Regola: **mai sovrascrivere automaticamente** un cliente esistente con un template aggiornato.
