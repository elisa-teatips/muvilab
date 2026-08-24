---
client: muvi-neogela
phase: 04-campaigns
period: 2026-06
type: analysis
status: draft
owner: elisa-moratello
last_updated: 2026-06-11
source: "Export Google Ads 11 mag–11 giu 2026 (inputs/Campaign report.csv, Ad group report.csv, Asset groups report.csv, Ad report.csv)"
---

# Analisi Google Ads — Neogela — 11 mag–11 giu 2026

## Quadro generale

**Spesa totale: €1.387,30 | Conv. value: €15.949 | ROAS: 11,5x | CPA medio: €8,98**

Il numero di superficie è buono, ma è gonfiato dalla Brand Search che da sola genera l'84% del conv. value (€13.361 su €15.949) con il 40% della spesa. Tolto il brand, il resto dell'account ha un ROAS di circa **4,6x** e un CPA di **€27**.

---

## Analisi per campagna

### Brand Search — `IT | Search | Conv | Brand`
**ROAS 24x | CPA €4,44 | CTR 18,4% | Conv. rate 8,1%**

Performa molto bene. Il budget €26/giorno non è in limited status, ma con un CTR del 18% e un conv. rate dell'8% è probabile che stia perdendo impression share per budget.

**Problemi:**
- L'ad group dinamico (`B-Search - gruppo di annunci dinamici`) è in pausa — corretto, i DSA brand tendono a cannibalizzare senza controllo
- ROAS target impostato al **2800%** — troppo alto, frena Google dall'allocare impression su aste che avrebbero comunque convertito bene ma sotto quella soglia

**Azioni:**
- Controllare Impression Share (Search IS) e Search Lost IS (Budget) — se perde più del 20% per budget, aumentare il giornaliero da €26 a €35–40
- Abbassare il Target ROAS a **1500–2000%** per allargare la copertura senza sacrificare efficienza
- Valutare ad group separato per keyword di navigazione (es. "neogela shop", "neogela acquisto") con bid manuale o tCPA basso

---

### Pmax — `IT | Pmax | Conv | Hot&Cold`
**ROAS 3x | CPA €28 | Conv. rate 0,48% | Status: Limited (policy + budget)**

Campagna con più margine di miglioramento.

**Problemi strutturali:**
1. **Asset disapprovati**: 4 immagini Not eligible bloccano impression su display/discovery. Con integratori alimentari Google è severo: immagini che evocano "prima/dopo", dolore fisico esplicito o claim terapeutici vengono bocciate sistematicamente.
2. **Budget €18/giorno insufficiente per Pmax**: Google ha bisogno di dati per il machine learning. Con €18/giorno e CPA ~€28, la campagna fa al massimo 0,6 conversioni/giorno — troppo poche per stabilizzarsi. Servono minimo 30–50 conv/mese per asset group.
3. **Asset group "Interessi" a 0 conversioni**: 2.769 impression, 595 interazioni, 0 conv. — segnale audience troppo freddo o creatività non adatte al segmento.
4. **Target ROAS potenzialmente troppo alto**: la campagna è in "Maximize Conversion Value (Target ROAS)" — se il target è eccessivo blocca le aste come per la Brand.

**Azioni:**
- **Immediato**: rimuovere tutti gli asset con status "Not eligible / Disapproved" e sostituirli con immagini lifestyle (persone attive, niente focus su dolore o osso)
- **Immediato**: sospendere l'asset group "Interessi" (0 conv.) e concentrare budget sui due gruppi che convertono
- **Budget**: portare a €25–30/giorno
- **Customer Match**: aggiungere la lista clienti Klaviyo come segnale audience — è il segnale più potente disponibile per Pmax
- **URL expansion**: verificare che sia limitata a pagine prodotto e shop, non al blog — altrimenti Pmax porta traffico informativo che non converte

---

### Search Traffico Cold — `IT | Search | Traffico | Cold`
**ROAS 3,2x | CPA €25 | CTR 16,2% | Conv. rate 0,17%**

Il problema non è la campagna: CTR 16% su keyword fredde è ottimo, gli annunci sono pertinenti. Il problema è la landing.

La landing è il blog osteoporosi (rimedi naturali). Chi cerca "cure osteoporosi" o "alternativa bifosfonati" è in fase informativa, non di acquisto. Il funnel attuale:

```
keyword informativa → blog post → uscita
```

Conv. rate 0,17% = 1 utente su 600 converte. Coerente con bounce rate ~90% rilevato nel report maggio.

**Azioni:**
- **Aggiungere CTA lead gen nel blog**: pop-up o banner "Scarica la guida gratuita" con form Klaviyo — trasforma traffico informativo in lead invece di perderlo
- **Landing dedicata**: testare una pagina specifica per il traffico Google con headline che aggancia la keyword + CTA diretta al prodotto o alla consulenza gratuita
- **Segmentare per intento**: separare keyword informative (es. "osteoporosi rimedi naturali") da keyword transazionali (es. "collagene per ossa acquisto") in ad group distinti con landing diverse
- **Rivalutare l'obiettivo**: se la campagna porta traffico freddo, misurarla su CPL (lead) anziché ROAS

---

## Problemi trasversali

### Merchant Center — 4 prodotti non approvati
Problema strutturale: il prezzo delle confezioni multiple con sconto quantità su Shopify non coincide con il prezzo nel feed Google. Finché non allineato, quei 4 prodotti non escono su Shopping né su Pmax. Non urgente ma va sistemato perché Pmax usa il catalogo come segnale.

### Qualità tracciamento conversioni
Il report mostra "Conv. value" ma non specifica se sono conversioni GA4 o Shopify. Con bounce rate ~90%, è possibile che ci siano micro-conversioni (scroll, visite pagina) conteggiate come conversioni. Verificare che le azioni tracciate siano solo acquisti reali o invii form.

### Budget Google vs contratto
Il contratto definisce €1.500/mese su Meta. Il budget Google (~€1.387 nel periodo) non ha un cap contrattuale definito. Vale la pena formalizzare la ripartizione con il cliente.

---

## Priorità interventi

| Priorità | Azione | Impatto | Effort |
|----------|--------|---------|--------|
| 🔴 Alta | Rimuovere asset Pmax disapprovati (4 immagini) | Sblocca impression Pmax | Basso |
| 🔴 Alta | Aggiungere Customer Match Klaviyo come segnale Pmax | Migliora targeting Pmax | Basso |
| 🔴 Alta | Abbassare Target ROAS Brand da 2800% a 1500% | Più copertura a parità di efficienza | Basso |
| 🟡 Media | Aggiungere CTA lead gen nel blog (landing Search Traffico) | Converte traffico informativo in lead | Medio |
| 🟡 Media | Sospendere asset group "Interessi" Pmax (0 conv.) | Concentra budget dove funziona | Basso |
| 🟡 Media | Verificare IS Budget Brand Search (aumentare a €35–40/gg se perde >20%) | Più volume su campagna top performer | Basso |
| 🟢 Bassa | Allineare prezzi Shopify/Google Merchant per 4 prodotti | Sblocca prodotti su Pmax/Shopping | Alto |
| 🟢 Bassa | Verificare qualità tracciamento conversioni | Dati più affidabili | Medio |
