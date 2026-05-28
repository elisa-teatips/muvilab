---
client: bognolo
phase: 04-campaigns
campaign: 2026-iperammortamento
date: 2026-05-28
status: draft
owner: elisa
audience: dev interno Muvi
related: ./audit-roadmap.md, ./brief-dev-fase-0.md
prerequisite: Fase 0 completata (tracking attivo)
---

# Brief implementativo Fase 1 — Quick wins landing Iperammortamento
## Landing: https://bognolo.it/iperammortamento-2026/

Obiettivo: aumentare il **tasso di submit form** dalla baseline stimata <1% al **3-5%**, senza ricostruire la landing.
Metodo di test: **before/after su finestre di 14 giorni comparabili** (no A/B test tool, traffico insufficiente per significatività statistica).

Prerequisito: tracking conversioni attivo (vedi `brief-dev-fase-0.md`). Senza GA4 `generate_lead` funzionante non possiamo misurare l'impatto.

---

## Interventi previsti (4)

| # | Intervento | Effort dev | Impatto atteso |
|---|---|---|---|
| 1 | Sticky CTA bar in alto (telefono + form scroll) | bassa | +30-50% click-to-form |
| 2 | Form corto ATF (4 campi) + multi-step in fondo invariato | media | +100-300% submit rate |
| 3 | Hero rewrite (H1 + bullet + trust badge ATF) | bassa | -quick back, +scroll depth |
| 4 | Fix tecnico LCP/CLS | media | già in Fase 0 (collegato) |

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

### Posizionamento
Subito sotto l'hero, prima della sezione "Step 1-6". Ancora HTML: `#form-short`.
Visivamente: box con sfondo leggermente differenziato (grigio chiaro o colore brand al 5% opacity), padding generoso, no distrazioni laterali.

### Struttura form

**Titolo box**:
> Scopri in 3 giorni se il tuo investimento è agevolabile

**Sottotitolo**:
> Risposta tecnica gratuita di un ingegnere iscritto MIMIT. Nessun impegno.

**Campi (4 in totale)**:

| Campo | Tipo | Obbligatorio | Note |
|---|---|---|---|
| Nome e cognome | text | ✅ | placeholder "Mario Rossi" |
| Azienda | text | ✅ | placeholder "Nome azienda srl" |
| Telefono | tel | ✅ | placeholder "+39 ..." — validazione pattern numerico |
| Tipo investimento | select | ✅ | opzioni: Macchinario / Software / Fotovoltaico / Progetto combinato / Non so ancora |

**Checkbox privacy**: obbligatoria, testo: "Accetto la Privacy Policy e autorizzo il trattamento dei dati per essere ricontattato."

**CTA submit**:
> Richiedi consulenza gratuita

Colore brand Bognolo, full-width su mobile, larghezza naturale desktop.

### Trust elements sotto form
Riga unica orizzontale, font 13px, colore grigio scuro:
> ✓ Risposta entro 3 giorni ・ ✓ Nessun impegno ・ ✓ Iscritto MIMIT & INNOVENETO

### Behavior tecnico
- Submit → stesso endpoint del Fusion Form esistente (riusare configurazione email/CRM)
- Tracking: trigger evento dataLayer `lead_form_submit` con `form_step: 'short'` per distinguerlo dal multi-step (`form_step: 'final'`) → permette di misurare la conversione per variante
- Conferma submit: stesso messaggio "Invio completato con successo" del form attuale
- Errori: validazione inline (HTML5 + custom messaggi italiano)

### Form multi-step in fondo
**Resta invariato**. Non rimuovere. Razionale: utenti più consapevoli/qualificati che scrollano fino in fondo trovano il form di profilazione approfondita. Misureremo la distribuzione short vs final dopo 30 gg.

---

## 3. Hero rewrite (above the fold)

### H1 attuale (da sostituire)
> IPERAMMORTAMENTO 2026-2028: scopri se il tuo investimento è agevolabile e ottieni documentazione tecnica completa e difendibile in caso di verifica.

(28 parole, troppo lungo, è una promessa di valore non un titolo)

### H1 nuovo
> Iperammortamento 2026: la tua perizia asseverata, senza rischi di contestazione.

### H2 / sottotitolo
> Ingegneri industriali iscritti MIMIT. Ti seguiamo dall'analisi di agevolabilità alla comunicazione al GSE, con un unico referente.

### Bullet ATF (3, in quest'ordine)
1. ✓ **Oltre 200 perizie asseverate** completate per imprese del Nord-Est *(⚠️ verificare numero con cliente)*
2. ✓ **Iscritti MIMIT** ed accreditati **INNOVENETO**
3. ✓ Risposta entro **3 giorni lavorativi**, prima consulenza gratuita

### CTA hero
Pulsante primario:
> Richiedi consulenza gratuita →
(Scroll a `#form-short`)

Link secondario sotto pulsante (font più piccolo):
> oppure chiamaci al +39 0444 XXX XXX

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
- **Desktop**: hero split 60/40 (testo a sx, immagine/grafica a dx). H1 e CTA a sinistra, immagine di un macchinario industriale o foto Ing. Bognolo a destra
- **Mobile**: stack verticale — H1 → H2 → bullet → CTA → trust badge → form corto immediatamente sotto

### Asset richiesti
| Asset | Dimensione | Note |
|---|---|---|
| Hero image | min 1920×1080 (desktop), WebP | Da fornire/scegliere: foto industriale o ritratto professionale Ing. Bognolo |
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
- Numero telefono da usare
- Numero "200 perizie completate" (o cifra reale verificata)
- Asset hero image (foto da fornire o scelta da stock)
- Disponibilità loghi clienti per uso ATF (Euronda, Tomasetto, Tintess potrebbero richiedere conferma)
- Copy nuovi (H1 + sottotitolo + bullet + CTA)

> Standard playbook: silenzio-assenso a 48h dall'invio per modifiche non strutturali. Sui numeri/asset legali (cifra perizie, loghi clienti) **serve approvazione esplicita scritta**, no silenzio-assenso.
