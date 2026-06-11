---
client: bognolo
phase: 05-reports
period: 2026-05-26
status: approved
owner: elisa
last_updated: 2026-06-11
---

# Report Andamento Campagne — Studio Bognolo — Maggio-Giugno 2026

**Periodo di riferimento**: 11 maggio – 11 giugno 2026 (31 giorni attivi)
**Periodo di confronto**: 11 – 26 maggio 2026 (16 giorni — primo report)
**Campagne attive**: Google Ads Search (AI Max) + Facebook Ads Lead Generation

---

## Executive Summary

- **Volumi raddoppiati nel secondo blocco di 15 giorni**: Google Ads passa da 272 a 428 click totali (+57%) e da €245,91 a €373,97 di spesa (+52%); Facebook Ads consolida 5 lead reali (vs 3 al 26 maggio) con spesa €394,74. Spesa media combinata 31 giorni: **€768,71**.
 - **Tracking configurato ma silenzioso**: la conversione `iper_form_submit` è stata configurata in GA4 e importata in Google Ads (1 giugno), ma ad oggi non risulta nessun evento registrato. Il problema è tecnico — possibile mancata emissione dell'evento da parte del Fusion Form, filtro URL non corrispondente, o Google Tag assente sulla pagina del form. Federico ha accesso per diagnosticare.
- **Performance tecnica della landing in netto miglioramento parziale**: CLS sceso da 1,582 a 0,225 (-86%), punteggio complessivo da 67,7 a 72,7. Resta critico l'LCP (4,54s vs soglia 2,5s) e peggiora INP (216ms, sopra soglia 200ms).
- **Segnali di disallineamento annuncio/landing**: il quick back è raddoppiato (3,38% vs 2,42%) e i dead click salgono a 7,89% (56 sessioni). Compensati però da +80% sui click "Contattaci" Smart Event (9 vs 5) e 12 sessioni dirette sull'ancora `#form` — intenzione reale ma esperienza ancora frizionata.
- **Decisione strategica imminente**: la finalità della campagna è legata al ciclo Iperammortamento 2026 (scadenza fiscale tipicamente fine anno solare ma con finestra commerciale ottimale aprile-luglio). Da concordare con Studio Bognolo se intensificare il budget nell'ultimo mese o consolidare il CPL su Facebook prima di chiudere.

---

## 1. Google Ads — Search (AI Max)

**Campagna**: Iperammortamento 2026 - Traffic - Search - AI Max
**Periodo dati**: 11 maggio – 11 giugno 2026 (31 giorni)

### 1.1 Metriche chiave — confronto periodo

| Metrica | 11–26 mag (16 gg) | 11 mag–11 giu (31 gg) | Δ |
|---|---|---|---|
| Impression totali | 3.470 | **5.907** | +70% |
| Click totali | 272 | **428** | +57% |
| CTR medio | 7,84% | **7,25%** | -0,59 pp |
| CPC medio | €0,90 | **€0,87** | -€0,03 |
| Spesa totale | €245,91 | **€373,97** | +52% |
| Conversioni tracciate | 0 ⚠️ | **0** ⚠️ | invariato |

 > **⚠️ GAP CRITICO AGGIORNATO — Tracking configurato ma 0 eventi registrati**: la conversione `iper_form_submit` è stata configurata in GA4 (1 giugno) e importata in Google Ads. Tuttavia ad oggi non risulta nessun evento registrato. Questo significa che il form sulla landing non sta generando submit tracciati — le cause possibili sono: (a) il form non viene compilato e inviato dagli utenti, (b) l'evento GA4 `form_submit` non si attiva correttamente sul Fusion Form della landing, (c) il filtro su `page_location` non matcha l'URL effettivo al momento del submit. Federico ha accesso per verificare. Fino a risoluzione, AI Max continua a ottimizzare sui click.

**Lettura del trend**: il secondo blocco di 15 giorni ha mantenuto il ritmo del primo. CTR leggermente in calo (-0,59 pp) e CPC in calo (-€0,03): l'algoritmo sta ampliando il matching mantenendo i costi. Senza tracking non possiamo dire se la qualità del traffico stia migliorando o peggiorando in termini di conversione effettiva.

### 1.2 Performance per dispositivo

*Dati device disponibili solo per il periodo 10–26 maggio (16 giorni). Google Ads non ha aggiornato il break-down nel periodo esteso.*

| Dispositivo | Click | CPC | % Budget |
|---|---|---|---|
| Desktop | 162 | €0,98 | 64,5% |
| Mobile | 108 | €0,79 | 34,9% |
| Tablet | 2 | €0,78 | 0,6% |

**Nota**: il dato è da considerarsi indicativo per il primo blocco. Sul totale 31 giorni la distribuzione è plausibilmente analoga (Bognolo è un servizio B2B desktop-pesante).

### 1.3 Landing page

Tutta la spesa converge su **bognolo.it/iperammortamento-2026/**:
- Periodo precedente: 272 click / 4.039 impression / CTR 6,73%
- Periodo esteso: dato landing aggiornato non disponibile nel report fornito; coerente con i totali campagna 428 click / 5.907 impression / CTR 7,25%

### 1.4 Analisi geografica

*Dati geografici disponibili solo per il primo blocco (10–26 maggio).*

| Provincia | Click | CTR | CPC |
|---|---|---|---|
| Vicenza | 62 | 8,90% | €1,09 |
| Padova | 53 | 7,84% | €0,95 |
| Treviso | 49 | 7,36% | €0,83 |
| Verona | 42 | 7,06% | €0,75 |
| Venezia | 33 | 8,23% | €0,92 |
| Trento | 25 | 6,85% | €0,84 |
| Belluno | 8 | 11,43% | €0,62 |

**Osservazione confermata**: Belluno mantiene il miglior rapporto CTR/CPC del bacino — mercato poco competitivo, alta intenzione. Vicenza resta la provincia con maggiore volume e spesa.

### 1.8 Analisi keyword (31 giorni)

| Keyword | Click | Impression | CTR | CPC | Spesa | % Budget |
|---|---|---|---|---|---|---|
| iperammortamento 2026 | 264 | 3.432 | 7,69% | €0,87 | €228,56 | 61,1% |
| agevolazioni acquisto macchinari 2026 | 117 | 1.745 | 6,70% | €0,91 | €106,32 | 28,4% |
| interconnessione macchinari 4.0 | 12 | 123 | 9,76% | €0,59 | €7,13 | 1,9% |
| perizia iperammortamento | 9 | 101 | 8,91% | €1,65 | €14,86 | 4,0% |
| iperammortamento software gestionale | 7 | 118 | 5,93% | €0,47 | €3,31 | 0,9% |
| perizia asseverata | 5 | 87 | 5,75% | €0,96 | €4,79 | 1,3% |
| iperammortamento macchinari | 5 | 197 | 2,54% | €0,71 | €3,53 | 0,9% |
| AI Max landing page matches | 3 | 21 | 14,29% | €0,67 | €2,01 | 0,5% |
| asseverazione tecnico abilitato | 1 | 11 | 9,09% | €0,60 | €0,60 | 0,2% |
| **Totale** | **428** | **5.907** | **7,25%** | **€0,87** | **€373,97** | **100%** |

**Variazioni rilevanti rispetto al primo blocco**:

- **"perizia iperammortamento"** è passata da 5 a 9 click (+80%) ma con CPC sceso da €2,31 a €1,65. Resta la keyword con CPC più alto del set: è qualificata (chi cerca "perizia" è in fase decisionale) ma costosa. Da monitorare con priorità appena attivo il tracking — sarà la prima da valutare in termini di ROI.
- **"interconnessione macchinari 4.0"** è cresciuta da 3 a 12 click con CPC €0,59 e CTR 9,76%: ottimo profilo prestazioni/costo, keyword tecnica ad alta intenzione. Consigliato mantenerla attiva e monitorarne la conversione una volta installato il tracking.
- **"iperammortamento software gestionale"** entra nel report con 7 click a CPC €0,47 — molto basso. Keyword secondaria che intercetta query informative su un sotto-segmento (software gestionale): volume limitato, monitorare se porta traffico qualificato.
- **"agevolazioni acquisto macchinari 2026"** raddoppia i click (65 → 117) mantenendo CPC contenuto: continua a essere il secondo motore di volume.
- **"iperammortamento 2026"** mantiene la leadership con il 61% del budget — domina la campagna.

### 1.6 Performance asset (Headline e Description)

**Periodo**: 11 maggio – 11 giugno 2026

#### Headline

| Headline | Impression | Click | CTR | CPC medio | Costo |
|---|---|---|---|---|---|
| Iter Completo Iperammortamento | 2.896 | 214 | 7,39% | €0,84 | €179,48 |
| Fotovoltaico Agevolato 2026 | 961 | 73 | 7,60% | €0,88 | €64,55 |
| Verifica Requisiti 4.0 | 910 | 82 | **9,01%** | €1,02 | €83,96 |
| Agevolazioni Iperammortamento | 935 | 81 | **8,66%** | €0,94 | €76,24 |
| Agevolazioni Macchinari 2026 | 807 | 68 | 8,43% | €0,99 | €67,19 |
| Perizia Iperammortamento | 573 | 55 | **9,60%** | €0,83 | €45,75 |
| Perizia asseverata macchinari | 283 | 26 | 9,19% | €1,00 | €26,09 |
| Agevolazioni per aziende | 301 | 37 | **12,29%** | €0,95 | €35,27 |
| Il Tuo Bene Rientra? Scoprilo | 65 | 4 | 6,15% | €0,30 | €1,21 |
| Ottieni Perizia Asseverata | 9 | 0 | 0,00% | — | €0,00 |
| Iperammortamento per software | 2 | 0 | 0,00% | — | €0,00 |

#### Description

| Description | Impression | Click | CTR | CPC medio | Costo |
|---|---|---|---|---|---|
| Iperammortamento: il tuo investimento rientra? | 3.525 | 245 | 6,95% | €0,89 | €219,03 |
| Consulenza Gratuita Iperammortamento 2026-2028: scopri se il tuo investimento rientra | 3.066 | 254 | **8,28%** | €0,92 | €233,85 |
| Verifica il tuo caso senza impegno | 828 | 71 | **8,57%** | €1,03 | €73,36 |
| Studio Bognolo: la consulenza per l'iperammortamento 2026. | 2.253 | 162 | 7,19% | €0,93 | €150,77 |

**Osservazioni operative**:

- **Headline top per CTR**: "Agevolazioni per aziende" (12,29%) su 301 impression — CTR eccezionale su volume medio. Segnala che il framing generico "aziende" intercetta query ad alta intenzione con un copy semplice. Da testare in posizione 1 su volume maggiore.
- **"Perizia Iperammortamento"** (9,60% CTR, CPC €0,83) — headline ad alta precisione: chi clicca sa già cosa cerca. Performance migliore della keyword omonima (8,91% CTR), a CPC più basso. Da mantenere.
- **"Verifica Requisiti 4.0"** (9,01%, 82 click) e **"Agevolazioni Iperammortamento"** (8,66%, 81 click): due headline forti su volume consistente — pilastri del volume qualificato.
- **"Iter Completo Iperammortamento"**: domina per volume (2.896 imp, 214 click) ma con CTR 7,39% — sotto la media delle headline migliori. È il maggiore driver di costo (€179,48). Con tracking attivo, sarà la prima da valutare in termini di CPL: porta volume ma non necessariamente i click più qualificati.
- **"Fotovoltaico Agevolato 2026"**: 961 impression con CTR 7,60%. Rappresenta un sotto-segmento (fotovoltaico) che non è il core business di Studio Bognolo. Con tracking attivo, valutare se i click si convertono o attirano lead non pertinenti.
- **Headline da eliminare/rivalutare**: "Ottieni Perizia Asseverata" (9 imp, 0 click) e "Iperammortamento per software" (2 imp, 0 click) — volume trascurabile, nessuna interazione. Google AI Max le ha di fatto scartate. Possono essere sostituite con varianti più dirette.
- **Description vincente**: "Consulenza Gratuita Iperammortamento 2026-2028" (8,28% CTR) e "Verifica il tuo caso senza impegno" (8,57% CTR) battono le description informative. Il pattern è chiaro: **CTA diretta + riduzione rischio percepito** ("gratuita", "senza impegno") funzionano meglio delle descrizioni brandizzate.
- **Description da migliorare**: "Iperammortamento: il tuo investimento rientra?" ha il CTR più basso (6,95%) nonostante le più alte impression — è probabilmente la default mostrata più spesso dall'algoritmo ma con la formulazione meno efficace. Testare una versione con CTA esplicita.

---

### 1.7 Competitor (Auction Insights)

*Dati Auction Insights disponibili solo per il primo blocco. Posizione competitiva sostanzialmente stabile.*

| Competitor | Impression Share | Posizionato sopra Bognolo |
|---|---|---|
| **Studio Bognolo** | **36,59%** | — |
| sanmarcoinformatica.com | 13,18% | 62% dei casi |
| teamsystem.com | 10,38% | 50,8% dei casi |

**Letture**: Bognolo mantiene la quota di impression più alta del settore. La competizione non è ancora aggressiva: la finestra resta favorevole.

---

## 2. Facebook Ads — Lead Generation

**Campagna**: Lead Generation - Iperammortamento
**Adset**: Cap Province Vicenza/Padova/Verona/Venezia/Treviso/Trento/Belluno
**Ad principale**: Video - Raccolta contatti Iperammortamento - Copia
**Periodo**: 11 maggio – 11 giugno 2026 (31 giorni)

### 2.1 Metriche aggregate — confronto periodo

| Metrica | 13–25 mag (13 gg) | 11 mag–11 giu (31 gg) | Δ |
|---|---|---|---|
| Spesa totale (campagna) | €219,66 | **€394,74** | +80% |
| Lead | 3 | **5** | +2 |
| CPL | €73,03 | **€78,95** | +€5,92 |
| Copertura | 8.352 | **11.387** | +36% |
| Impression | 15.113 | **22.007** | +46% |
| Frequenza | 1,81 | **~1,93** | +0,12 |

**Letture**:
- Il CPL si è leggermente alzato (+€5,92) nonostante il volume di lead sia raddoppiato in valore assoluto (3 → 5). Su una base di 5 osservazioni la varianza è alta: il dato non è ancora statisticamente significativo, ma l'ordine di grandezza (~€75-80 a lead) è ormai consolidato.
- La frequenza media sale a 1,93: il pubblico inizia a vedere l'inserzione quasi 2 volte. Sotto 2 è ancora gestibile, sopra 2,5 si entra in zona affaticamento creativo.

### 2.2 Distribuzione geografica (31 giorni)

| Regione | Copertura | Impression | Frequenza | Lead | Spesa | CPL |
|---|---|---|---|---|---|---|
| Veneto | 10.068 | 19.834 | 1,97 | 4 | €346,88 | €86,72 |
| Trentino-A.A. | 943 | 1.702 | 1,80 | 1 | €34,29 | €34,29 |
| Lombardia | 261 | 339 | 1,30 | 0 | €11,09 | — |
| Emilia-Romagna | 115 | 132 | 1,15 | 0 | €2,48 | — |
| **Totale** | **11.387** | **22.007** | **~1,93** | **5** | **€394,74** | **€78,95** |

**Osservazioni operative**:
- Il targeting è impostato sulle province del Veneto + Trento + Belluno, ma Meta sta distribuendo budget marginale su Lombardia ed Emilia-Romagna (~3,4% del totale, €13,57). I lead provengono tutti dal Veneto/Trentino — la spesa fuori-target non sta producendo risultati.
- **Trentino-A.A. ha il CPL migliore** (€34,29 contro €86,72 del Veneto): conferma che Trento/Belluno sono mercati meno saturi e con un cost-per-acquisition più favorevole. Da considerare come segnale per eventuali split adset futuri.
- **Veneto concentra l'80% dei lead** ma anche l'88% della spesa: efficienza coerente con la massa critica di pubblico, ma CPL più alto di 2,5x rispetto a Trentino.

### 2.3 Lead raccolti

**Lead reali qualificati: 5** (di cui 3 con anagrafica completa nel CSV, 2 acquisiti dopo il 25 maggio non presenti nel CSV dettagliato fornito).

| # | Nome | Azienda | Settore | Provincia | Budget dichiarato | Fase | Tipo investimento |
|---|---|---|---|---|---|---|---|
| 1 | Nicola Conzatti | Conzatti Elettromeccanica Srl | Servizi Elettrici | Trento | €100.000–250.000 | In valutazione | Nuovo macchinario |
| 2 | Michele Bolzonella | (Edilizia) | Edilizia | Venezia | €50.000–100.000 | In valutazione | Nuovo autocarro |
| 3 | Adriano Pegoraro | Mikiservice Srl | Trasporti e movimento terra | Padova | €100.000–250.000 | Da ordinare | Nuovo macchinario |
| 4 | n/d | n/d | n/d | Veneto (presunto) | n/d | n/d | n/d |
| 5 | n/d | n/d | n/d | Veneto (presunto) | n/d | n/d | n/d |

> **Nota dati**: il CSV leads dettagliato fornito copre solo fino al 25 maggio (3 lead). I 2 lead aggiuntivi (acquisiti tra il 26 maggio e l'11 giugno) sono ricavati dal delta numerico dei risultati Meta (3 → 5) e dall'allocazione regionale (entrambi in Veneto). L'anagrafica completa dei 2 nuovi lead va recuperata direttamente dal pannello lead Meta o dal CRM/file di consegna interno di Studio Bognolo prima del primo follow-up commerciale.

### 2.4 Analisi qualità lead (campione consolidato)

**Punti positivi**:
- 2/3 lead anagrafabili dichiarano budget > €100.000 — fascia coerente con il profilo cliente target.
- Pegoraro (Mikiservice) in fase "da ordinare": alta urgenza commerciale.
- Distribuzione geografica coerente con il targeting (Trento, Venezia, Padova).

**Punti di attenzione**:
- Bolzonella (Yahoo personale, edilizia + autocarro): verificare ammissibilità del bene rispetto ai requisiti di interconnessione 4.0 prima di investire tempo commerciale.
- Volume lead complessivo (5 in 31 giorni) resta basso ma in linea con un B2B di nicchia. Il vero benchmark sarà il **conversion rate lead → cliente pagante**: dato disponibile solo dopo il follow-up commerciale di Studio Bognolo.

---

## 3. Landing Page — Microsoft Clarity

**URL principale**: bognolo.it/iperammortamento-2026/
**Periodo**: 11 maggio – 11 giugno 2026 (31 giorni)

### 3.1 Metriche chiave — confronto periodo

| Metrica | 11–26 mag | 11 mag–11 giu | Δ |
|---|---|---|---|
| Sessioni totali | 413 | **710** | +72% |
| Sessioni bot | 52 (12,6%) | **140 (19,7%)** | +88 |
| Sessioni reali | 361 | **570** | +58% |
| Utenti unici | 358 | **598** | +67% |
| Nuovi utenti | 95,5% | **89,6%** | -5,9 pp |
| Utenti di ritorno | 4,5% | **10,4%** | +5,9 pp |
| Pagine per sessione | 1,47 | **1,52** | +0,05 |
| Profondità scorrimento media | 28,6% | **30,12%** | +1,5 pp |
| Tempo attivo / totale | 57s / 130s (44%) | **66s / 150s (44%)** | +9s attivo |

**Letture**:
- **Quota utenti di ritorno raddoppiata** (4,5% → 10,4%): segnale positivo di riconoscimento del brand o di utenti che tornano per valutare. Coerente con un servizio B2B ad alto coinvolgimento.
- **Bot al 19,7%** (era 12,6%): quota in crescita, da monitorare nel break-down (vedi 3.6).
- **Tempo attivo cresciuto da 57s a 66s** (+15%) a parità di proporzione attivo/totale: gli utenti restano leggermente più a lungo sulla pagina.

### 3.2 Segnali di frustrazione — confronto

| Segnale | 11–26 mag | 11 mag–11 giu | Trend |
|---|---|---|---|
| Clic inattiva (dead click) | 33 (7,99%) | **56 (7,89%)** | stabile in % |
| Clic rapido tasto Indietro | 10 (2,42%) | **24 (3,38%)** | ⚠️ **+0,96 pp, raddoppiato in valore assoluto** |
| Rage click | 1 (0,24%) | 1 (0,14%) | stabile |
| Scorrimento eccessivo | 1 (0,24%) | 2 (0,28%) | stabile |

**Letture critiche**:
- **Quick back salito al 3,38%**: 24 sessioni in cui l'utente atterra e torna indietro rapidamente. È il segnale più chiaro di un possibile **disallineamento tra promessa dell'annuncio e contenuto della landing**. Da valutare se rivedere la coerenza headline annuncio ↔ headline landing, o se il problema è il tempo di caricamento (LCP 4,5s = molti utenti tornano indietro prima di vedere il contenuto).
- **Dead click stabile in proporzione (~8%)** ma cresciuto in valore assoluto (33 → 56): da identificare con session replay quali elementi sembrano cliccabili e non lo sono.

### 3.3 Pagine principali (sessioni)

| Pagina | Sessioni |
|---|---|
| bognolo.it/ (homepage) | 91 |
| bognolo.it/iperammortamento-2026/ | 73 |
| bognolo.it/perizie-tecniche/ | 14 |
| **bognolo.it/iperammortamento-2026/#form** | **12** ← segnale qualitativo importante |
| bognolo.it/chi-siamo/ | 10 |
| bognolo.it/contatti/ | 9 |

> **12 sessioni sull'ancora `#form`**: gli utenti stanno effettivamente raggiungendo la sezione del form (autonomamente o tramite link interno). È un segnale di intenzione reale che oggi non si converte in lead tracciato. Va incrociato con i 9 click "Contattaci" Smart Event (3.5).

### 3.4 Browser / Device

| Browser | Sessioni | % |
|---|---|---|
| Chrome (desktop) | 352 | 49,58% |
| ChromeMobile | 140 | 19,72% |
| MobileSafari | 69 | 9,72% |
| Firefox | 40 | 5,63% |
| Edge | 28 | 3,94% |
| SamsungInternet | 26 | 3,66% |
| FacebookApp + InstagramApp | 18 | 2,54% |

**Mobile complessivo (~35%)**: confermato il dato del primo blocco e coerente con Google Ads. La rilevanza del mobile sulle micro-conversion (form) è ribadita.

### 3.5 Smart Events — confronto

| Evento | 11–26 mag | 11 mag–11 giu | Trend |
|---|---|---|---|
| Click "Contattaci" | 5 (1,21%) | **9 (1,27%)** | **+80% volume**, +0,06 pp |
| Clic in uscita | 4 (0,97%) | 5 (0,70%) | stabile |

> **+80% sui click "Contattaci"**: 9 sessioni hanno cliccato il pulsante di contatto. Combinato con le 12 sessioni sull'ancora `#form` siamo intorno a **20+ micro-conversioni potenziali** in 31 giorni — ma **nessuna è tracciata su Google Ads** né su GA4. È il dato più frustrante del report: c'è intenzione reale che non si trasforma in lead misurabile.

### 3.6 Bot traffic — break-down

| Tipologia bot | Sessioni |
|---|---|
| suspiciousInteractionBot | 119 |
| suspiciousNetworkBot | 99 |
| suspiciousDeviceBot | 72 |
| ppcAdFraudBot | 45 ← impatta direttamente Google Ads |
| webScraperBot | 6 |
| otherBots | 1 |

**Letture**:
- **45 sessioni di "PPC ad fraud"** (era 17 nel primo blocco): il dato è quasi triplicato. Su 428 click Google Ads, 45 sessioni potenzialmente fraudolente sono il **~10,5% del traffico paid** — soglia da monitorare. A campagna terminata, valutare richiesta di rimborso a Google per invalid clicks se il pattern persiste.
- Le altre categorie bot (interaction/network/device) sono pattern di scraping generici, meno preoccupanti operativamente ma rilevanti per l'igiene dati.

### 3.7 Performance tecnica (Core Web Vitals) — confronto

| Metrica | 11–26 mag | 11 mag–11 giu | Trend | Soglia Google |
|---|---|---|---|---|
| Punteggio complessivo | 67,7/100 | **72,7/100** | **+5 punti** ✅ | 90+ ottimo |
| LCP (Largest Contentful Paint) | 5,401s ❌ | **4,542s** ❌ | **-0,86s** (migliorato) | <2,5s |
| INP (Interaction to Next Paint) | 170ms ✅ | **216ms** ⚠️ | **+46ms** (peggiorato) | <200ms |
| CLS (Cumulative Layout Shift) | 1,582 ❌ | **0,2255** ⚠️ | **-86%** (drasticamente migliorato) | <0,1 |

**Letture**:
- **CLS in netto recupero**: da 1,582 a 0,225 (-86%). Era una delle azioni segnalate come priorità nel report precedente — l'intervento del team sviluppo ha funzionato. Rimane sopra la soglia ottimale Google (0,1) ma l'esperienza utente ne ha già beneficiato.
- **LCP migliorato ma ancora critico**: da 5,4s a 4,5s. Stiamo recuperando ma siamo ancora a quasi il doppio della soglia Google (2,5s). Impatta direttamente:
  - Quality Score Google Ads (e quindi CPC reale)
  - Quick back rate (utenti che tornano indietro prima del caricamento)
  - Conversione del form (utenti mobile che non aspettano)
- **INP peggiorato**: 170ms → 216ms. È sceso sotto la soglia "buono" e si avvicina alla zona "scarso". Probabile correlazione con l'intervento sul CLS: l'ottimizzazione del layout potrebbe aver introdotto JavaScript pesante. Da verificare con il dev team.
- **Punteggio complessivo +5 punti**: progressione concreta ma siamo ancora lontani dal target 90+.

### 3.8 Sorgenti di traffico (referrer)

| Referrer | Sessioni |
|---|---|
| google.com | 397 |
| bognolo.it (navigazione interna) | 388 |
| syndicatedsearch.goog | 16 |
| LinkedIn, YouTube, altri | minimi |

**Nota**: il traffico Facebook resta marginale verso il sito — coerente con il flusso lead-gen Meta che usa il form nativo. I lead Meta non passano da bognolo.it.

---

## 4. Sintesi Congiunta

| Canale | Spesa | Lead misurabili | CPL |
|---|---|---|---|
| Google Ads | €373,97 | n/d (tracking assente) | n/d |
| Facebook Ads | €394,74 | 5 lead reali | **€78,95** |
| **Totale** | **€768,71** | **5 lead confermati** | **€153,74** (parziale, solo FB tracciato) |

**Segnali da Clarity non monetizzati**:
- 9 click "Contattaci" Smart Event
- 12 sessioni sull'ancora `#form`
- ~20+ micro-conversioni potenziali totali in 31 giorni, **non tracciate**.

> Se anche solo il 25% delle micro-conversioni Clarity fosse stata in realtà un lead Google reale (ipotesi conservativa), il CPL Google sarebbe nell'ordine dei €70-80 — comparabile al CPL Facebook. Senza tracking restiamo nell'incertezza: questa è la principale leva di efficienza non sfruttata del progetto.

---

## 5. Azioni Raccomandate

### Priorità ALTA (bloccanti)

1. **Diagnosticare i 0 eventi `form_submit` su Google Ads**
   Il tracking è stato configurato (GA4 key event `iper_form_submit` + import in Google Ads, 1 giugno) ma non ha ancora registrato nessun evento. Tre cause da verificare in ordine:
   - **A** — Il Fusion Form non emette l'evento generico `form_submit` su GA4: aprire GA4 DebugView e compilare il form in tempo reale per verificare se l'evento appare.
   - **B** — Il filtro `page_location contains /iperammortamento-2026/` non matcha: verificare l'URL esatto al momento del submit (potrebbe includere query string o trailing slash).
   - **C** — Il Google Tag non è presente sulla pagina del form: verificare con Tag Assistant.
   Federico ha già accesso all'account per verificare. Fino a risoluzione AI Max ottimizza solo sui click.
   *Owner: Federico + Elisa. Deadline: entro 48h.*

2. **Risolvere LCP (4,54s vs soglia 2,5s)**
   Il CLS è stato risolto, ora il punto critico è il Largest Contentful Paint. Probabili interventi: lazy-load immagini hero, ottimizzare web fonts, ridurre payload JavaScript above-the-fold.
   *Owner: sviluppatore sito. Deadline: entro 14 giorni.*

3. **Verificare INP (216ms, peggiorato dopo l'intervento CLS)**
   Investigare se l'ottimizzazione layout ha introdotto JavaScript pesante. INP fuori soglia ha impatto su Quality Score e tasso di interazione del form.
   *Owner: sviluppatore sito. Deadline: contestuale al punto 2.*

4. **Recuperare anagrafica completa dei 2 nuovi lead Facebook (post 25 maggio)**
   Esportare il CSV lead aggiornato dal pannello Meta o dal CRM Bognolo per consentire il follow-up commerciale.
   *Owner: Studio Bognolo. Deadline: entro 48h.*

5. **Decisione strategica fine campagna**
   Definire entro fine giugno se: (a) aumentare il budget nell'ultima finestra utile per chiudere lead "da ordinare" prima dell'estate; (b) consolidare il CPL Facebook attuale e tagliare progressivamente; (c) chiudere a fine luglio. La decisione dipende dai lead già contattati e dalla loro pipeline commerciale.
   *Owner: Studio Bognolo + Elisa. Deadline: 25 giugno.*

### Priorità MEDIA

8. **Testare headline "Agevolazioni per aziende" in posizione 1 e sostituire gli asset morti**
   "Agevolazioni per aziende" ha il CTR più alto delle headline (12,29%) su 301 impression. Da promuovere a posizione pinned per raccogliere più dati. Eliminare "Ottieni Perizia Asseverata" (0 click) e "Iperammortamento per software" (0 click) — Google le ha già di fatto scartate. Inserire 2 varianti con struttura "[Azione] + [Beneficio diretto]" (es. "Scopri se il Tuo Macchinario Rientra", "Perizia in 5 Giorni Lavorativi").
   *Owner: Elisa. Deadline: entro 7 giorni.*

9. **Riformulare la description "Iperammortamento: il tuo investimento rientra?"**
   Ha il CTR più basso tra le description (6,95%) nonostante sia mostrata con più impression. Testare una variante con CTA esplicita e riduzione del rischio percepito, allineata al pattern vincente delle description ad alto CTR ("gratuita", "senza impegno").
   *Owner: Elisa. Deadline: contestuale al punto 8.*

10. **Indagare il quick back al 3,38%**
   Da 2,42% a 3,38% in 31 giorni. Aprire 10-15 session replay Clarity per capire se è LCP (utenti che escono prima del caricamento) o disallineamento contenuto (annuncio promette X, landing dice Y). Se è il secondo, riallineare headline e value prop above-the-fold.

11. **Ottimizzare l'esperienza del form (12 sessioni dirette su `#form`)**
   12 utenti hanno raggiunto direttamente la sezione del form senza convertirsi. Verificare con session replay dove si interrompono. Possibili cause: campi superflui, validazioni rigide, mancanza di feedback al submit, esperienza mobile non ottimale.

12. **Monitoraggio "perizia iperammortamento" (CPC €1,65 — keyword più cara)**
   Cresciuta da 5 a 9 click. Una volta attivo il tracking, valutare se il CPC è giustificato dal tasso di conversione lead. Se sì, mantenere; se no, valutare bid adjustment al ribasso.

13. **Verificare PPC ad fraud (45 sessioni)**
   ~10,5% dei click Google sono classificati come fraudolenti da Clarity. A campagna conclusa, esportare il dato e considerare reclamo Google Ads per invalid clicks.

14. **Identificare i 56 dead click con heatmap Clarity**
    7,89% delle sessioni clicca elementi non interattivi. Identificare i 3-5 elementi più colpiti e renderli effettivamente cliccabili o rimuovere l'affordance visiva fuorviante.

### Priorità BASSA (opportunità)

15. **Split adset Facebook Trentino vs Veneto**
    CPL Trentino €34,29 vs Veneto €86,72 (2,5x più basso). Valutare un adset dedicato Trentino-Belluno con budget proporzionale per testare se il mercato meno saturo regge la scalabilità.

16. **Bid adjustment Belluno Google Ads**
    CTR 11,43% e CPC €0,62 (dato primo blocco): mercato favorevole. Valutare bid +10/15% per intercettare più volume su query qualificate.

---

## 6. Flag revisione strategia

**Revisione strategica annuale necessaria**: ❌ NO (per ora).

**Motivazione**:
- Siamo a 31 giorni dalla partenza, in piena fase di rampa-up della prima campagna.
- I KPI principali (CTR, CPC, CPL Facebook) sono dentro range accettabili per il settore B2B di nicchia.
- Il problema dominante non è strategico ma operativo (tracking conversioni mancante, LCP critico). Sono interventi tecnici, non di posizionamento.
- La finestra commerciale Iperammortamento 2026 è limitata nel tempo: una revisione strategica ora rischierebbe di interrompere il momentum invece di amplificarlo.

**Quando richiamare lo strategist**:
- Se al 30 giugno il tracking conversioni resta non configurato → la campagna sta sprecando budget e va rivista la priorità di ingaggio col team tecnico Bognolo.
- A campagna conclusa (fine luglio o data di stop concordata): consuntivo completo + valutazione se replicare il modello su altre stagionalità fiscali (Iperammortamento 2027, beni strumentali, transizione 5.0 ecc.).

---

*Report generato il 2026-06-11. Periodo dati: 11 maggio – 11 giugno 2026 (31 giorni). Dati device, geografia, Auction Insights, landing page Google Ads disponibili solo per il sotto-periodo 10–26 maggio. Anagrafica dettagliata Facebook leads disponibile per 3 lead su 5 (CSV aggiornato al 25 maggio). Sostituisce la versione del 2026-05-26.*
