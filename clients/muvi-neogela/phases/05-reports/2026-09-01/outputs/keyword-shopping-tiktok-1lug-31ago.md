---
client: muvi-neogela
phase: 05-reports
period: 2026-07-01 – 2026-08-31
status: draft
owner: elisa
last_updated: 2026-09-01
---

# Neogela — Keyword/Shopping (Google Traffico|Cold) e TikTok Ads, 1 lug – 31 ago 2026

Segue [analisi-dati-meta-giu-ago-google-lifetime.md](./analisi-dati-meta-giu-ago-google-lifetime.md). Dati letti da Google Ads e TikTok Ads Manager via estensione Chrome, nessun export scaricato.

---

## 1. GOOGLE ADS — IT | Search | Traffico | Cold (1 lug – 31 ago 2026)

### ⚠️ Novità: l'ad group "Estate | Kit Viaggio" è ora in pausa

Controllando la campagna è emerso che l'ad group **"Estate | Kit Viaggio"** (creato il 22/07, il cui check era previsto per il 10/08 e segnalato come scaduto nell'ultima analisi) **risulta oggi in pausa**, non più attivo. I suoi dati coincidono esattamente tra la finestra 1 lug-31 ago e lo storico "all time" (96 clic, 972 impr, €84,51 spesi, conv. value €609,33) — segno che ha operato solo in questa finestra e poi è stato fermato. Anche l'ad group "Prodotti" risulta in pausa (23 clic totali storici, quasi irrilevante). **Solo l'ad group "Rimedi" resta attivo (Eligible)** oggi.

### Top keyword per clic — ad group Rimedi (1 lug – 31 ago 2026)

| Keyword | Clic | Impr. | CTR | CPC | Costo |
|---|---|---|---|---|---|
| terapie osteoporosi | 3.909 | 28.663 | 13,64% | €0,06 | €215,08 |
| Cure naturali per osteoporosi | 2.385 | 12.977 | 18,38% | €0,06 | €148,23 |
| osteoporosi cura | 1.924 | 13.757 | 13,99% | €0,05 | €96,36 |
| rimedi osteoporosi | 1.408 | 11.451 | 12,30% | €0,05 | €73,86 |
| bifosfonati naturali | 781 | 5.142 | 15,19% | €0,08 | €62,77 |

Stesso pattern dello storico di maggio-giugno: le keyword informative su osteoporosi restano il traffico dominante, a CPC molto basso. Nessuna sorpresa rispetto al mix già noto.

### Prodotti venduti via Shopping (1 lug – 31 ago 2026)

| Prodotto | Impr. | Clic | CTR | Costo | Conversioni | Valore conversioni |
|---|---|---|---|---|---|---|
| 1 Barattolo Collagene Neogela 400g | 54.772 | 434 | 0,79% | €230,78 | 6,99 | €654,16 |
| **Tutti gli altri 15 prodotti a catalogo** | — | 0 | — | €0,00 | 0,00 | €0,00 |

**ROAS su questo unico prodotto: 2,83x.**

**⚠️ Alert grave**: a differenza del report di maggio-giugno (5 formati diversi in vendita, €26.549 di revenue totale), **in questa finestra un solo prodotto ha generato vendite**, e oggi **tutti i 16 prodotti del catalogo — incluso quello che ha venduto — risultano "Not eligible in any campaigns"** ("No campaigns advertising this product"). La spiegazione è diretta: Google Shopping/Pmax sono le uniche campagne che possono vendere prodotti via feed, e la Pmax è **paused dal 22/07** (vedi [[project_neogela_ads_luglio_agosto2026]]). Le vendite Shopping (€654,16) sono quindi tutte concentrate nelle prime 3 settimane di luglio, prima della pausa — da fine luglio a fine agosto **il canale Shopping/Pmax ha fruttato zero**, coerentemente con la decisione (corretta, vista la policy irrisolta) di tenerlo fermo.

---

## 2. TIKTOK ADS (contenuto online 1 lug – 31 ago 2026)

**Solo 2 campagne su 10 (+14 bozze mai lanciate) hanno avuto delivery nel periodo** — tutte le altre sono rimaste in pausa/a zero spesa per l'intera finestra.

| Campagna | Stato | Spesa | Impression | Copertura | Frequenza | Clic | CTR | Conversioni | Costo/conv. | ROAS | Aggiunte al carrello |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Conversione Agosto | Ended (Review issue) | €81,74 | 47.628 | 18.736 | 2,54 | 467 | 0,98% | **0** | — | 0,000 | 0 |
| Traffico Luglio 2026 | Ended | €200,00 | 197.012 | 85.533 | 2,30 | 2.040 | 1,04% | 1.200 | €0,17 | 0,000 | 1 |
| **Totale** | | **€281,74** | **244.640** | **101.353** | **2,41** | **2.507** | **1,02%** | **1.200** | **€0,23** | **0,000** | **1** |

### Osservazioni

- **"Conversione Agosto" ha generato 467 clic e zero conversioni tracciate** — €81,74 spesi senza un solo evento di conversione registrato. Il flag "Review issue" segnala un problema (probabilmente lo stesso di policy salute/integratori già noto da giugno) che potrebbe spiegare la mancata delivery ottimale o il mancato tracciamento. Da verificare se il pixel/evento di conversione è configurato correttamente per questa campagna prima di investirci ulteriore budget.
- **"Traffico Luglio 2026"** ha generato volume alto (2.040 clic, CPC €0,10) e 1.200 "conversioni" a costo bassissimo (€0,17) — ma trattandosi di una campagna con obiettivo Traffico, questa metrica **conversioni è probabilmente un evento leggero** (es. visita pagina), non un acquisto: da non confondere con vendite reali.
- **ROAS e valore conversioni sono a 0,000 su entrambe le campagne** — confermato quanto già noto da maggio/giugno: **TikTok Shop / tracciamento e-commerce non è mai stato attivato correttamente** per Neogela (vedi nota storica: "sbloccare l'accesso al Business Center Neogela permetterebbe di attivare campagne vendita native"). Le **aggiunte al carrello sono praticamente a zero (1 totale su tutto il periodo)** — stesso segnale.
- **8 campagne su 10 restano ferme** (community interaction, copertura, traffico giugno, ecc.) — nessuna new delivery da mesi. TikTok resta un canale marginale per Neogela rispetto a Meta e Google.

---

## 3. Riepilogo azioni da questa lettura

- [ ] Verificare perché "Conversione Agosto" su TikTok non genera nessuna conversione tracciata (81€ spesi a vuoto)
- [ ] Confermare/registrare che l'ad group "Estate | Kit Viaggio" è stato messo in pausa (non risulta una decisione precedentemente comunicata) e capire se è stata una scelta esplicita o un effetto collaterale
- [ ] Se si vuole rianimare il canale Shopping, la priorità resta risolvere la policy Pmax (unico blocco strutturale) prima di aggiungere altri prodotti
- [ ] TikTok Shop: se non già fatto, sbloccare l'accesso al Business Center per abilitare tracciamento vendite reale (azione nota da mesi, mai eseguita)
