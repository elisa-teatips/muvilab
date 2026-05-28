---
client: bognolo
phase: 04-campaigns
campaign: 2026-iperammortamento
date: 2026-05-28
status: draft
owner: elisa
---

# Audit Iperammortamento — Landing & Ads + Roadmap test

Periodo dati analizzati: 11–26 maggio 2026 (16 gg attivi).
Fonti: report `clients/bognolo/phases/05-reports/2026-05-26/outputs/report.md`, CSV Google Ads, lead form Meta, landing live `https://bognolo.it/iperammortamento-2026/`.

---

## 1. Diagnosi sintetica

### Numeri grezzi
- Spesa: €465,57 (Google €245,91 + Meta €219,66)
- Lead confermati: **3** (tutti da Meta)
- Google: 272 click, **0 conversioni misurate** (tracking off)
- Landing: 480 views GA4 / 361 sessioni reali Clarity / scroll medio **28,6%** / LCP **5,4s** / CLS **1,58** / 5 click "Contattaci"

### Cosa funziona (preservare)
1. **Intercept search**: CTR 7,84% medio, "iperammortamento 2026" 8,48% — keyword head centrata
2. **Engagement on-page**: 97s tempo medio GA4 → il contenuto regge, chi resta legge
3. **Quality lead Meta**: 2/3 con budget >100k€, 1 "da ordinare" → ICP centrato
4. **Posizione competitiva**: IS 36,6% Auction Insights, leader del settore

### I 4 problemi che bloccano il risultato

**P1 — Tracking conversioni assente (Google Ads + GA4)**
Pilotiamo AI Max senza segnali di conversione → ottimizza per click, non per lead. È il vincolo strutturale che azzoppa tutto il resto.

**P2 — Mismatch ads-landing → scroll 28,6% + quick back 2,4%**
La landing è lunga 7 sezioni, il form sta in fondo. ATF c'è un H1 esplicativo lungo ma niente azione concreta né proof. Il 71% degli utenti non scende oltre il primo quarto.

**P3 — Form multi-step su pagina lenta (LCP 5,4s, CLS 1,58)**
Form a 3 step con 8+ campi, dopo scroll lungo, su pagina con Core Web Vitals critici. GA4 registra 0 key events: non solo converte poco, non lo stiamo nemmeno misurando.

**P4 — Mismatch canale Meta**
CPL €73 + conv "sotto la media" + 4s di view-time video → audience FB intercettata in fase educativa, hook video non aggancia, form Meta probabilmente troppo lungo.

---

## 2. Audit Landing — dettaglio

### Above the fold
- ❌ H1 di 28 parole = promessa di valore lunga, non titolo
- ❌ CTA "Richiedi una consulenza" → anchor verso form in fondo (no form ATF)
- ❌ Nessun proof ATF (no "200 perizie", no loghi clienti, no badge MIMIT visibile)
- ⚠️ 3 bullet ok ma MIMIT al secondo posto invece che hero
- ✅ Micro-promessa "Risposta entro 3 giorni lavorativi"

### Body
- ✅ Sezioni Step 1-6 e "Cosa verifichiamo" solide ma sotto la fold
- ✅ FAQ allineate alle query "uncategorized" Google
- ❌ Case study Euronda/Tomasetto/Tintess sepolti in fondo
- ❌ Zero numeri concreti (X perizie, Y€ benefit medio, Z% approvazione)
- ❌ Nessuna sezione "simulazione" nonostante query "simulazione iperammortamento 2026" (104 imp)

### Form
- ❌ Multi-step 8+ campi su audience B2B in valutazione fornitore
- ❌ Form raggiungibile solo via scroll lungo o anchor click
- ⚠️ Dropdown Provincia con 110 voci (friction inutile)
- ❌ Nessuna alternativa: no phone sticky, no WhatsApp, no calendar booking

### Tecnico
- ❌ LCP 5,4s (soglia poor >4s) → penalizza Quality Score Google Ads
- ❌ CLS 1,58 (~16× soglia) → quasi certamente blocco form/immagine in lazy load, causa dei 33 dead click
- ✅ INP 170ms OK

---

## 3. Audit Ads — dettaglio

### Google Search (AI Max)
- ❌ **Tracking conversioni OFF** = blocker assoluto
- ⚠️ Broad Match + AI Max con 1.412 imp "uncategorized" (40%): mancano negative keyword
- ⚠️ Una sola ad group mescola intent (head + perizia + agevolazioni macchinari) → impossibile A/B testare copy per intent
- ❌ Asset extension generici (structured snippet "Consulenze CE, Prototipazione, Perizie" non allineato a campagna)
- ✅ Geo Nord-Est corretto, IS dominante

### Meta Lead Gen
- ❌ 1 sola creatività video reale in test (la "grafica" è marginale, €0,57 spesi)
- ❌ Video view-time medio 4s su 14.928 viz → hook non aggancia
- ❌ 1 sola audience (cap province), no lookalike, no interest-based
- ❌ Form Meta classificato conv "sotto la media" → probabilmente troppi campi
- ⚠️ Frequency 1,81 in 13 gg ok ma audience ristretta → saturazione prossima

---

## 4. Roadmap test

Ordine per impatto × tempo × dipendenze. **Fase 0 sblocca tutto il resto.**

### FASE 0 — Sbloccare misurazione (settimana 1, non negoziabile)

| # | Azione | Owner | Effort |
|---|---|---|---|
| 0.1 | Conversion tracking Google Ads: form_submit + click telefono + click email | Dev sito | 2-3h |
| 0.2 | Key events GA4: form_submit, contact_click, scroll_50%, scroll_90% | Dev sito | 1-2h |
| 0.3 | Switch Google Ads da Maximize Clicks → Maximize Conversions (dopo 15-20 conv raccolte) | Elisa | quando attivo |

### FASE 1 — Quick wins landing (settimana 1-2, no rebuild)

| # | Test | Ipotesi | KPI |
|---|---|---|---|
| 1.1 | Sticky CTA bar in alto: telefono cliccabile + "Consulenza gratuita in 3 giorni" | +30-50% click-to-form | contact_click |
| 1.2 | Form versione corta ATF (4 campi: nome, azienda, telefono, tipo investimento) | +100-300% submit rate | form_submit |
| 1.3 | Hero rewrite: H1 secco "Iperammortamento 2026: la tua perizia asseverata, senza rischi di contestazione" + 3 trust-badge ATF (MIMIT / INNOVENETO / loghi clienti) | +10-20% scroll, -quick back | scroll_50 |
| 1.4 | Fix tecnico: lazy loading immagini, dimensioni fisse container form, defer script non critici | LCP <2,5s, CLS <0,1 | core web vitals |

### FASE 2 — Test ads Google (settimana 2-4)

| # | Test | Note |
|---|---|---|
| 2.1 | Split ad group per intent: (a) head "iperammortamento 2026" (b) "perizia asseverata" (c) "agevolazioni macchinari" — copy dedicato | abilita A/B copy per intent |
| 2.2 | Negative keywords da search terms uncategorized (es. "cos'è", "wikipedia", "esempio", "fac simile") | -10-20% spreco |
| 2.3 | RSA con 2 angle: "rischio" (no contestazioni) vs "semplicità" (1 referente fino al GSE) | A/B Headlines |
| 2.4 | Asset extension overhaul (callout, sitelink, structured snippet già scritti in `note-asset-landing.md`) | deliverable già pronto |
| 2.5 | Bid +20-30% su Belluno (CTR 11,4% / CPC €0,62) | piccolo test geo |

### FASE 3 — Test ads Meta (settimana 3-5)

| # | Test | Note |
|---|---|---|
| 3.1 | 3 nuove creatività con hook diversi: (a) case Euronda con numeri (b) carosello "I 6 errori che bloccano la perizia" (c) statica "Hai già comprato? 80% delle pratiche è ancora salvabile" | target view-time >8s |
| 3.2 | Form Meta accorciato: nome + telefono + tipo investimento + budget | -CPL 30-50% atteso |
| 3.3 | Audience split: (a) attuale cap province (b) Lookalike 1% lista clienti (c) Interest "Industria 4.0 + Responsabile produzione/acquisti" | identificare audience più efficiente |
| 3.4 | Campagna Traffic→Landing in parallelo + retargeting pixel di chi visita /iperammortamento-2026/ e non converte | espandere coverage |
| 3.5 | LinkedIn pilot €300/mese su CFO/Responsabile Amministrativo/Direttore Operations Nord-Est manifatturiero | ICP perfetto per LinkedIn |

### FASE 4 — Landing v2 (settimana 4-6)

Sulla base dei risultati Fase 1, ricostruire:
- Sezione "Calcola il tuo beneficio" (simulazione semplice da budget)
- Case study con numeri reali (Euronda: X linee, Y€ agevolato)
- Sezione "Hai già comprato? Cosa puoi ancora fare" (intercept query "bene già installato")
- 2 varianti landing per ad-group Google (perizia vs agevolazioni): message match perfetto

---

## 5. KPI target 60 giorni

| KPI | Baseline maggio | Target luglio |
|---|---|---|
| Lead totali / mese | 3 | 15-20 |
| CPL medio | €155 (parziale) | <€80 |
| Form submit rate landing | <1% (stima) | 3-5% |
| Scroll depth medio | 28,6% | >50% |
| LCP landing | 5,4s | <2,5s |
| Google conv tracking | OFF | ON + 20+ conv/mese |
| Meta video hook hold (>3s) | ~40% | >60% |

---

## 6. Next action

**Prossimo turno**: Fase 0 — brief tecnico al dev sito per implementare conversion tracking (Google Ads + GA4 key events + fix Core Web Vitals LCP/CLS).
