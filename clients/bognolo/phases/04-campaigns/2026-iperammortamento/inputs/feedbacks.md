---
client: bognolo
phase: 04-campaigns
campaign: 2026-iperammortamento
status: in-review
owner: elisa
last_updated: 2026-06-11
---

# Feedbacks e decisioni operative — Campagna Iperammortamento 2026

Registro cronologico delle decisioni prese durante la campagna. Fonte primaria: catena email interna Muvi Lab (29 maggio – 5 giugno 2026) e aggiornamenti successivi.

---

## [2026-05-29] Feedback post-condivisione cliente — Elena

**Fonte**: email Elena Caccia → team interno, 29 maggio 2026

### Form landing + Meta
- Tenere solo la prima slide del form; P.IVA e telefono diventano **facoltativi**
- Form Meta: aggiungere link prenotazione slot Google Calendar: `https://calendar.app.google/UApLCnj6vwcp22ZTA`

### Google Ads — keyword
- Aggiungere keyword action-oriented: *"richiedi perizia"*, *"consulenza iperammortamento"*
- Aggiungere anche: *"perizia asseverata"*

### Geo
- Aggiungere **Emilia-Romagna + Lombardia (intera)** sia a Meta che a Google Ads

### Contenuti (confermato dal cliente)
- La perizia asseverata è obbligatoria e non può essere svolta in autonomia: richiede firma di ingegnere o perito iscritto all'ordine. Utilizzabile come elemento differenziante nel copy.

### Video
- Marco realizzerà 2 teaser da 15-30s con materiale esistente
- Giovanni deve fornire macro linee guida per la ripresa

---

## [2026-06-01] Domanda Elisa su form → risposta Elena

**Fonte**: email Elisa → Elena, 1 giugno 2026

- **Domanda**: il form deve chiedere solo i campi base (screenshot allegato), senza fatturato o stato dell'investimento?
- **Risposta Elena (3 giugno)**: Esatto. Telefono e P.IVA diventano facoltativi.

---

## [2026-06-01] Tracking conversioni — configurazione GA4 (Elisa)

**Fonte**: `inputs/brief-dev-tracking-form.md`

- Creato evento custom `iper_form_submit` in GA4 con filtro su `page_location contains /iperammortamento-2026/`
- Evento marcato come Key event in GA4
- Form compilato con dati di test per generare prima occorrenza
- **Stato al 11 giugno**: evento configurato in GA4, import in Google Ads ancora in sospeso per problema tecnico — Federico ha ricevuto accesso per verificare
- **Stato al 11 giugno (aggiornamento)**: tracking conversione `form_submit` importato in Google Ads da GA4. **Nessun evento registrato** ad oggi — il form non ha ancora generato submit tracciati dopo l'attivazione.

---

## [2026-06-03] Aggiornamento lavori Federico (dev)

**Fonte**: email Federico Lucietto → team, 3 giugno 2026

- **Landing mobile**: lavori completati. Nota: se la visualizzazione non è soddisfacente serve testo più breve per la hero section.
- **Ottimizzazioni performance**: applicate nei limiti del perimetro. Server non in gestione diretta → ulteriori ottimizzazioni non praticabili in questa configurazione.
- **Tracking `form_start`**: evento già predisposto nel form, disponibile per attivazione.
- **Sezione "Quali investimenti possono rientrare"**: aggiornata a formato toggle su mobile (come le FAQ).
- **Slide form eliminata** (seconda slide rimossa).

---

## [2026-06-04] Aggiornamento lavori Elisa

**Fonte**: email Elisa → team, 4 giugno 2026

- **Form Meta aggiornato**: campi ora — ragione sociale, P.IVA (fac.), nome, cognome, telefono, email (fac.), settore di appartenenza
- Link prenotazione call Calendly inserito in coda al form Meta
- **Nuovo form Meta creato** (necessario per le modifiche): nuovo Google Sheet raccolta lead → `https://docs.google.com/spreadsheets/d/1WUa4tSqdxkQLLPj__MQBJ4gJhDPNbDnyP_QKpy-fFEQ/`
- **Keyword Google Ads aggiunte**: *"richiedi perizia"*, *"consulenza iperammortamento"*, *"perizia asseverata"*
- **Geo aggiornato**: aggiunte Emilia-Romagna + Lombardia su Meta e Google Ads; escluse tutte le altre regioni (nota: un lead Meta risultava dalla Sardegna — possibile presenza temporanea in zona target)
- **Tracking Google Ads**: identificato problema tecnico nell'import da GA4 → Federico ha ricevuto accesso per verificare

---

## [2026-06-05] Aggiornamento immagine Federico

**Fonte**: email Federico Lucietto → team, 5 giugno 2026

- Ridotta dimensione immagine hero modificandone la struttura: ora dovrebbe vedersi meglio su mobile.
- **Punto ancora aperto**: immagine hero su mobile — l'unica soluzione praticabile è nasconderla o spostarla sotto. Federico attende indicazioni. → **Decisione richiesta a Elisa/Elena.**

---

## Punti aperti al 11 giugno 2026

| # | Item | Owner | Priorità |
|---|---|---|---|
| 1 | Tracking Google Ads: 0 eventi `form_submit` registrati dopo attivazione — verificare se il form sulla landing genera correttamente l'evento GA4 | Elisa + Federico | **ALTA** |
| 2 | Immagine hero mobile: nascondere o spostare sotto | Elisa / Elena | MEDIA |
| 3 | Numero telefono per sticky CTA e hero | Studio Bognolo | MEDIA |
| 4 | Numero perizie verificato (placeholder "200") | Studio Bognolo | MEDIA |
| 5 | Asset hero image (foto industriale o ritratto Ing. Bognolo) | Studio Bognolo | MEDIA |
| 6 | OK loghi Euronda/Tomasetto/Tintess per uso ATF | Studio Bognolo | MEDIA |
| 7 | Linee guida video per Marco (2 teaser 15-30s) | Giovanni | BASSA |
