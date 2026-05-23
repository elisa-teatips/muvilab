---
client: muvi-neogela
type: migration-report
date: 2026-05-23
last_updated: 2026-05-23
status: in-review
owner: framework-bot
---

# Migration report — muvi-neogela

Migrazione di `/Users/elisa/Developer/muvi_neogela/` → `clients/muvi-neogela/` eseguita 2026-05-23.

## Strategia

- Modalità: **copia** (no delete del source) per sicurezza.
- 94 file sorgente → 182 file destinazione (la cardinalità è cresciuta per via dei file di scaffold del template: README, mail.md, TODO.md, feedbacks.md, etc.).
- Tutti i 94 file sorgente sono mappati.

## Mappatura eseguita

### context/
| Source | Destination |
|--------|-------------|
| `social/input/Copia di *.pdf` (4 file) | `context/brand-assets/` |
| `social/input/Aug-04-2025_Nov-03-2025_*.csv` (3) | `context/raw-data/2025-08-to-11/` |
| `social/input/Dec-01-2025_Dec-31-2025_*.csv` (5) | `context/raw-data/2025-12/` |
| `social/input/dataset_instagram-scraper_2025-10-24*.csv` | `context/raw-data/2025-10/` |
| `social/input/dataset_instagram-scraper_2025-11-01*.csv` | `context/raw-data/2025-11/` |
| `social/input/NEOGELA_Analisi Promo WOD 2025*.csv` | `context/raw-data/2025-wod/` |
| `social/input/Untitled spreadsheet - Sheet1.csv` | `context/raw-data/_unknown/` ⚠️ |
| `adv/Neogela-Pu-licità-*.csv` + `adv/tools/Neogela-Pu-licità-Campagne-*.csv` | `context/raw-data/google-ads/` |
| `social/input/Gestione Contenuti *.csv` | `context/legacy-content-plan{,-all}.csv` |
| `social/input/Idee contenuti video.md` | `context/ideas.md` |
| `social/input/Neogela - Argomenti PED.md` | `context/topics.md` |
| `social/input/appunti-debriefing` | `context/debriefing.md` |
| `social/input/ZETA 92 - Content Plan *.md` | `context/legacy-briefs/zeta-92-content-plan.md` |
| `social/todo` | `context/legacy-briefs/competitor-2025.md` |
| `social/output/social/competitor/*.md` (3) | `context/competitor-analysis/` |
| `social/output/social/analisi-social/{analisi-social-*, analisi-contenuti-performanti-*, competitor-analysis-results}.md` (4) | `context/baseline-audit/` |
| `adv/strategia-analisi-competitor-neogela.md` | `context/baseline-audit/` |
| `.github/istruzioni/target.md` | `context/brand-guidelines/target.md` |
| `.github/istruzioni/tone-of-voice.md` | `context/brand-guidelines/tone-of-voice.md` |
| `.github/istruzioni/tone-of-voice-neogela-guide.md` | `context/brand-guidelines/tone-of-voice-guide.md` |
| `.github/istruzioni/SKILL.md` | `context/brand-guidelines/legacy-skill.md` |
| `.github/istruzioni/istruzioni` | `context/brand-guidelines/istruzioni-generali.md` |

`context/brand.md` riscritto come sintesi + indice di `brand-guidelines/`.

### phases/03-ped/
| Source | Destination |
|--------|-------------|
| `adv/ped-novembre.md` | `phases/03-ped/2025-11/outputs/ped.md` |
| `adv/piano-editoriale-equilibrato-neogela.md` | `phases/03-ped/2025-11/outputs/piano-editoriale-equilibrato.md` |
| `social/output/social/analisi-social/piano-editoriale-giugno-2026-neogela.md` | `phases/03-ped/2026-06/outputs/ped.md` |
| Caroselli + copy datati per mese (vedi sotto) | `phases/03-ped/<YYYY-MM>/outputs/posts/` |
| Posts evergreen (senza data nel nome) | `context/posts-library/{caroselli,copy}/` |

Distribuzione posts mensile:
- **2025-12**: `carosello-routine-ossa-feste-dicembre-2025`, `copy-video-auguri-natale-team-neogela`
- **2026-01**: `copy-video-auguri-capodanno-team-neogela`, `proposta-2-caroselli-gennaio-2026`
- **2026-02**: 10 file febbraio (caroselli dose-collagene, integratori-fratture; copy post/video consulenza, crolli-vertebrali, ripresa-attività, segnali-collagene)
- **2026-03**: `copy-video-artrosi-anca-marzo-2026`, `copy-video-picco-massa-ossea-25-30-anni-marzo-2026`
- **2026-04**: 3 caroselli aprile (collagene-fa-ingrassare, recensioni-trustpilot, ricette-salutari)
- **2026-06**: 2 caroselli giugno (5-errori-ossa-dopo-30, allenamento-recupero)

### phases/04-campaigns/
| Source | Destination |
|--------|-------------|
| `adv/strategia-campagne-novembre-black-friday-2025.md` | `phases/04-campaigns/2025-11/outputs/campaign.md` |
| `adv/strategia-campagna-conversione-novembre-dicembre-2025.md` | `phases/04-campaigns/2025-11/outputs/strategia-conversione-nov-dic.md` |
| `adv/copy-conversione-retargeting-senza-blackfriday.md` | `phases/04-campaigns/2025-11/outputs/copy-retargeting.md` |
| `social/output/.../script-video-black-friday-neogela-2025.md` | `phases/04-campaigns/2025-11/outputs/script-video-bf.md` |
| `adv/strategia-promo-natale-2025-neogela.md` | `phases/04-campaigns/2025-12/outputs/campaign.md` |
| `adv/analisi-campagna-conversione-natalizia-dicembre-2025.md` | `phases/04-campaigns/2025-12/outputs/results.md` |
| `adv/analisi-campagna-conversione-dicembre-2025.md` | `phases/04-campaigns/2025-12/outputs/results-conversione.md` |
| `adv/Neogela-Pu-licità-Ads-1-Dec-2025-*.csv` (2) | `phases/04-campaigns/2025-12/inputs/raw-data/` |
| `adv/promo-svalentino2026.md` | `phases/04-campaigns/2026-02/outputs/campaign.md` |
| `social/output/.../copy-adv-traffico-osteoporosi-...md` | `phases/04-campaigns/2026-02/outputs/copy-adv-traffico.md` |

### phases/05-reports/
| Source | Destination |
|--------|-------------|
| `social/output/social/analisi-campagne/analisi-campagne-ads-ottobre-2025.md` | `phases/05-reports/2025-10-31/outputs/report.md` |
| `social/input/View Report-Insights-Creatives-Table-20251201-20251231.xlsx` | `phases/05-reports/2025-12-31/inputs/raw-data/` |
| `adv/analisi-google-ads-report-feb-2026.md` | `phases/05-reports/2026-02-28/outputs/report.md` |

### tools/ (framework-wide)
- `adv/tools/analyze_google_ads_reports.py` → `tools/analyze_google_ads_reports.py`

## File ambigui o con flag — RISOLTI 2026-05-23

1. ✅ `Untitled spreadsheet - Sheet1.csv` → ispezionato: è export Meta Ads creatives dicembre 2025. Spostato in `phases/05-reports/2025-12-31/inputs/raw-data/meta-creatives-dec-2025.csv`. Cartella `_unknown/` rimossa.
2. ✅ `NEOGELA_Analisi Promo WOD 2025 - Foglio1.csv` → periodo accertato: 8-28 ottobre 2025. Spostato in `phases/05-reports/2025-10-31/inputs/raw-data/promo-wod-ott-2025.csv`. Cartella `2025-wod/` rimossa.
3. ✅ `strategia-analisi-competitor-neogela.md` → è metodologia, non audit. Spostato in `phases/02-strategy/2025/inputs/metodologia-analisi-competitor.md`.
4. ✅ `piano-editoriale-equilibrato.md` → ricostruito ruolo: è l'ossatura strategica annuale (10 nov 2025, basata su analisi 124 post). Spostato in `phases/02-strategy/2025/outputs/piano-editoriale-equilibrato.md`. La `strategy.md` 2025 ora indicizza questo file.

## TODO residui

- [x] ✅ **Frontmatter**: 35 artefatti storici arricchiti con `status: approved`, `owner: legacy-migration`, `note: migrato pre-framework`, `last_updated: 2026-05-23`.
- [x] ✅ **`02-strategy/2025/outputs/strategy.md`**: ricostruita retroattivamente come indice + ossatura strategica, puntando al piano editoriale equilibrato.
- [x] ✅ **`AGENTS.md` cliente**: compilato con anagrafica ZETA 92 SRL + doppio brand Neogela/LynUp (2026-05-23).
- [x] ✅ **`context/contracts/contract.md`**: ricostruito da `Proposta commerciale_Neogela Lynup 2.pdf` (Settembre 2025). Status `in-review` — verificare contratto firmato finale.
- [x] ✅ **`context/accesses.md`**: compilato con ID Meta Business, GA4, Google Ads, canali social Neogela. Riferimenti vault `<DA DEFINIRE>` da popolare.
- [x] ✅ **LynUp**: sospeso dal cliente (2026-05-23) — annotato in `AGENTS.md` e `brand.md`. No azione richiesta.
- [x] ✅ **Referente cliente**: Giulia Zeggio (`giulia.zeggio@zeta92.it`) — registrata in `accesses.md`.
- [x] ✅ **Vault**: Notion cliente (tutti gli accessi operativi) — propagato in `accesses.md`.
- [x] ✅ **Contratto**: confermato OK dal cliente (proposta Settembre 2025 = riferimento operativo).
- [ ] **Mesi PED senza file**: 2026-01 ha solo 2 file, 2026-03 ha 2 file, 2026-04 ha 3 file. Verosimilmente alcuni post sono in `context/posts-library/` (evergreen riusati) o in `context/legacy-content-plan.csv`. Verificare quando si pianifica il mese reale.
- [x] ✅ **Cleanup source**: utente ha autorizzato eliminazione `/Users/elisa/Developer/muvi_neogela/` (eseguita 2026-05-23).

## Cosa NON è stato migrato

- File `.DS_Store` (esclusi esplicitamente)
- `.git/` (esclusa)
- `.github/` (le sole istruzioni utili sono in `context/brand-guidelines/`)
