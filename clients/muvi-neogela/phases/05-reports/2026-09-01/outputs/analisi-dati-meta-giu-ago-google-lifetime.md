---
client: muvi-neogela
phase: 05-reports
period: Meta 2026-06-01 – 2026-08-31 | Google dall'inizio delle campagne attive – 2026-08-31
status: draft
owner: elisa
last_updated: 2026-09-01
---

# Analisi dati Neogela — Meta Ads (giu–ago 2026) & Google Ads (storico campagne attive)

**Fonti:** Meta Ads Manager e Google Ads, dati letti direttamente da interfaccia via estensione Chrome, nessun export scaricato.

**Perimetro richiesto da Elisa (24/08→01/09/2026):** per Meta, solo le campagne attive nella finestra **1 giugno – 31 agosto 2026**; per Google, i dati **dall'inizio delle singole campagne attualmente attive fino al 31 agosto 2026** (non un periodo fisso).

**Nota importante su Google:** le due campagne oggi attive (Brand e Traffico | Cold) sono oggetti-campagna esistenti già dal **29 gennaio 2015** secondo i dati disponibili in Google Ads — quindi "dall'inizio della campagna" qui significa oltre 11 anni di storico cumulato, non solo il 2026. I totali di questa sezione sono quindi **cumulati su tutta la vita della campagna**, utili per un ordine di grandezza complessivo ma non direttamente comparabili con le letture mensili/settimanali fatte finora. Vanno letti come "quanto ha reso la campagna da quando esiste", non come performance recente.

---

## 1. META ADS — campagne attive 1 giugno – 31 agosto 2026

| Campagna | Spesa | Impression | Copertura | Frequenza | Risultato | CTR | ROAS | Valore conversioni | Aggiunte al carrello | Costo/risultato |
|---|---|---|---|---|---|---|---|---|---|---|
| Conversione - Giugno/Luglio | €2.053,18 | 503.356 | 66.222 | 7,60 | 128 acquisti | 2,00% | 6,35x | €13.032,96 | 380 | €16,04/acquisto |
| Lead Generation Agosto | €1.561,58 | 376.821 | 93.384 | 4,04 | 2.108 contatti | 4,49% | — | — | 6 | €0,74/contatto |
| [Conversione] Retargeting Agosto | €1.513,70 | 376.112 | 24.684 | **15,24** | 76 acquisti | 1,78% | 4,83x | €7.307,63 | 211 | €19,92/acquisto |
| BAU - Cold - Visite al profilo IG | €1.104,34 | 745.140 | 282.492 | 2,64 | 48.963 visite profilo | 8,33% | — | — | — | €0,02/visita |
| Conversione - Promo Estiva | €996,07 | 179.034 | 48.091 | 3,72 | 42 acquisti | 1,51% | 3,89x | €3.876,04 | 210 | €23,72/acquisto |
| **Totale account (periodo)** | **€7.228,87** | **2.180.463** | **455.327\*** | **4,79\*** | 254 acquisti + 2.108 contatti + 48.963 visite | 4,52% | — | €24.216,63 | 807 | — |

\* copertura e frequenza a livello di account (deduplica tra campagne), non somma delle righe.

### Osservazioni (allargando la finestra a giugno)

- **La frequenza sul Retargeting Agosto è salita ulteriormente**: 15,24x su giu-ago (era 12,83x sulla finestra più stretta 1 lug-24 ago analizzata la settimana scorsa). Confermato: più si allarga la finestra includendo giugno, più la campagna mostra segni di saturazione — è la stessa audience colpita ininterrottamente da mesi. Il problema segnalato dopo la call del 29/06 non solo non è stato risolto ma continua ad aggravarsi. Vedi [[project_neogela_meta_ads_giugno2026]] e [[project_neogela_ads_luglio_agosto2026]].
- **Giugno/Luglio resta la campagna più efficiente** (ROAS 6,35x su tre mesi, contro 8,66x calcolato sulla finestra più stretta lug-ago) — la extra spesa di giugno inclusa in questa lettura abbassa leggermente il ROAS medio ma la campagna resta solidamente la migliore per volume+efficienza tra quelle di conversione.
- **Lead Generation Agosto conferma il costo per lead molto basso** (€0,74) su un campione più ampio (2.108 contatti, +26% spesa rispetto alla finestra più stretta) — il dato non è un caso isolato di poche settimane, è un pattern stabile su tre mesi.
- **Aggiunte al carrello**: 807 totali nel trimestre, concentrate su Retargeting Agosto (211) e Promo Estiva (210) più che su Giugno/Luglio (380, ma con volume di acquisti nettamente maggiore) — indica che Giugno/Luglio converte gli ATC in acquisti in modo più efficiente delle altre due.

---

## 2. GOOGLE ADS — campagne attive, storico dall'inizio (fino al 31/08/2026)

| Campagna | Costo (storico) | Impression (storico) | CTR (storico) | Conversioni (storico) | Valore conversioni (storico) | ROAS (storico) | CPA (storico) |
|---|---|---|---|---|---|---|---|
| IT \| Search \| Conv \| Brand | €20.013,07 | 218.610 | 24,50% | 4.853,30 | €351.981,65 | **17,59x** | €4,12 |
| IT \| Search \| Traffico \| Cold | €5.383,41 | 811.412 | 13,89% | 351,52 | €34.302,09 | 6,37x | €15,31 |
| **Totale** | **€25.396,48** | **1.030.022** | **16,14%** | **5.204,81** | **€386.283,74** | **15,21x** | **€4,88** |

Copertura e frequenza non disponibili a livello di campagna Search su Google Ads.

### Osservazioni

- Il **CPA storico di Brand (€4,12)** è quasi identico al valore di riferimento pre-pressione competitiva che Elisa aveva usato come baseline (€4,03, dati gen-giu 2026) — logico: la media su 11+ anni diluisce completamente il rialzo recente (€6,50 a giugno, €8,53 fine luglio). **Questo numero storico non deve essere letto come "il CPA è tornato normale"**: è solo l'effetto media-lunga. Il segnale reale resta quello di breve periodo (Auction Insights di oggi, 24/08, è il check mensile già programmato).
- **Il CPA storico di Traffico | Cold (€15,31) è più basso di quello osservato di recente** (€19,27 sulla finestra 1 lug-24 ago) — coerente con l'aumento di budget e il nuovo ad group "Estate | Kit Viaggio" ancora in fase di apprendimento: è normale che i primi giorni/settimane di un ad group nuovo costino di più della media storica della campagna.
- **Non è possibile isolare la Pmax in questa lettura** perché è **paused**, quindi esclusa dal filtro "campagne attive" richiesto da Elisa. Il suo storico completo (incluse le versioni Hot, Cold, Hot+Cold di anni precedenti) resta disponibile ma non richiesto in questo giro; il problema di policy segnalato a giugno risulta ancora irrisolto (vedi [[project_neogela_ads_luglio_agosto2026]]).

---

## 3. Che uso fare di questi due dataset

I due dataset **non sono comparabili linea per linea**: Meta copre 3 mesi, Google copre oltre 11 anni. Vanno letti come due lenti diverse:
- **Meta (giu-ago)** = fotografia recente, utile per decisioni operative immediate (frequenza, refresh creativo, riallocazione budget).
- **Google (storico)** = ordine di grandezza complessivo di quanto le due campagne search abbiano reso "da sempre" — utile per capire il peso relativo di Brand vs Traffico nella storia dell'account (Brand genera oltre 10x il valore di Traffico pur avendo un quarto delle impression), non per decisioni tattiche di breve periodo.

Per un confronto Google su base comparabile con Meta (stessa finestra 1 giu-31 ago), la lettura già fatta nella sessione precedente resta quella di riferimento: vedi [[project_neogela_ads_luglio_agosto2026]] per i dati Google nella finestra 1 lug-24 ago 2026.
