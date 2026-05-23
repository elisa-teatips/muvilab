---
name: social-framework
description: Procedure operative del framework gestione clienti social. Usa questa skill quando l'utente lavora su un cliente (`clients/<slug>/`), avvia una fase (presales/strategy/ped/campaigns/reports), invoca un command custom (`/new-client`, `/new-month`, `/start-phase`, `/gap-check`, `/send-mail`, `/status`, `/migrate`), o chiede di applicare le regole di playbook (touch-point mail, gap-check, MVI, silenzio-assenso, isolamento clienti).
---

# Social framework skill

Operatività del mono-repo `framework/`. Letture obbligatorie prima di agire:

- `AGENTS.md` — 10 regole isolamento clienti (mai violare)
- `FLOW.md` — flusso end-to-end e mappa nodi↔path
- `playbook.md` — touch-point mail, gap-check, MVI, frontmatter, versioning
- `glossary.md` — definizioni univoche
- `clients/<slug>/AGENTS.md` — context cliente-specifico

---

## Quando si attiva

- L'utente nomina un cliente (`muvi-neogela`, `acme-spa`, …) o uno slug
- L'utente parla di "fase", "PED", "campagna", "report", "presales", "strategia"
- L'utente invoca un command custom del framework
- L'utente chiede di creare/migrare/aggiornare cartelle dentro `clients/`
- L'utente chiede status/gap di un cliente

---

## Regole non negoziabili (riassunto)

1. **Slug esplicito** in ogni operazione. Niente default. Ambiguità → chiedi.
2. **Path assoluti** che includono `clients/<slug>/...`. Mai relativi che possano risolvere altrove.
3. **Cross-client ban**: non leggere/scrivere/citare altri clienti nello stesso turno.
4. **Multi-slug in un turno → rifiuta** e chiedi di separare.
5. **Gap-check first**: prima di produrre artefatti di fase, verifica presenza input richiesti. Se manca anche un solo elemento → mail "non garantisco il risultato" PRIMA di procedere.
6. **Cliente nuovo (MVI)**: storico vuoto = mitigazione rischio esplicita nei primi 1-3 mesi.
7. **Touch-point mail**: ogni passaggio di fase genera `mail.md` con 5 blocchi (Ricevuto / Deciso-Prodotto / Approvatori / Modalità approvazione+deadline / Gap).
8. **Silenzio-assenso = default**.
9. **Frontmatter obbligatorio** su ogni output: `client, phase, period, status (draft|in-review|approved), owner, last_updated`.

---

## Anatomia fase (memorizzare)

```
phases/<fase>/[<periodo>]/
├── inputs/
│   ├── _scratch.md
│   └── feedbacks.md          (assente in 01-presales e 05-reports)
└── outputs/
    ├── <artefatto>.md        (TODO / strategy / ped+posts / campaign / report)
    ├── mail.md
    └── TODO.md               (genera fase successiva; assente in 05-reports)
```

Convenzioni `<periodo>`:

- `01-presales` → nessun periodo (one-shot)
- `02-strategy` → `YYYY`
- `03-ped` → `YYYY-MM`
- `04-campaigns` → `YYYY-MM`
- `05-reports` → `YYYY-MM-DD` (data fine periodo)

---

## Workflow standard per fase

1. Carica context: `clients/<slug>/context/` + `clients/<slug>/AGENTS.md`
2. **Gap-check** (vedi `playbook.md §4`): se manca input → `mail.md` "mancano X,Y,Z" e STOP
3. Genera artefatto con frontmatter `status: draft`
4. Genera `mail.md` (5 blocchi) e marca artefatto `status: in-review`
5. Se feedback arriva → aggiorna `inputs/feedbacks.md`, rigenera artefatto, mantieni `in-review`
6. Su approvazione (esplicita o silenzio-assenso scaduto) → `status: approved`
7. Compila `TODO.md` per fase successiva

---

## Comandi disponibili

| Command | Scopo |
|---------|-------|
| `/new-client <slug>` | Copia `_template/` in `clients/<slug>/`, scrive `.framework-version` |
| `/new-month <slug> <fase> <periodo>` | Copia template fase (`03-ped`/`04-campaigns`/`05-reports`) in nuovo periodo |
| `/start-phase <slug> <fase> [<periodo>]` | Avvia fase: carica context, esegue gap-check, propone artefatto draft |
| `/gap-check <slug> <fase> [<periodo>]` | Verifica presenza input minimi per la fase; emette mail se gap |
| `/send-mail <slug> <fase> [<periodo>]` | Compila `mail.md` 5-blocchi e marca artefatto `in-review` |
| `/status <slug>` | Mappa stato di tutte le fasi del cliente |
| `/migrate <slug-from-path>` | Migra cartella legacy in `clients/<slug>/` secondo mappatura |

---

## Subagent disponibili

| Agent | Modello | Quando invocarlo |
|-------|---------|------------------|
| `strategist` | opus-4.7 | redazione/revisione `strategy.md` |
| `ped-creator` | sonnet-4.6 | redazione `ped.md` + `posts.md` mensile |
| `campaign-planner` | sonnet-4.6 | redazione `campaign.md` mensile |
| `mail-drafter` | sonnet-4.6 | compilazione `mail.md` 5-blocchi |
| `reporter` | opus-4.7 | redazione `report.md` mensile + trigger revisione strategia |

Ogni subagent applica le stesse regole isolamento. Dichiara sempre nello stesso messaggio quale `<slug>` sta usando.

---

## Errori da non commettere

- ❌ Produrre artefatto senza gap-check
- ❌ Inventare dati storici per un cliente nuovo (usare MVI)
- ❌ Confrontare con altri clienti ("come abbiamo fatto per X")
- ❌ Sovrascrivere automaticamente clienti esistenti quando `_template/` evolve
- ❌ Dimenticare il frontmatter
- ❌ Inviare mail senza uno dei 5 blocchi
- ❌ Path relativo che possa risolvere su un altro cliente
