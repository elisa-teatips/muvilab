---
client: bognolo
phase: 05-reports
period: 2026-05-26
status: draft
owner: elisa
last_updated: 2026-05-26
---

# Nota operativa — Asset alternativi per ridurre il quick back sulla landing iperammortamento

**Contesto**: il report 2026-05-26 segnala un 2,42% di quick back (10 sessioni) sulla landing `/iperammortamento-2026/`, con scorrimento medio al 28,6%. Il dato suggerisce un disallineamento tra le aspettative create dagli annunci e il contenuto trovato sulla pagina, probabilmente su query informative (es. "iperammortamento 2026 quali beni", "come funziona", "simulazione") dove l'utente non è ancora in fase di richiesta contatto.

---

## 1. Callout da aggiungere (livello account o campagna)

| Testo | Razionale |
|---|---|
| `Oltre 200 perizie completate` | Prova sociale — riduce il rimbalzo per chi è in fase di valutazione del fornitore |
| `Valutazione gratuita del bene` | Promessa concreta che risponde a "vale il mio macchinario?" prima ancora di cliccare |
| `Accreditato INNOVENETO` | Differenziatore credenziale specifico per il Nord-Est, rafforza fiducia |
| `Consulenza senza impegno` | Abbassa la frizione per chi non è ancora in fase decisionale |

---

## 2. Sitelink da aggiungere

| Titolo | URL target | Razionale |
|---|---|---|
| `Beni ammissibili 4.0` | `/iperammortamento-2026/#beni` oppure nuova pagina FAQ | Intercetta la query "iperammortamento 2026 quali beni" (69 imp. nel search term report) — l'utente arriva su una sezione pertinente invece che sul form |
| `Come funziona la perizia` | `/perizie-tecniche/` (già esistente) | Risponde alle query "come funziona" portando su una pagina esplicativa, non di conversione — riduce rimbalzo per utenti in fase educativa |
| `Simulazione investimento` | `/iperammortamento-2026/#simulazione` | Intercetta "simulazione iperammortamento 2026" (104 imp.) — richiede creazione di un anchor o sezione dedicata sulla landing |

**Nota**: il sitelink "Come funziona la perizia" è zero-effort (URL già esistente) — priorità massima.

---

## 3. Structured snippet da sostituire

**Attuale** — header generico, irrilevante per la campagna iperammortamento:
> `Servizi: Consulenze marcatura CE, Prototipazione prodotti, Perizie Tecniche` (CTR 2,27%)

**Proposta** — allineato all'intenzione di ricerca:
> Header: `Beni ammissibili` — Valori: `Macchinari industriali, Impianti produttivi, Sistemi automatizzati`

Alternativa:
> Header: `Settori` — Valori: `Manifatturiero, Alimentare, Meccanica di precisione`

---

## 4. Ordine di priorità interventi

1. **Aggiungere callout** "Valutazione gratuita del bene" e "Consulenza senza impegno" → immediato, nessuna modifica al sito
2. **Aggiungere sitelink** "Come funziona la perizia" → `/perizie-tecniche/` già esistente, zero effort
3. **Sostituire structured snippet** con versione "Beni ammissibili" → immediato
4. **Aggiungere callout** "Oltre 200 perizie completate" e "Accreditato INNOVENETO" → verificare i numeri con il cliente prima di pubblicare
5. **Sitelink "Beni ammissibili 4.0"** e **"Simulazione investimento"** → richiedono aggiornamento della landing page, da pianificare con il cliente

---

## 5. Note per il cliente

- I callout con numeri ("Oltre 200 perizie") devono essere verificati e approvati prima della pubblicazione.
- Il sitelink "Simulazione investimento" è efficace solo se sulla landing viene aggiunta una sezione con simulazione o calcolatore (anche semplice).
- Tutti gli interventi 1-3 sono attivabili entro 24 ore senza modifiche al sito.
