---
client: bognolo
phase: 04-campaigns
campaign: 2026-iperammortamento
date: 2026-05-28
status: in-review
owner: elisa
audience: dev interno Muvi
related: ./audit-roadmap.md, ./brief-dev-fase-0.md
prerequisite: Fase 0 completata (tracking attivo)
last_updated: 2026-06-11
---

# Brief implementativo Fase 1 — Quick wins landing Iperammortamento
## Landing: https://bognolo.it/iperammortamento-2026/

Obiettivo: aumentare il **tasso di submit form** dalla baseline stimata <1% al **3-5%**, senza ricostruire la landing.
Metodo di test: **before/after su finestre di 14 giorni comparabili** (no A/B test tool, traffico insufficiente per significatività statistica).

Prerequisito: tracking conversioni attivo (vedi `brief-dev-fase-0.md`). Senza GA4 `generate_lead` funzionante non possiamo misurare l'impatto.

---

## Interventi previsti (4)

| # | Intervento | Effort dev | Impatto atteso | Stato al 11 giu |
|---|---|---|---|---|
| 1 | Sticky CTA bar in alto (telefono + form scroll) | bassa | +30-50% click-to-form | **da fare** |
| 2 | Form corto ATF (4 campi) + multi-step in fondo invariato | media | +100-300% submit rate | **parzialmente fatto** — vedi §2 aggiornato |
| 3 | Hero rewrite (H1 + bullet + trust badge ATF) | bassa | -quick back, +scroll depth | **parzialmente fatto** — mobile completato, testo hero da aggiornare |
| 4 | Fix tecnico LCP/CLS | media | già in Fase 0 (collegato) | **parzialmente fatto** — CLS risolto, LCP ancora critico |

> ⚠️ Pubblicare **tutti gli interventi insieme** in unica deploy, non incrementali. La misurazione before/after richiede una finestra netta di confronto.

---

## 1. Sticky CTA bar

### Comportamento
Barra orizzontale fissa in alto, visibile a partire dallo scroll di 100px (per non sovrapporsi al menu Avada in stato iniziale). Sempre visibile dopo, anche su mobile.

### Contenuto desktop
```
[Logo piccolo] | Iperammortamento 2026 — consulenza gratuita in 3 giorni | 📞 0444 XXX XXX  [Compila il form →]
```

### Contenuto mobile (< 768px)
```
📞 Chiama ora    |    Compila il form →
```
Due CTA affiancate al 50% di larghezza, altezza 56px, font 14-15px, fondo bianco con ombra sottile.

### Specifiche tecniche
- `position: fixed; top: 0; z-index: 9999;`
- Background: `#FFFFFF` con `box-shadow: 0 2px 8px rgba(0,0,0,0.08)`
- CTA primaria (form): background colore brand Bognolo, testo bianco
- Telefono: `<a href="tel:+39XXXXXXXXXX">` (recuperare numero da cliente — placeholder finché non confermato)
- CTA form: anchor `<a href="#form-short">` che porta al form corto ATF (vedi sezione 2)
- Su mobile: sostituire il telefono cliccabile con icona + label "Chiama"

### Numero di telefono
**⚠️ Da richiedere al cliente** prima del deploy. Verificare con Studio Bognolo se vogliono:
- Numero fisso studio (orario ufficio)
- Numero mobile referente
- Numero dedicato campagna (consigliato per tracking call-tracking futuro)

---

## 2. Form corto ATF

> **⚠️ AGGIORNAMENTO 4-5 giugno 2026** — Le decisioni su form e Meta sono state allineate in una catena email interna (vedi `inputs/feedbacks.md`). Le specifiche qui sotto riflettono quanto concordato e già parzialmente implementato da Elisa (form Meta) e Federico (landing).

### Posizionamento
Subito sotto l'hero, prima della sezione "Step 1-6". Ancora HTML: `#form-short`.
Visivamente: box con sfondo leggermente differenziato (grigio chiaro o colore brand al 5% opacity), padding generoso, no distrazioni laterali.

### Struttura form — **AGGIORNATA**

**Titolo box** (aggiornato rispetto alla prima versione):
> Compila il form e verrai ricontattato entro 3 giorni lavorativi.

*(Il titolo originale "Scopri in 3 giorni se il tuo investimento è agevolabile" è stato sostituito con questa dicitura più diretta su indicazione del cliente — Elena, 29 maggio 2026)*

**Campi (aggiornati) — landing page**:

| Campo | Tipo | Obbligatorio | Note |
|---|---|---|---|
| Ragione Sociale | text | ✅ | placeholder "Nome azienda srl" |
| P.IVA | text | ⬜ facoltativo | |
| Nome e Cognome | text | ✅ | placeholder "Mario Rossi" |
| Email | email | ✅ | |
| Telefono | tel | ⬜ facoltativo | placeholder "+39 ..." |

> **Nota**: rispetto al brief originale (4 campi: nome, azienda, telefono, tipo investimento) la struttura è stata riallineata a quanto implementato su Meta (29 maggio) e confermata da Elena il 3 giugno. P.IVA e Telefono sono facoltativi. Il campo "Tipo investimento" è stato rimosso dalla prima slide.

**Seconda slide**: **ELIMINATA** (confermato da Federico il 5 giugno).

**Checkbox privacy**: obbligatoria, testo: "Accetto la Privacy Policy e autorizzo il trattamento dei dati per essere ricontattato."

**CTA submit**:
> Richiedi consulenza gratuita

**Aggiunta link prenotazione call** (dopo il submit o come alternativa):
Link Google Calendar: `https://calendar.app.google/UApLCnj6vwcp22ZTA`
*(Inserito già nel form Meta da Elisa il 4 giugno — da portare anche nella landing)*

### Trust elements sotto form
Riga unica orizzontale, font 13px, colore grigio scuro:
> ✓ Risposta entro 3 giorni ・ ✓ Nessun impegno ・ ✓ Iscritto MIMIT & INNOVENETO

### Behavior tecnico
- Submit → endpoint Fusion Form esistente (configurazione email/CRM invariata)
- Tracking: evento `iper_form_submit` configurato in GA4 il 2026-06-01 (vedi `inputs/brief-dev-tracking-form.md`). Evento `form_start` già predisposto lato form da Federico.
- **Stato tracking al 11 giugno**: GA4 key event configurato; import in Google Ads ancora in sospeso per un problema tecnico identificato — Federico ha ricevuto accesso per verificare.
- Conferma submit: messaggio "Invio completato con successo"
- Errori: validazione inline (HTML5 + messaggi in italiano)

### Form Meta — **già aggiornato da Elisa (4 giugno)**
- Campi: ragione sociale, P.IVA (fac.), nome, cognome, telefono, email (fac.), settore di appartenenza
- Link prenotazione call Calendly/Google Calendar aggiunto in coda
- Nuovo Google Sheet per raccolta lead: `https://docs.google.com/spreadsheets/d/1WUa4tSqdxkQLLPj__MQBJ4gJhDPNbDnyP_QKpy-fFEQ/`
- Form Meta: **nuovo form creato** (necessario per le modifiche) — il vecchio form non è più attivo

---

## 3. Hero rewrite (above the fold)

> **⚠️ AGGIORNAMENTO 3-5 giugno 2026** — Federico ha completato i lavori lato mobile (confermato 3 giugno). Rimane aperta la questione dell'immagine hero su mobile (vedi sotto).

### H1 attuale (da sostituire)
> IPERAMMORTAMENTO 2026-2028: scopri se il tuo investimento è agevolabile e ottieni documentazione tecnica completa e difendibile in caso di verifica.

*(Federico ha segnalato che i testi attuali sono troppo lunghi per la hero section su mobile — serve versione più corta)*

### H1 nuovo
> Iperammortamento 2026: la tua perizia asseverata, senza rischi di contestazione.

### H2 / sottotitolo
> Ingegneri industriali iscritti MIMIT. Ti seguiamo dall'analisi di agevolabilità alla comunicazione al GSE, con un unico referente.

### Bullet ATF (3, in quest'ordine)
1. ✓ **Oltre 200 perizie asseverate** completate per imprese del Nord-Est *(⚠️ verificare numero con cliente — non ancora confermato)*
2. ✓ **Iscritti MIMIT** ed accreditati **INNOVENETO**
3. ✓ Risposta entro **3 giorni lavorativi**, prima consulenza gratuita

> **Nota Federico (3 giugno)**: il "3 giorni" compare già nella prima slide e nell'ultima — ha valutato la ripetizione eccessiva e non ha modificato il titolo. Allineare con Elena se mantenere o variare la dicitura in uno dei due punti.

### CTA hero
Pulsante primario:
> Richiedi consulenza gratuita →
(Scroll a `#form-short`)

Link secondario sotto pulsante (font più piccolo):
> oppure chiamaci al +39 0444 XXX XXX

### Immagine hero mobile — **PUNTO APERTO**

Federico (5 giugno): *"L'unico fix per l'immagine per come è posizionata è nasconderla/spostarla sotto da mobile (se la spostiamo sotto tanto vale nasconderla). Aspetto indicazioni."*

**Decisione richiesta a Elisa/Elena**: nascondere l'immagine hero su mobile (`display: none` sotto breakpoint 768px) o spostarla sotto il form corto. Raccomandazione: **nasconderla** — su mobile la priorità è H1 → bullet → CTA → form, l'immagine aggiunge peso senza valore percepito immediato.

### Trust badge ATF
Sotto i bullet, riga orizzontale con loghi reali (in grayscale o colore tenue):
- Logo Euronda
- Logo Tomasetto Achille
- Logo Tintess
- Eventuale badge "MIMIT" (se esiste asset grafico)
- Eventuale badge "INNOVENETO"

Caption sopra i loghi (font 12px, colore grigio):
> Hanno scelto Studio Bognolo:

### Layout suggerito
- **Desktop**: hero split 60/40 (testo a sx, immagine/grafica a dx). H1 e CTA a sinistra, immagine a destra
- **Mobile**: stack verticale — H1 → H2 → bullet → CTA → (immagine nascosta o sotto form)

### Asset richiesti
| Asset | Dimensione | Note |
|---|---|---|
| Hero image | min 1920×1080 (desktop), WebP | Da fornire/scegliere: foto industriale o ritratto professionale Ing. Bognolo — **non ancora confermata** |
| Logo Euronda/Tomasetto/Tintess | PNG trasparente | già presenti in `context/brand-assets/` — verificare risoluzione |
| Badge MIMIT | SVG/PNG | da reperire o ricreare |
| Badge INNOVENETO | SVG/PNG | da reperire o ricreare |

---

## 4. Fix tecnico Core Web Vitals

Vedi `brief-dev-fase-0.md` sezione 2. **Deve essere chiuso prima o contestualmente** a Fase 1: pubblicare nuovi elementi su una pagina con LCP 5,4s vanifica i miglioramenti UX.

Validazione finale Fase 1 = PageSpeed mobile ≥75 + LCP <2,5s + CLS <0,1.

---

## 5. Cosa NON tocchiamo in Fase 1

- ❌ Struttura sezioni "Step 1-6", "Cosa verifichiamo", FAQ, "Quali investimenti rientrano", "I sei punti critici", "Perché Studio Bognolo", "Casi di riferimento" → restano identiche
- ❌ Form multi-step in fondo → resta identico, non rimuovere
- ❌ Menu di navigazione Avada
- ❌ Footer

Tutto questo è materiale di Fase 4 (landing v2 vera e propria), dopo aver imparato dai dati Fase 1-3.

---

## 6. Misurazione before/after

### Periodo before
**11–25 maggio 2026** (15 giorni, dati già nel report)
- Sessioni landing: 361 (Clarity)
- Lead Google: 0 tracciati (era pre-tracking)
- Lead Meta: 3 (form nativo, non landing)
- Click "Contattaci": 5 (1,38%)

### Periodo after (post-deploy Fase 1)
14 giorni consecutivi a partire dal deploy completo. Stessi giorni della settimana per evitare bias settimanale (es. lun→dom × 2).

### KPI da confrontare

| Metrica | Source | Target after |
|---|---|---|
| Sessioni landing | GA4 | parità o superiore (no perdita traffico) |
| `generate_lead` count | GA4 (Fase 0 attivo) | ≥8-15 in 14gg |
| Form submit rate | `generate_lead` / sessioni | 3-5% (vs <1% baseline) |
| `contact_click_phone` | GA4 | ≥10 (vs 0 misurati prima) |
| Distribuzione short vs final | parametro `form_step` | output informativo, no target |
| Scroll depth media | Clarity | >50% (vs 28,6%) |
| Quick back rate | Clarity | <1% (vs 2,42%) |
| LCP / CLS | PageSpeed | <2,5s / <0,1 |

### Report
A 14 gg dal deploy: genero un mini-report comparativo `clients/bognolo/phases/04-campaigns/2026-iperammortamento/outputs/report-fase-1.md` con verdict per ogni KPI (PASS/FAIL) e raccomandazione su Fase 2 (split ad group Google).

---

## 7. Deliverable richiesti al dev

| # | Output | Formato | Deadline proposta |
|---|---|---|---|
| 1 | Sticky CTA bar deployata + responsive testata | URL preview/staging | T+3 gg |
| 2 | Form corto ATF funzionante + Fusion Form backend integrato + tracking dataLayer | URL preview + screenshot evento GA4 DebugView | T+5 gg |
| 3 | Hero rewrite con nuovo copy + asset image | URL preview | T+5 gg |
| 4 | Fix CWV completato | report Lighthouse pre/post | T+7 gg |
| 5 | Deploy production di tutti gli interventi (single batch) | URL produzione + checklist test | T+8 gg |

---

## 8. Checklist test pre-deploy (su staging)

- [ ] Submit form corto da desktop → arriva email + evento `generate_lead` in GA4 DebugView
- [ ] Submit form corto da mobile → idem
- [ ] Click numero telefono mobile → apre dialer + evento `contact_click_phone`
- [ ] Sticky bar visibile su scroll >100px, non sovrapposta a menu
- [ ] Sticky bar responsive su 320px / 375px / 768px / 1024px / 1920px
- [ ] Hero responsive: H1 leggibile, bullet allineati, CTA tap-target ≥44px su mobile
- [ ] Form multi-step in fondo continua a funzionare invariato (regressione)
- [ ] PageSpeed mobile ≥75 confermato
- [ ] No errori console JS
- [ ] Privacy policy linkata correttamente

---

## 9. Approvazione cliente pre-deploy

Prima di pubblicare in produzione servono OK da Studio Bognolo su:
- Numero telefono da usare (**ancora aperto**)
- Numero "200 perizie completate" o cifra reale verificata (**ancora aperto**)
- Asset hero image (**ancora aperto**)
- Disponibilità loghi clienti per uso ATF (**ancora aperto**)
- Copy nuovi (H1 + sottotitolo + bullet + CTA)
- **Decisione immagine hero mobile**: nascondere o spostare sotto (attende indicazione Elisa/Elena)

> Standard playbook: silenzio-assenso a 48h dall'invio per modifiche non strutturali. Sui numeri/asset legali (cifra perizie, loghi clienti) **serve approvazione esplicita scritta**, no silenzio-assenso.
