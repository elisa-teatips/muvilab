---
client: muvi-neogela
phase: 03-ped
period: 2026-09
status: draft
owner: elisa
last_updated: 2026-09-07
note: selezione contenuti dal bacino "Da montare" richiesta il 07/09/2026, rivista sul vincolo di 3 uscite/settimana e sul vincolo di collegamento al blog emerso in call con Elena. Il PED di settembre è in stato approved: applicare modifiche a ped.md lo riporta in in-review e richiede un nuovo touch-point mail.
---

# Selezione contenuti "Da montare" — shooting agosto 2026

## 1. Fonte e perimetro

**Fonte usata**: export Notion del database **ZETA 92 - Content Plan** (07/09/2026), archiviato in
`clients/muvi-neogela/phases/03-ped/2026-09/inputs/`. Filtro: `Brand = Neogela`, `Stato = 💻 Da montare`.

**Risultato**: 13 contenuti, di cui **2 esclusi** come richiesto perché `Formato = Video YouTube`
(Spieghiamo il collagene e i suoi benefici · Studi clinici sul collagene). Restano **11 candidati**.

**+1 recuperato fuori filtro**: `"3 segnali che il tuo corpo ti manda quando ha bisogno di collagene"` risulta
censito come `💡 Idea`, ma ha `Data di registrazione = 03/07/2026`, soggetto Giulia e **script completo**: è
girato, non è un'idea. Errore di stato in Notion, da correggere. Lo conto tra i disponibili → **12 contenuti
pronti al montaggio**.

Verificato che nessun altro stato contiene materiale utilizzabile: i 17 `🗓️ Programmato` hanno tutti date di
pubblicazione 2025 (residui legacy), i restanti 35 `💡 Idea` non hanno né script né data di registrazione.

### ⚠️ Bacino Notion "Contenuti → I Miei Contenuti → Da montare" — non enumerabile (aggiornato 07/09)

**Correzione rispetto alla prima versione di questo documento**: non è un problema di permessi dell'account
Guest, come avevo scritto. È un problema di **filtri delle viste**.

Aprendo il pannello filtri della vista *Per Cliente* del database **Contenuti**, i filtri attivi sono tre:

- `Status: Not ✅ Pubblicato, …`
- `Categoria: Video Social, V…`
- `Progetto Social: Contains …`

Il terzo filtro è agganciato a un progetto specifico, e per questo la vista restituisce zero righe. La vista
*I Miei Contenuti* filtra invece su `Social Media Manager: Contains Me`, che non risolve sul record persona di
Elisa (restituisce 2 sole schede, nessuna Neogela). *Periodo Editing* e *Calendar* sono viste timeline e non
mostrano elenchi utilizzabili.

I dati **ci sono**: la relazione `194 Contenuti` sulla pagina *Comunicazione Neogela* li elenca tutti, e le
singole schede si aprono dalla ricerca (es. "Neogela nella vita reale" → `Status: 💪🏻 Da pubblicare`,
SMM Elisa Moratello). Ma né la relazione né la ricerca mostrano lo **Status**, quindi non è possibile isolare
i "Da montare" senza aprire le schede una per una.

**Quindi la domanda "c'è altro disponibile lì dentro?" resta aperta — non ho una risposta negativa, ho una
non-risposta.** Per scioglierla serve una di queste tre cose, tutte rapide:

1. duplicare *I Miei Contenuti* in una vista personale e sostituire il filtro "Contains Me" con
   `Progetto Social = Comunicazione Neogela` + raggruppamento per Status;
2. correggere il filtro `Progetto Social` della vista *Per Cliente*;
3. farsi esportare la vista da chi ha ruolo Member.

Finché non è sciolta, la fonte utilizzata resta il **ZETA 92 - Content Plan**, di cui ho verificato in Notion
la vista **"Da montare"**: 13 record, identici all'export.

---

## 2. Vincolo bloccante: questi video sono legati al blog

Dalla call con Elena, riferito **allo shooting di agosto per Neogela** (quello con Giovanni):

- lo shooting "era più basato sul blog";
- Giulia ha ripreso in mano gli articoli del blog e su quegli articoli **vorrebbe fare dei quiz** — meccanismo che
  Elena stessa ha detto di non aver capito bene;
- alla fine ha voluto far girare dei video **che comunque possono uscire come contenuti**.

Questo si legge direttamente negli script: **tutti e 10 i video del batch agosto si chiudono con un rimando
all'articolo** ("Nell'articolo ti spiego…") e portano **due chiusure alternative fra cui va scelta una sola** —
`▶ CTA A · QUIZ` e `▶ CTA B · INTERAZIONE`. Non è un dettaglio di copy: è la variabile che decide se e quando
ciascun video può uscire.

### Cosa ne consegue per la programmazione

1. **Un video con chiusura "nell'articolo" non può essere programmato prima che il suo articolo sia online.**
   Per ognuno dei 12 servono due informazioni: *è collegato a un articolo?* e *quell'articolo è pubblicato, e da
   quando?* Senza questa mappatura il calendario di ottobre si può impostare ma non chiudere.
2. **La CTA quiz resta sospesa.** Gli script dicono "fai il nostro quiz sulla salute delle tue ossa", che sembra
   il quiz di lead generation già esistente (quello che ha girato a €0,17 a contatto). Ma l'idea di Giulia è di
   fare quiz **sui singoli articoli**, che è un'altra cosa e non è chiaro se esista. Finché non lo sappiamo,
   **default a `CTA B · Interazione` su tutti**: è l'unica chiusura che funziona sia con sia senza blog e quiz,
   e non manda traffico verso qualcosa che potrebbe non esserci.
3. **Se sono collegati al blog, nel calendario editoriale va previsto il link** — come chiedeva Elena. Va deciso
   dove: link in caption, in bio, o sticker/commento fissato.

### ⚠️ Rischio sul blog: Eva non c'è più

Nel framework il blog risulta **"gestito internamente da Eva con supervisione Giulia"**
(`04-campaigns/2026-06/inputs/_scratch.md` e `2026-07/inputs/_scratch.md`). Con Eva fuori e Giulia unica
referente, **12 delle 13 uscite di ottobre dipendono da articoli il cui proprietario interno non c'è più**.
Da chiedere a Giulia insieme al resto: chi gestisce ora il blog e con che calendario di pubblicazione.

### Chi sblocca cosa

| Domanda | A chi | Quando |
|---------|-------|--------|
| "Come sono, come non sono" questi video — cosa è montabile e in che stato | Elena → punto con Gio | **venerdì 11/09** |
| Ciascun video è collegato a un articolo? Quale, ed è pubblicato? | **Giulia** | da chiedere |
| Possiamo usare questi video nei prossimi mesi (ottobre incluso)? | **Giulia** | da chiedere |
| I quiz sugli articoli esistono / sono previsti? La CTA quiz punta a quale quiz? | **Giulia** | da chiedere |
| Chi gestisce il blog ora che Eva non c'è più, e con che calendario | **Giulia** | da chiedere |

Giulia è ora **l'unica referente** e non ha ancora risposto alla mail del 01/09 su promo ottobre e Black Friday
(`03-ped/2026-10/inputs/`). Conviene **accorpare queste domande a quel sollecito** invece di aprire un terzo
thread: da lei dipendono ormai sia il piano contenuti sia il piano campagne di ottobre.

---

## 3. Il conto: 3 uscite a settimana

Oggi è **lunedì 07/09/2026**.

### Fabbisogno

| Periodo | Settimane | Uscite a 3/sett. |
|---------|-----------|------------------|
| Settembre residuo (08→30/09) | 07-13 (restano 2 slot) · 14-20 · 21-27 · 28-30 | **10** |
| Ottobre | 1-4 · 5-11 · 12-18 · 19-25 · 26-31 | **13** |
| | | **23 totali** |

### Disponibilità reale

| Voce | Quantità | Note |
|------|----------|------|
| Contenuti pronti al montaggio (§1) | **12** | girati e con script — ma **subordinati al vincolo blog** (§2) |
| Slot settembre già assegnati nel PED approvato | 10 | dal 09/09 al 30/09 — stato di produzione da verificare |
| Altro materiale utilizzabile | 0 | il resto del bacino è o legacy o non girato |

### Conclusione

**7 contenuti in riserva non coprono ottobre**, che ne chiede 13. E il problema è più a monte: 12 contenuti
pronti contro 23 uscite da qui a fine ottobre. Il conto chiude solo in uno scenario:

- **Se i 10 slot di settembre sono coperti e in produzione** → settembre si chiude senza toccare il batch, i 12
  vanno interi su ottobre e coprono 12 uscite su 13. **Manca 1 contenuto.**
- **Se i 10 slot di settembre sono fermi** → i 12 si consumano quasi tutti per chiudere settembre e
  **ottobre resta scoperto per ~13 uscite**, nel mese dell'osteoporosi.

La differenza fra i due scenari è di **12 contenuti**, cioè uno shooting intero.

A questa incognita se ne aggiunge ora una seconda, indipendente: anche nello scenario buono, i 12 sono
utilizzabili **solo se il vincolo blog si scioglie** (§2). Sono due gap distinti che si sommano.

---

## 4. Raccomandazione

**Non spezzare il batch.** La proposta iniziale (4 a settembre, 7 a ottobre) non regge né il vincolo di
3/settimana né quello del blog: le 4 sostituzioni erano a saldo zero — spostavano contenuti in riserva invece di
aggiungerne — e avrebbero mandato in onda contenuti con rimando al blog prima di sapere se il rimando regge.

1. **I 12 restano bloccati per ottobre**, dove coprono 12 uscite su 13 e sono tematicamente il mese
   dell'osteoporosi. È l'unico modo di arrivare al 20/10 con un piano pieno senza girare nulla.
2. **Settembre si chiude con quello che è già in produzione.** Se e solo se uno slot è fermo, si pesca dal batch
   **un contenuto alla volta**, sapendo che ogni prelievo toglie 1:1 a ottobre. Priorità di prelievo, scelta fra
   i contenuti **meno dipendenti dal blog**: "3 segnali che il tuo corpo ti manda…" (chiusura autonoma:
   salva + commenta, nessun rimando all'articolo) → "Fratture da fragilità" (chiusura generica) → poi il batch
   agosto, ma solo con `CTA B`.
3. **Prenotare la data dello shooting di ottobre adesso**, senza aspettare Giulia. Nello scenario migliore serve
   1 contenuto, nel peggiore 13; ma il vincolo vero è il preavviso — Dott. Zeggio almeno una settimana, altri
   specialisti ~10 giorni (`clients/muvi-neogela/AGENTS.md`). Prenotare ora, dimensionare dopo venerdì.
4. **Il PED di ottobre non si apre finché §2 non è sciolto.** Si può impostare la struttura, non fissare le date.

---

## 5. I 12 contenuti disponibili

### A. Batch shooting agosto 2026 — serie blog/SEO (10)

Blocco editoriale unico: stessa struttura, stesso registro, tutti chiusi con rimando all'articolo di blog.
**CTA consigliata: `B · Interazione` su tutti**, finché Giulia non chiarisce blog e quiz (§2).

| # | Contenuto | Tipologia | Angolo / hook |
|---|-----------|-----------|---------------|
| 1 | Osteoporosi — sintomi e campanelli d'allarme | Informativo | "L'osteoporosi non fa male. Ed è proprio questo il problema." |
| 2 | Osteoporosi cause — perché si presenta | Informativo | 5 milioni di persone in Italia; il collagene come impalcatura dell'osso |
| 3 | MOC — diagnosticare la fragilità ossea | Informativo | "Possiamo scoprire l'osteoporosi prima della prima frattura?" |
| 4 | Osteopenia — cos'è, significato e come si cura | Informativo | "Ti hanno trovato un valore di osteopenia? Non spaventarti. Ma prendilo sul serio." |
| 5 | Fratture da osteoporosi — proteggersi e guarire prima | Informativo | "In Italia, in un minuto, avviene una frattura da fragilità" |
| 6 | Crolli vertebrali da osteoporosi | Informativo | "Una vertebra può cedere mentre ti allacci le scarpe" |
| 7 | Osteoporosi maschile — la patologia ignorata | Informativo | 1 uomo su 5 dopo i 50 anni |
| 8 | Osteoporosi post menopausa — non sei sola | Informativo | 1 donna su 3 dopo i 50 anni — la CTA B qui è la più forte del batch |
| 9 | Calcio alto nel sangue e osteoporosi (ipercalcemia) | Informativo | Controintuitivo: calcio alto ≠ ossa forti |
| 10 | Artrosi all'anca e sport | Consigli | "Temi di dover smettere di fare sport? La risposta è no." |

Se Giulia conferma blog e quiz, i tre a intento più alto su cui riportare `CTA A · Quiz` sono **#4 Osteopenia**,
**#3 MOC** e **#1 Sintomi**: chi ha appena letto "osteopenia" o "T-score" su un referto è il lead migliore.

### B. Residui shooting 03/07/2026 (2) — non legati al blog

| # | Contenuto | Soggetto | Note |
|---|-----------|----------|------|
| 11 | "Fratture da fragilità: cosa sono e perché aumentano con l'età" | Doc (Dott. Zeggio) | Chiusura debole ("continua a seguirci"), **CTA da riscrivere**. Passaggio caregiver esplicito. Introduce il concetto che tre contenuti del batch agosto riprendono. |
| 12 | "3 segnali che il tuo corpo ti manda quando ha bisogno di collagene" | Giulia | Censito per errore come `💡 Idea`. Chiusura autonoma già pronta (salva + commenta), **nessun rimando all'articolo** → è il contenuto più subito utilizzabile dei 12. Unico sul pillar prodotto/collagene anziché patologia. |

---

## 6. Verifiche di compliance prima del montaggio

- **Titolo "Osteopenia — cos'è, significato e come si cura"**: è un titolo SEO da blog. In video/caption la parola
  **"cura"** accostata a un integratore è un claim terapeutico → riformulare per il social
  (es. "Osteopenia: cosa significa davvero e cosa puoi fare adesso").
- **Disclaimer obbligatorio** "non sostituisce terapie mediche prescritte" su tutti i contenuti che parlano di
  diagnosi, MOC, farmaci o percorsi di cura (`clients/muvi-neogela/AGENTS.md`).
- **Dati numerici con fonte**: "1 donna su 3", "1 uomo su 5", "quasi 5 milioni di persone", "una frattura al
  minuto", "T-score tra -1 e -2,5".
- Lo script #3 (MOC) contiene un consiglio clinico in prima persona ("oggi consiglio soprattutto in menopausa e
  dopo i 70 anni"): accettabile solo pronunciato dal medico in video, non riportabile in caption a nome brand.

---

## 7. Decisioni che servono

1. **Da Giulia** (accorpare al sollecito della mail 01/09): collegamento blog per ciascun video · utilizzabilità
   nei prossimi mesi · quiz sugli articoli · chi gestisce il blog dopo Eva. → §2
2. **Da Elena/Gio, venerdì 11/09**: stato reale dei video di agosto.
3. **Stato di produzione dei 10 slot di settembre** (09→30/09) — la domanda che vale 12 contenuti. Segnale: sulla
   scheda Notion del video del 01/09 lo scambio è ancora aperto ("siamo in attesa del contenuto, quindi intanto
   non procediamo con il copy").
4. **Data shooting ottobre** — da prenotare ora, dimensionare dopo venerdì.
5. **Accesso Notion** al DB *Contenuti* (§1).
6. **Correzione stato** in Notion di "3 segnali che il tuo corpo ti manda…": da `💡 Idea` a `💻 Da montare`.
7. Aggiornare i referenti in `context/accesses.md` e la lista approvatori dei touch-point mail dopo l'uscita di
   Eva (le mail di `04-campaigns/2026-09` sono indirizzate anche a lei).
8. Ogni modifica a `ped.md` riporta il PED da `approved` a `in-review` e richiede un nuovo touch-point mail.
