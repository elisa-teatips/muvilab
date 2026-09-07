---
client: muvi-neogela
phase: 05-reports
period: 2026-06-01 – 2026-08-31
status: draft
owner: elisa@teatips.it
last_updated: 2026-09-07
---

# Neogela — Organico Meta (Facebook + Instagram) e TikTok, 1 giugno – 31 agosto 2026

> **Perimetro di questo file.** È il `report.md` della fase, ma copre la sola parte **organica**. La parte **paid** dello stesso periodo vive nei file di dettaglio accanto, ed è parte integrante del report:
> - [analisi-dati-meta-giu-ago-google-lifetime.md](./analisi-dati-meta-giu-ago-google-lifetime.md) — Meta Ads giu-ago, Google Ads storico
> - [keyword-shopping-tiktok-1lug-31ago.md](./keyword-shopping-tiktok-1lug-31ago.md) — keyword, Shopping, TikTok Ads
> - [recap-team-meta-giu-ago-google-lifetime.md](./recap-team-meta-giu-ago-google-lifetime.md) — recap sintetico paid
>
> La lettura trasversale paid + organico, con le considerazioni qualitative per il team, è in [mail.md](./mail.md).

**Fonti:** Meta Business Suite (Insights → Risultati e Contenuti, `time_range` personalizzato 1/6–31/8) e TikTok Studio Analytics, letti da interfaccia via estensione Chrome il 07/09/2026. Nessun export scaricato.

**Perimetro:** completa e sostituisce per il trimestre estivo la lettura parziale di [organico-social-maggio-luglio2026.md](../../2026-08-24/outputs/organico-social-maggio-luglio2026.md), che si fermava al 31 luglio (e per Instagram al solo mese di luglio).

**Nota metodologica su TikTok:** le tab "Contenuto", "Spettatori" e "Follower" di TikTok Studio non accettano un intervallo personalizzato (l'opzione esiste ma è disabilitata). I dati di periodo sono stati ottenuti interrogando l'endpoint dati interno `aweme/v2/data/insight` con finestre esplicite. **Il metodo è stato calibrato** riproducendo la finestra 30/06–31/07 già verificata nella raccolta del 24/08: risultato 223.279 visualizzazioni, **identico** al dato registrato allora. I numeri TikTok di questo documento sono quindi verificati, non stimati.

---

## 1. META — livello account

| Metrica | Facebook | Instagram |
|---|---:|---:|
| Visualizzazioni | ≈1,9 mln (+1,1%) * | 833.463 (+19,2%) |
| Copertura (account unici) | 420.156 (+27,8%) | 196.633 (+4,9%) |
| Interazioni con i contenuti | 3.706 (+45,9%) | 4.905 (+1,7%) |
| Clic sul link | 41.887 (+2,4%) | 28.601 (−0,4%) |
| Visite (pagina / profilo) | 7.408 (+18,6%) | 69.785 (+32,8%) |
| Follow | 495 (+36,7%) | 2.233 (−12,7%) |

Le variazioni percentuali sono quelle esposte da Meta rispetto ai 3 mesi precedenti (mar–mag 2026).

\* Meta espone questo valore arrotondato ("1,9 mln") e non il numero esatto.

**Due avvertenze di lettura, per non confondere queste righe con la tabella del capitolo 2:**
- Le metriche di account sono **generate nel periodo su tutto ciò che circola**, inclusi contenuti pubblicati prima del 1° giugno che continuano a ricevere visualizzazioni. La tabella dei contenuti (cap. 2) misura invece **solo gli 82 post pubblicati dentro la finestra**. È la ragione per cui i due totali non coincidono e non devono coincidere.
- Le card di account possono includere anche visualizzazioni generate da contenuti sponsorizzati, mentre la vista contenuti è organica. Dove serve una lettura puramente organica, fare riferimento al capitolo 2.

### Osservazioni

- **Le interazioni su Facebook sono in crescita del 45,9%, non in calo.** Questo corregge una lettura della relazione precedente: guardando i soli mesi maggio→giugno→luglio le interazioni sembravano crollate (1.642 → 891 → 955), ma quel confronto era interno a una finestra che partiva da un maggio eccezionale. Sul trimestre pieno, confrontato col trimestre precedente, Facebook è in crescita su tutto tranne i clic sul link. **Da correggere prima che finisca nel report al cliente.**
- **Instagram porta 2.233 follower contro i 495 di Facebook** — 4,5 volte tanto, pur con un quarto delle visualizzazioni. Resta il motore di crescita del profilo.
- **Instagram è però l'unica metrica in flessione sui follow (−12,7%)**, mentre le visite al profilo crescono del 32,8%: arriva più gente sul profilo ma una quota minore decide di seguire. Vale la pena guardare bio e primi 9 post in griglia, che sono ciò che vede chi atterra.
- **Attenzione ad attribuire all'organico le visite al profilo Instagram**: nello stesso periodo la campagna Meta "BAU Cold – Visite al profilo IG" ha generato 48.963 visite al profilo a pagamento su un totale di 69.785. Circa il **70% del traffico al profilo è a pagamento**, non organico. È un dato da presentare con onestà: giustifica il budget di quella campagna, ma ridimensiona la lettura "l'organico su IG sta esplodendo".

---

## 2. META — livello contenuti (82 post pubblicati nel periodo)

| Mese | Piattaforma | Post | Copertura | Visualizz. | Interazioni | Like | Condiv. | Salvat. | Commenti |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Giugno | Instagram | 12 | 27.679 | 36.834 | 573 | 391 | 56 | 80 | 32 |
| Giugno | Facebook | 11 | 21.624 | 23.836 | 263 | 189 | 30 | 23 | 21 |
| Luglio | Instagram | 16 | 31.412 | 42.004 | 489 | 346 | 28 | 75 | 28 |
| Luglio | Facebook | 14 | 42.768 | 44.591 | 398 | 295 | 33 | 51 | 19 |
| Agosto | Instagram | 14 | 22.029 | 31.724 | 448 | 253 | 29 | **129** | 21 |
| Agosto | Facebook | 14 | 14.408 | 16.087 | 129 | 79 | 21 | 23 | 6 |
| Agosto | Storia cross | 1 | 279 | 331 | 4 | 4 | 0 | — | — |
| **Totale** | | **82** | **160.199** | **195.407** | **2.304** | **1.557** | **197** | **381** | **127** |

Cadenza mantenuta e regolare: 23 post a giugno, 30 a luglio, 29 ad agosto (contando entrambe le piattaforme). Nessun buco editoriale estivo.

### Top 10 contenuti per visualizzazioni

| # | Data | Piatt. | Formato | Contenuto | Copertura | Visualizz. | Interaz. | Salvat. |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 22 lug | FB | Reel | Calcio alto nel sangue? Un segnale importante | 22.503 | **22.252** | 219 | 28 |
| 2 | 15 giu | FB | Reel | Sai che le ossa sono vive? | 10.470 | 11.359 | 175 | 17 |
| 3 | 31 lug | FB | Reel | Le ossa non danno segnali | 6.221 | 6.752 | 56 | 5 |
| 4 | 31 lug | IG | Reel | Uno degli aspetti più insidiosi dell'osteoporosi | 4.837 | 6.486 | 81 | 10 |
| 5 | 12 ago | FB | Reel | **[UGC]** Le tue ossa si rinnovano ogni giorno | 4.642 | 5.449 | 53 | 13 |
| 6 | 15 giu | IG | Reel | Pensi che le ossa siano solo "pezzi duri"? | 3.968 | 5.091 | 131 | 15 |
| 7 | 12 ago | IG | Reel | **[UGC]** Le articolazioni non chiedono il permesso | 3.666 | 5.040 | **109** | **37** |
| 8 | 10 ago | IG | Carosello | Davanti a un referto della MOC ci si sente spaesati | 2.497 | 5.011 | 85 | **48** |
| 9 | 17 lug | IG | Reel | Se usi il collagene, probabilmente… | 3.045 | 4.797 | 25 | 4 |
| 10 | 26 giu | IG | Reel | Dopo i 40 anni perdi massa muscolare | 3.589 | 4.753 | 77 | 10 |

### Osservazioni sui contenuti

- **Il picco assoluto del trimestre è il reel Facebook del 22 luglio "Calcio alto nel sangue"**, con 22.252 visualizzazioni: da solo vale più di tutti i post Facebook di agosto messi insieme. È un contenuto di tipo "segnale d'allarme da un esame che hai già fatto" — lo stesso angolo del referto MOC. Conferma quale leva funziona su questo pubblico: **partire da un dato clinico che la persona ha già in mano**, non dal prodotto.
- **Agosto è il mese con più salvataggi su Instagram (129)** nonostante meno visualizzazioni di giugno e luglio. Il tasso di salvataggio passa da 0,22% (giugno) a 0,41% (agosto): meno persone raggiunte ma più intenzione. I due contenuti che trainano sono il carosello sul referto MOC (48 salvataggi) e il reel UGC (37).
- **Il carosello del 10 agosto sul referto MOC ha il miglior tasso di salvataggio del trimestre** (48 salvataggi su 2.497 di copertura = 1,9%). È materiale che la gente si mette da parte per rileggerlo — esattamente il comportamento che ci si aspetta da un lead magnet. Vale la pena valutarlo come base per una guida scaricabile.
- **Facebook ad agosto dimezza le interazioni** (129 contro 398 di luglio) a parità di post pubblicati. Non è un problema editoriale: è il mese in cui Facebook ha distribuito meno.

---

## 3. Il post UGC del 12 agosto — analisi dedicata

Stesso creativo pubblicato su entrambe le piattaforme (verificato: inquadratura casalinga, tazza di caffè e barattolo Neogela tenuto in mano — riconoscibile come contenuto di creator, non come grafica di brand).

| Metrica | Instagram (12:13) | Facebook (12:01) | Totale |
|---|---:|---:|---:|
| Visualizzazioni | 5.040 | 5.449 | **10.489** |
| Copertura | 3.666 | 4.642 | 8.308 |
| Interazioni nette | 109 | 53 | 162 |
| "Mi piace" | 48 | 28 | 76 |
| Commenti | 10 | 2 | 12 |
| Condivisioni | 12 | 10 | 22 |
| Salvataggi | 37 | 13 | 50 |
| **Nuovi follow generati** | 6 | 3 | **9** |
| Tempo di visualizzazione medio | **15 s** | **13 s** | — |
| Tempo di visualizzazione totale | 15h 34m | 17h 26m | 33h |

**Meta lo segnala esplicitamente sopra la media** dei contenuti recenti su tutte e tre le dimensioni — visualizzazioni, copertura e interazioni — su entrambe le piattaforme.

### Perché ha funzionato

- **Ritenzione (dato Facebook)**: 99,8% di chi lo apre resta ai primi secondi, 83% è ancora lì a 4 secondi, 62% a 6 secondi. L'abbandono principale è a 0:06 e il tempo medio è 13 secondi. 1.342 persone lo hanno guardato per almeno 15 secondi. Per un contenuto di brand su un integratore sono numeri molto buoni.
- **Distribuzione**: l'82,2% del tempo di visualizzazione su Facebook arriva dai **"Consigli"** (utenti che non ci seguono), solo il 17,7% dai follower. È il contenuto che ha lavorato meglio come acquisizione, non come fidelizzazione.
- **È il post che ha generato più follow del trimestre in rapporto alla copertura**: 9 nuovi follower su 8.308 persone raggiunte.
- **Il pubblico raggiunto è esattamente il target**: donne 93,3% su Instagram e 86,4% su Facebook; su Facebook il 75,7% ha più di 55 anni (65+ 46,8%, 55-64 28,9%). Geograficamente ben distribuito su tutta Italia — Lombardia 355, Sicilia 352, Lazio 332, Campania 303, Puglia 228.

### I commenti dicono più dei numeri

Sotto il post ci sono conversazioni d'acquisto reali, non complimenti generici:

- *"Costa un po' tanto"* → obiezione prezzo, arrivata spontaneamente
- *"Ma è il migliore… la salute non ha prezzo"* → risposta di un'altra utente, non nostra
- *"Buonissimo sono al secondo ordine"* → cliente ricorrente che si autoidentifica

**⚠️ Segnalazione di compliance da girare a Giulia.** Due commenti chiedono se il prodotto sia compatibile con terapie oncologiche in corso — uno cita esplicitamente il **Letrozolo** (farmaco per il tumore al seno). Sono domande a cui **non possiamo rispondere nel merito**: il prodotto è un integratore alimentare, i claim terapeutici sono vietati e il disclaimer "non sostituisce terapie mediche prescritte" è obbligatorio. Serve una risposta standard concordata da usare in questi casi, che rimandi al medico curante senza sbilanciarsi. Segnalo anche che il community management è escluso dal nostro contratto: **queste risposte le deve dare il cliente**, ma va avvisato che stanno arrivando domande di questo tipo.

### Cosa ne ricaviamo

Il formato UGC ha battuto la media su un pubblico freddo, con ritenzione alta e commenti che aprono conversazioni d'acquisto. Con un solo contenuto non si fa una strategia, ma il segnale è abbastanza netto da giustificare **almeno 2-3 altri UGC prima della stagione alta di ottobre-novembre**, e da riprendere il discorso con Giulia sulle piattaforme UGC che stava riattivando.

---

## 4. TIKTOK — 1 giugno – 31 agosto 2026

### Trimestre

| Metrica | Valore |
|---|---:|
| Visualizzazioni video | 613.612 |
| Copertura | 441.648 |
| Visite al profilo | 1.702 |
| Mi piace | 2.432 |
| Commenti | 98 |
| Condivisioni | 334 |
| Follower | 7.016 → 7.206 (**+190**) |

### Il dato che conta: l'andamento mensile

| Metrica | Giugno | Luglio | Agosto | ago vs giu |
|---|---:|---:|---:|---:|
| Visualizzazioni | 335.517 | 222.978 | **55.117** | **−84%** |
| Copertura | 225.578 | 181.803 | **34.267** | **−85%** |
| Visite al profilo | 917 | 716 | **69** | **−92%** |
| Mi piace | 1.348 | 978 | 106 | −92% |
| Commenti | 52 | 38 | 8 | −85% |
| Condivisioni | 175 | 149 | 10 | −94% |
| Follower netti | +121 | +83 | **−13** | — |

**Ad agosto il canale TikTok si è fermato.** Non è un rallentamento fisiologico da mese estivo: è un crollo dell'85% della distribuzione, con i follower netti **negativi per la prima volta** nel periodo osservato.

### Non è un problema di quanto pubblichiamo

La cadenza editoriale è stata mantenuta: tra il 12 agosto e il 4 settembre sono usciti 8 post, circa 2-3 a settimana, in linea con giugno e luglio. Il problema è quanto ciascun post viene distribuito: **i contenuti recenti raccolgono tra 90 e 283 visualizzazioni ciascuno**, contro le migliaia dei mesi precedenti.

Detto altrimenti: stiamo pubblicando come prima, TikTok ha smesso di mostrarci.

### Cosa può averlo causato — e cosa verificare

Non ho elementi per stabilirlo con certezza dai soli dati di analytics, ma le ipotesi da controllare in ordine di probabilità sono:

1. **Penalizzazione dell'account legata ai problemi di policy sulle campagne.** Ad agosto la campagna "Conversione Agosto" si è fermata per "Review issue" su salute/integratori. Se TikTok ha applicato una limitazione a livello di account — non solo sulle ads — questo spiegherebbe perché l'organico crolla nello stesso mese. **È l'ipotesi da verificare per prima**, e alza ulteriormente la priorità di parlare con l'assistenza TikTok.
2. **Cambio di contenuti o formato** in agosto rispetto ai mesi precedenti.
3. **Normale volatilità dell'algoritmo** dopo che giugno e luglio erano stati trainati da pochi video ad alta distribuzione.

Il punto 1 è quello che cambia le decisioni: se l'account è limitato, non ha senso investire budget né tempo di produzione su TikTok finché non si risolve.

### Engagement

L'engagement rate sul trimestre è **0,47%** sulle visualizzazioni (2.864 interazioni su 613.612 views). Basso in assoluto, ma coerente con un canale che distribuisce a pubblico freddo. Il vero problema non è il tasso, è che ad agosto è sparito il denominatore.

---

## 5. Lettura d'insieme dei tre canali

| | Facebook | Instagram | TikTok |
|---|---|---|---|
| Visualizzazioni trimestre | 1,9 mln | 833.463 | 613.612 |
| Copertura trimestre | 420.156 | 196.633 | 441.648 |
| Follower acquisiti | +495 | +2.233 | +190 |
| Engagement su views | 0,20% | 0,59% | 0,47% |
| Ruolo | volume e copertura, pubblico passivo | crescita follower e salvataggi | notorietà, oggi bloccato |

**Instagram è il canale che costruisce base**: un quarto delle visualizzazioni di Facebook ma 4,5 volte i follower acquisiti e il tasso di interazione più alto. **Facebook è il canale che fa numeri**: distribuisce moltissimo a persone che non ci seguono (l'82% del tempo di visualizzazione del post UGC arriva dai Consigli), ma quel pubblico guarda e va oltre — ed è la ragione tecnica per cui su Facebook si vedono tante visualizzazioni e pochi "mi piace". **TikTok era il terzo canale di copertura e ad agosto si è fermato.**

L'angolo che funziona è lo stesso su tutte e tre le piattaforme, ed è quello già identificato: **partire da un esame, un referto o un sintomo che la persona ha già davanti** — calcio alto nel sangue, referto MOC, dolore articolare ricorrente — e non dal prodotto.

---

## 6. Azioni che escono da questa lettura

- [ ] **Correggere la lettura sull'organico Facebook** prima che vada nel report: le interazioni sono +45,9% sul trimestre, non in calo
- [ ] **Verificare se l'account TikTok è limitato** a livello organico oltre che pubblicitario — è la domanda da fare all'assistenza insieme al problema delle campagne
- [ ] **Girare a Giulia la segnalazione di compliance** sui commenti relativi a terapie oncologiche, e concordare una risposta standard (il community management è fuori dal nostro perimetro, ma l'alert va dato)
- [ ] **Programmare 2-3 contenuti UGC** prima di ottobre, visto il risultato del 12 agosto
- [ ] **Valutare il carosello "referto MOC" come base per un lead magnet** — è il contenuto con il miglior tasso di salvataggio del trimestre
- [ ] **Guardare bio e griglia Instagram**: visite al profilo +32,8% ma follow −12,7%
- [ ] Presentare le visite al profilo IG distinguendo organico e a pagamento (48.963 delle 69.785 sono da campagna BAU)
