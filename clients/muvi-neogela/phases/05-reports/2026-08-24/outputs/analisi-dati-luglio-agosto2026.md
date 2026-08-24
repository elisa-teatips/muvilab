---
client: muvi-neogela
phase: 05-reports
period: 2026-07-01 – 2026-08-24
status: draft
owner: elisa
last_updated: 2026-08-24
---

# Analisi dati Neogela — Meta Ads & Google Ads (1 luglio – 24 agosto 2026)

**Fonti:** Meta Ads Manager (account "Neogela Pubblicità", act 510094346470516) e Google Ads (account CID 119-354-005 / 504-618-6879, login elisa@muvilab.it) — dati letti direttamente da interfaccia con intervallo di date personalizzato 1 lug – 24 ago 2026, nessun export scaricato.

**Nota metodologica:** su questo intervallo hanno registrato spesa/attività solo 5 campagne Meta e 3 campagne Google (comprese quelle già in pausa nel periodo). Tutte le altre campagne presenti negli account (storiche, rimosse o mai attivate in questa finestra) hanno spesa €0 e sono escluse dalle tabelle. Google Ads non espone "Copertura"/"Frequenza" a livello di campagna Search/Performance Max nella vista standard (metrica nativa solo per Video/Display) — indicato come N/D. "Aggiunte al carrello" su Google non è isolabile senza aprire il breakdown delle singole conversion action — indicato come N/D.

---

## 1. META ADS

### 1.1 Tabella campagne (1 lug – 24 ago 2026)

| Campagna | Spesa | Impression | Copertura | Frequenza | Risultato | CTR | ROAS | Valore conversioni | Aggiunte al carrello | Costo/risultato |
|---|---|---|---|---|---|---|---|---|---|---|
| Lead Generation Agosto | €1.149,11 | 290.648 | 79.180 | 3,67 | 1.669 contatti | 4,45% | — | — | 3 | €0,69/contatto |
| [Conversione] Retargeting Agosto | €1.003,17 | 256.767 | 20.018 | **12,83** | 47 acquisti | 1,90% | 4,29x | €4.301,01 | 137 | €21,34/acquisto |
| Conversione - Promo Estiva | €996,07 | 179.034 | 48.091 | 3,72 | 42 acquisti | 1,51% | 3,89x | €3.876,04 | 210 | €23,72/acquisto |
| BAU - Cold - Visite al profilo IG | €652,93 | 464.824 | 210.810 | 2,20 | 30.592 visite profilo | 8,24% | — | — | — | €0,02/visita |
| Conversione - Giugno/Luglio | €628,11 | 166.747 | 14.413 | **11,57** | 53 acquisti | 2,20% | **8,66x** | €5.437,40 | 207 | €11,85/acquisto |
| **Totale account (periodo)** | **€4.429,39** | **1.358.020** | **326.266*** | **4,16*** | 142 acquisti + 1.669 contatti + 30.592 visite | 4,60% | — | €13.614,45 | 557 | — |

\* copertura e frequenza totali a livello di account (con deduplica tra campagne), non somma delle singole righe.

### 1.2 Osservazioni

- **Frequenza in escalation su Retargeting e Giugno/Luglio** (12,83x e 11,57x): sono le due campagne con il pubblico più piccolo (copertura 20.018 e 14.413) e la spesa concentrata sugli stessi utenti per settimane. È esattamente il rischio segnalato dopo la call del 29/06/2026 ("Retargeting: frequenza in aumento → da isolare in campagna separata"): a due mesi di distanza il problema non solo persiste ma è aumentato (allora si parlava di un trend, ora la frequenza è a due cifre). Vedi [[project_neogela_meta_ads_giugno2026]].
- **Giugno/Luglio è la campagna più efficiente del periodo** (ROAS 8,66x, CPA €11,85) — in linea con il miglior risultato mai registrato per Neogela su Meta (Advantage+ di giugno: 8,19x). Nonostante la frequenza alta, il ROAS non ne risente: segnale che il pubblico, per quanto piccolo, resta molto qualificato.
- **Retargeting Agosto ha il ROAS più basso delle 3 campagne di conversione** (4,29x vs 8,66x e 3,89x) pur avendo CTR e costo/acquisto nella media — coerente con la scoperta di giugno che il segmento "più caldo" non è sempre quello che converte meglio, e con l'azione richiesta (mai eseguita) di separare il retargeting in una campagna evergreen a 2 livelli con cap di frequenza 3-5x/settimana. Con una frequenza di 12,83x oggi, quel cap è ampiamente superato.
- **Lead Generation Agosto è la campagna con più budget** (€1.149,11, il 26% della spesa Meta totale) e genera 1.669 contatti a €0,69 ciascuno — costo per lead molto basso. Verificare con Giulia/CRM il tasso di conversione di questi lead a valle (era un blocker aperto a giugno se l'automazione email fosse pronta a valle di questa campagna, vedi [[project_neogela_leadgen_form_setup]]).
- **BAU - Cold - Visite al profilo IG** ha il CTR più alto in assoluto (8,24%) ma non genera conversioni tracciate — coerente con l'obiettivo (traffico al profilo, non acquisto) e con l'insight già noto che il CTR alto non implica intento d'acquisto.
- **Promo Estiva**: ROAS 3,89x, il più basso tra le 3 campagne di conversione dirette — plausibile impatto dello sconto (margine più basso a parità di valore ordine) più che un problema di targeting; da verificare se lo sconto luglio (10-15% su kit 400g+140g) è ancora attivo o già chiuso.

---

## 2. GOOGLE ADS

### 2.1 Tabella campagne (1 lug – 24 ago 2026)

| Campagna | Stato | Spesa | Impression | Clic/interazioni | CTR | Conversioni | Valore conversioni | ROAS | CPA |
|---|---|---|---|---|---|---|---|---|---|
| IT \| Search \| Conv \| Brand | Attiva | €1.335,79 | 10.492 | 2.648 clic | 25,24% | 226,00 | €24.528,40 | **18,37x** | €5,91 |
| IT \| Search \| Traffico \| Cold | Attiva (Limited by budget) | €629,59 | 68.192 | 9.729 clic | 14,27% | 32,67 | €3.030,73 | 4,81x | €19,27 |
| IT \| Pmax \| Conv \| Hot&Cold | **In pausa** dal 22/07 | €441,08 | 102.415 | 4.302 (clic+engagement) | 4,20% | 11,99 | €1.448,42 | 3,28x | €36,79 |
| **Totale account (periodo)** | | **€2.406,46** | **181.099** | | | **270,66** | **€29.007,56** | **12,05x** | €8,89 |

Copertura e frequenza non disponibili a livello di campagna per Search/Performance Max su Google Ads.

### 2.2 Osservazioni e confronto con lo storico

- **Brand**: CPA €5,91 nel periodo — migliora rispetto al dato di fine luglio rilevato da Elisa (€8,53) ma resta sopra lo storico pre-pressione competitiva (€4,03, dato di riferimento gennaio-giugno). Il trend di pressione competitiva sui costi Brand segnalato il 22/07 non si è invertito, ma il CPA medio dell'intero periodo (che include anche giorni migliori) resta comunque contenuto rispetto al valore che si registrava a fine luglio. Da monitorare il check mensile Auction Insights Brand impostato per il 24/08 (oggi). Vedi [[project_neogela_google_ads_luglio2026]].
- **Pmax ancora "All asset groups limited by policy"**: lo stesso alert di policy segnalato da Elisa a giugno (e ancora presente il 22/07) risulta **non risolto ancora oggi**, 24/08. La campagna resta in pausa dal 22/07 per scelta esplicita di Elisa fino a risoluzione del problema — la decisione presa (non riattivare finché non risolto) risulta quindi ancora corretta e da mantenere. Il ROAS nel periodo (3,28x, calcolato sui ~21 giorni di attività pre-pausa) conferma comunque il trend di miglioramento già notato (1,90x giugno → 2,77x fine luglio → 3,28x su questa finestra), ma il problema strutturale resta bloccante per una riattivazione.
- **Traffico | Cold**: ROAS 4,81x sull'intero periodo (che include ~21 giorni a budget vecchio €9/g pre-modifica e il resto a €15/g con il nuovo ad group "Estate | Kit Viaggio" attivo) — sostanzialmente in linea con il 5,32x pre-modifica registrato da Elisa il 22/07, nessun segnale di peggioramento dopo l'aumento di budget. **Il check dedicato del 10/08 sull'ad group Estate | Kit Viaggio risulta scaduto da 14 giorni** senza una lettura isolata della sua performance — a livello di campagna aggregata non si vede una flessione, ma per valutare l'ad group specificamente serve un'analisi a livello di ad group (fuori scope di questa analisi campagna-per-campagna).

---

## 3. LETTURA COMPLESSIVA CROSS-PIATTAFORMA

| | Meta | Google |
|---|---|---|
| Spesa totale periodo | €4.429,39 | €2.406,46 |
| Valore conversioni tracciato | €13.614,45 (solo camp. acquisto) | €29.007,56 |
| ROAS medio pesato (solo camp. acquisto) | ~5,29x | 12,05x |

Google resta la piattaforma con ROAS medio nettamente superiore, trainata dalla campagna Brand (18,37x) che da sola genera l'85% del valore Google — un pattern di concentrazione forte su un'unica campagna a intento di ricerca alto, coerente con lo storico. Su Meta il valore è più distribuito tra le 3 campagne di conversione, con Giugno/Luglio come singola migliore performance (8,66x) ma nessuna concentrazione paragonabile a Google Brand.

**Segnale prioritario**: la frequenza a due cifre su due campagne Meta di conversione (Retargeting Agosto 12,83x, Giugno/Luglio 11,57x) è il rischio più concreto per le prossime settimane — anche la campagna oggi più efficiente (Giugno/Luglio) è esposta ad ad fatigue imminente senza refresh creativo.
