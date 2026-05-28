---
client: bognolo
phase: 04-campaigns
campaign: 2026-iperammortamento
date: 2026-05-28
status: draft
owner: elisa
audience: dev interno Muvi
related: ./audit-roadmap.md
---

# Brief tecnico Fase 0 — Tracking conversioni & Core Web Vitals
## Landing: https://bognolo.it/iperammortamento-2026/

Obiettivo: **abilitare la misurazione delle conversioni** (oggi Google Ads e GA4 sono ciechi: 0 conversioni tracciate su 272 click search e 480 views landing) e **riportare la pagina nei limiti Core Web Vitals** (oggi LCP 5,4s e CLS 1,58 stanno penalizzando Quality Score, bounce e mobile UX).

Setup esistente verificato dal DOM live:
- WordPress + tema Avada (Fusion Builder)
- Form: Fusion Form, route `/fusion_form/form-ammortamento-2026/`
- Facebook Pixel: già installato via plugin **PixelYourSite** (ID `3251089495061859`)
- GTM: installato (confermato dal cliente)
- GA4: presente (vedi report 2026-05-26, 0 key events configurati)
- Google Ads: campagna `Iperammortamento 2026 - Traffic - Search - AI Max`, 0 conversioni tracciate

---

## 1. Conversion tracking — Google Ads + GA4 via GTM

Stack target: **GTM come unico orchestratore**, GA4 come fonte di verità, conversioni Google Ads importate da GA4 (no doppio tracking).

### 1.1 Eventi da tracciare

| Event name (GA4) | Trigger | Categoria | Priorità |
|---|---|---|---|
| `generate_lead` | Submit form Iperammortamento andato a buon fine | conversion primaria | 🔴 must |
| `contact_click_phone` | Click su qualsiasi `a[href^="tel:"]` | conversion secondaria | 🟠 high |
| `contact_click_email` | Click su qualsiasi `a[href^="mailto:"]` | conversion secondaria | 🟠 high |

Solo questi 3. Niente scroll/time-on-page per ora: aggiunta nella Fase 1 quando il setup base è stabile.

### 1.2 Trigger GTM — dettaglio

#### A) `generate_lead` (submit form Fusion)
Fusion Form non emette `gtm.formSubmit` nativo. Due strade:

**Strada consigliata (robusta)**: trigger su **conferma visibile**, non sul submit.
- Trigger type: `Element Visibility`
- Selection method: CSS selector
- Selector: `.fusion-form-confirmation, .fusion-alert-success` (verificare classe esatta del messaggio "Invio completato con successo. Grazie per la tua richiesta.")
- Fire on: Once per page
- Minimum percent visible: 50%

**Strada alternativa**: hook JS sul form. Aggiungere snippet nel `functions.php` del child-theme:

```php
add_action('wp_footer', function () {
  if (!is_page('iperammortamento-2026')) return; ?>
  <script>
    document.addEventListener('fusion-form-submit-success', function(e) {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: 'lead_form_submit',
        form_id: e.detail && e.detail.form_id ? e.detail.form_id : 'iperammortamento_2026',
        form_step: 'final'
      });
    });
  </script>
<?php });
```
> ⚠️ Verificare nome evento JS di Fusion (in alcune versioni è `fusion_form_after_submit` o emesso via jQuery `$(document).trigger`). Se non emette evento, usare Strada A.

#### B) `contact_click_phone` e `contact_click_email`
Trigger GTM `Just Links` con condizioni:
- `Click URL` starts with `tel:` → fire `contact_click_phone`
- `Click URL` starts with `mailto:` → fire `contact_click_email`

### 1.3 Tag GTM — GA4 Event

Per ogni evento dataLayer → un tag GA4 Event:

| Tag | Event name | Parameters |
|---|---|---|
| GA4 — generate_lead | `generate_lead` | `value: 100`, `currency: EUR`, `form_name: iperammortamento_2026` |
| GA4 — contact_phone | `contact_click_phone` | `link_url: {{Click URL}}` |
| GA4 — contact_email | `contact_click_email` | `link_url: {{Click URL}}` |

> `value: 100` è un placeholder per dare un peso economico alla conversione (utile per Maximize Conversion Value in futuro). Lo definiremo meglio col cliente dopo i primi 30 lead.

### 1.4 Configurazione GA4

In GA4 → Admin → **Events** → contrassegnare come **Key Event**:
- `generate_lead` ✅ (primario)
- `contact_click_phone` ✅
- `contact_click_email` ✅

### 1.5 Conversioni Google Ads

**NON** creare conversion tag duplicato in GTM. Procedura:
1. Linkare GA4 ↔ Google Ads (Admin → Product links → Google Ads)
2. In Google Ads → Goals → Conversions → **Import** → GA4 → selezionare `generate_lead` come conv **primaria** + 2 secondarie
3. Attendere 24-48h di dati
4. **Switch campagna** da Maximize Clicks → **Maximize Conversions** (dopo ≥15-20 conv accumulate, altrimenti AI Max non ha segnale sufficiente)

### 1.6 Facebook Pixel — già presente
Verificare che PixelYourSite emetta `Lead` event al submit form (impostazione plugin → Events → Form Triggers → selezionare Fusion Form). Se non lo fa nativamente, aggiungere trigger custom nel plugin con CSS selector del messaggio di successo.

### 1.7 Test & validazione
Prima di pubblicare in GTM:
1. **GTM Preview Mode** sulla landing → simulare submit form, click tel/mailto → verificare che gli eventi dataLayer escano correttamente
2. **GA4 DebugView** → verificare che eventi arrivino con i parameters
3. **Google Tag Assistant** sulla landing in produzione → verificare assenza tag duplicati
4. Test invio reale form da mobile (caso reale: 35% del traffico)

---

## 2. Core Web Vitals — fix LCP e CLS

Dati Clarity 11–26 mag: **LCP 5,4s** (soglia "poor" >4s), **CLS 1,58** (soglia "good" <0,1, "poor" >0,25 → siamo ~16× sopra), INP 170ms (✅ ok).

### 2.1 Diagnosi consigliata
Eseguire **prima** di toccare qualsiasi cosa:
- PageSpeed Insights su URL landing (mobile + desktop)
- Chrome DevTools → Lighthouse + Performance tab → trace di caricamento reale
- Layer di Avada: identificare quali immagini/blocchi causano i layout shift

### 2.2 Ipotesi di lavoro (da validare con audit reale)

#### LCP 5,4s — cause probabili
1. **Hero image non ottimizzata**: la landing carica un bg/hero pesante. Verificare:
   - Formato WebP/AVIF anziché JPG
   - Dimensioni responsive (`srcset`) per mobile vs desktop
   - `<link rel="preload">` per il LCP element nel `<head>`
   - `fetchpriority="high"` sul tag `<img>` LCP
2. **CSS render-blocking di Avada**: defer dei CSS non critical, inline del critical CSS ATF
3. **JS pesanti caricati sincroni**: PixelYourSite, GTM, Facebook Pixel, eventuali plugin Avada. Usare `async`/`defer` o caricamento condizionale
4. **Fonts**: `font-display: swap` su tutti i webfont + preload del font principale

#### CLS 1,58 — cause probabili
1. **Container immagini senza width/height** → al caricamento spingono il contenuto in basso. Aggiungere attributi `width` e `height` o `aspect-ratio` CSS a tutti gli `<img>` ATF
2. **Form Fusion che si rimonta in JS**: il container del form non ha altezza riservata. Aggiungere `min-height` CSS prima del render
3. **Sticky/cookie banner che pushano contenuto**: verificare che cookie banner usi `position: fixed` non `position: relative`
4. **Webfont swap**: combinare `font-display: swap` con `size-adjust` per evitare shift al cambio font

### 2.3 Plugin di supporto (se non già attivi)
- WP Rocket o LiteSpeed Cache (lazy load, defer JS, critical CSS)
- ShortPixel o Imagify (compressione + WebP)
- Asset CleanUp (caricamento condizionale plugin per pagina)

### 2.4 Target post-fix

| Metrica | Attuale | Target |
|---|---|---|
| LCP | 5,4s | <2,5s |
| CLS | 1,58 | <0,1 |
| INP | 170ms | <200ms (✅ già ok) |
| PageSpeed mobile | n.d. | >75 |

---

## 3. Bonus zero-effort — fix dead click (33 sessioni, 7,99%)

Da audit Clarity: 33 sessioni con dead click. Aprire Clarity → Heatmaps → identificare gli elementi su cui gli utenti cliccano "a vuoto". Probabili sospetti:
- Bullet/icone della sezione "Cosa verifichiamo" che sembrano cliccabili ma non lo sono
- Header delle FAQ chiusi (utenti cliccano il titolo aspettandosi espansione → verificare che il toggle funzioni anche su mobile)
- Loghi referenze (Euronda/Tomasetto/Tintess) che sembrano case study cliccabili

Soluzione: o renderli cliccabili (link a una pagina case study) o rimuovere lo stile `cursor: pointer`.

---

## 4. Deliverable richiesti al dev

| # | Output | Formato | Deadline proposta |
|---|---|---|---|
| 1 | Container GTM aggiornato con i 3 trigger + 3 tag GA4 | screenshot config + link versione GTM | T+3 gg |
| 2 | GA4: 3 key events marcati come conversion | screenshot Admin → Events | T+3 gg |
| 3 | Google Ads: import conversion da GA4 | screenshot Goals → Conversions | T+5 gg (dopo 24-48h dati GA4) |
| 4 | Report Lighthouse pre/post fix Web Vitals | PDF/screenshot | T+7 gg |
| 5 | Identificazione dead click da Clarity heatmap | breve nota testuale + screenshot | T+5 gg |

---

## 5. Cosa NON fare in questa fase

- ❌ Non toccare la struttura della landing (form, hero, sezioni) — è Fase 1
- ❌ Non aggiungere eventi scroll/time engagement (rumore, lo facciamo dopo)
- ❌ Non duplicare tag Google Ads conversion in GTM se già importato da GA4
- ❌ Non switchare la bid strategy della campagna prima di avere ≥15-20 conv tracciate

---

## 6. Validazione Elisa post-deploy

Prima di considerare Fase 0 chiusa:
1. Submitto form di test da mobile → verifico in GA4 DebugView l'evento `generate_lead`
2. Aspetto 48h → verifico in Google Ads che la colonna Conversions inizi a popolarsi
3. PageSpeed Insights → confermo LCP <2,5s e CLS <0,1
4. Aggiorno `audit-roadmap.md` con conferma chiusura Fase 0 e green light Fase 1
