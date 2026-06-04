---
client: bognolo
phase: 04-campaigns
campaign: 2026-iperammortamento
date: 2026-06-01
status: draft
owner: Elisa
---

# Brief sviluppatore — Tracking conversione form iperammortamento

## Obiettivo

Registrare come conversione in Google Ads l'invio del form presente sulla landing page:
`https://bognolo.it/iperammortamento-2026/`

Nome evento da usare: **`iper_form_submit`**

---

## Contesto tecnico

- Sulla landing è già installato il Google Tag (verificato)
- L'account Google Ads ha già collegato GA4 (`Bognolo.it - GA4`, ID `373221943`)
- Il Google Tag non risulta ancora collegato direttamente a Google Ads
- **Approccio scelto**: far sparare l'evento tramite GA4, poi importarlo come conversione in Google Ads

---

## Cosa ha già fatto Elisa (nessun intervento dev richiesto per ora)

Il tracking è stato configurato lato GA4 senza modifiche al codice della landing, sfruttando il fatto che GA4 raccoglie già l'evento generico `form_submit` su tutto il dominio.

**Passaggi completati il 2026-06-01:**

1. GA4 → Admin → Data display → **Events → Create event**
   - Nome evento: `iper_form_submit`
   - Condizioni:
     - `event_name` **equals** `form_submit`
     - `page_location` **contains** `/iperammortamento-2026/`
2. Evento marcato come **Key event** in GA4
3. Compilato il form sulla landing con dati di test per generare la prima occorrenza
4. In attesa 24-48h → poi importare in Google Ads come conversione

**Passo successivo (Elisa):**
- Google Ads → Goals → Conversions → Import → Google Analytics 4 → selezionare `iper_form_submit`

---

## Intervento dev: solo se il filtro GA4 non funziona

Se dopo 48h l'evento `iper_form_submit` non risulta importabile in Google Ads, sarà necessario sparare un evento custom direttamente dalla landing. In quel caso il dev dovrà:

1. Identificare il trigger del form:
   - **Caso A** — redirect a thank-you page → tag sul caricamento della thank-you page
   - **Caso B** — messaggio inline → tag sull'evento JS di submit

2. Aggiungere il codice al momento del submit:

**Caso A — su caricamento thank-you page:**
```html
<script>
  gtag('event', 'iper_form_submit', {
    'send_to': 'G-XXXXXXXXXX'  // sostituire con il Measurement ID GA4 di Bognolo.it
  });
</script>
```

**Caso B — su evento submit del form:**
```javascript
document.querySelector('#id-del-form').addEventListener('submit', function() {
  gtag('event', 'iper_form_submit', {
    'send_to': 'G-XXXXXXXXXX'  // sostituire con il Measurement ID GA4 di Bognolo.it
  });
});
```

> Sostituire `#id-del-form` con il selettore reale del form nella pagina.
> Sostituire `G-XXXXXXXXXX` con il Measurement ID GA4 di `Bognolo.it - GA4` (ID account: `373221943`).

---

## Riferimenti

- Landing page: `https://bognolo.it/iperammortamento-2026/`
- GA4 property collegata: `Bognolo.it - GA4` — ID `373221943`
- Google Ads account: verificare con Elisa
