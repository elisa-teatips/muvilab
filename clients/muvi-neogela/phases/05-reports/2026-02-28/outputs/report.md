---
client: muvi-neogela
phase: 05-reports
period: 2026-02-28
type: report
status: approved
owner: legacy-migration
last_updated: 2026-05-23
note: migrato da source pre-framework il 2026-05-23
---

# Neogela — Analisi report Google Ads (Campaign + Product + Asset association)
Periodo: 1 Feb 2025 – 11 Feb 2026 (come da export)

## Nota importante sui file
- I CSV in `adv/Neogela-Pu-licità-*` risultano export Meta/Facebook (campi `fb_pixel_purchase`).
- Questa analisi usa i report Google Ads: **Campaign report**, **Product report** e **Asset association report**.
- Nota: l’**Asset association report** è un report di *associazione asset* (Account/Campaign). I costi possono risultare non confrontabili 1:1 con i costi campagna (possibili duplicazioni per livello/associazione). Per spesa/ROAS usare il **Campaign report**.

## 0) Campagne — Campaign report
- Totale account (da Campaign report): Spesa €14.682,96 | Conv. value €218.831,04 | ROAS 14,90 | Conversioni 2.005,17 | CPA €7,32

### Elenco campagne (ordinate per spesa)
| Campagna | Tipo | Stato | Spesa | Conv. value | ROAS | Conv | CPA | Note |
|---|---|---|---:|---:|---:|---:|---:|---|
| IT / Pmax / Conv / Hot&Cold | Performance Max | Enabled | €6.114,97 | €23.845,18 | 3,90 | 234,62 | €26,06 | budget, policy, eligible-limited |
| IT / Search / Conv / Brand | Search | Enabled | €5.609,45 | €174.116,37 | 31,04 | 1.567,64 | €3,58 | budget, eligible-limited |
| IT / Search / Traffico / Cold | Search | Enabled | €2.264,35 | €19.214,40 | 8,49 | 184,05 | €12,30 | budget, eligible-limited |
| IT / Pmax / Conv / Hot | Performance Max | Paused | €694,18 | €1.655,09 | 2,38 | 18,85 | €36,83 | policy |
| IT / Video -visualizzazioni / +35 Cold | Video | Paused | €0,00 | €0,00 | 0,00 | 0,00 | €0,00 | disapproved |

**Insight campagne**
- Miglior ROAS (Enabled): **IT | Search | Conv | Brand** (ROAS 31,04, spesa €5.609,45).
- Peggior ROAS (Enabled): **IT | Pmax | Conv | Hot&Cold** (ROAS 3,90, spesa €6.114,97).

**Problemi ricorrenti (da Campaign report)**
- Campagne con ‘limited by budget’: 3
- Campagne con limitazioni policy negli asset group: 2

**Azioni consigliate (per tipo campagna)**
- Search Brand: aumentare budget finché ROAS/CPA restano efficienti; verificare Impression Share persa per budget/rank; mantenere Brand separato da Non-brand.
- Search Cold: migliorare struttura per intent (ad group tematici), negative su query poco profittevoli; landing dedicate e RSA con value prop + prova sociale.
- PMax: risolvere asset/policy (sitelink/landing ‘health sensitive’), segmentare per linea prodotto/bundle con `custom_label`, e valutare esclusioni brand in PMax per evitare cannibalizzazione del Brand Search.

## 1) Shopping / Merchant Center — Product report
- Spesa totale: €5.053,41 | Click: 16.599 | Impression: 1.953.709
- CTR pesato: 0,85% | CPC medio: €0,30

### Top prodotti per spesa (Top 10)
| Prodotto | Stato | Click | Impr | CTR | CPC | Spesa | Quota spesa |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 Barattolo Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Eligible | 9.541 | 1.033.113 | 0,92% | €0,31 | €3.002,18 | 59,41% |
| 3 Barattoli Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Eligible | 1.560 | 191.252 | 0,82% | €0,34 | €532,40 | 10,54% |
| 6 Barattoli Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Eligible | 1.869 | 199.957 | 0,93% | €0,25 | €459,66 | 9,10% |
| 2 Barattoli Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Eligible | 1.100 | 131.323 | 0,84% | €0,29 | €315,62 | 6,25% |
| 3 Scatole Collagene Neogela - Scatola 28 buste da 5 grammi | Eligible | 343 | 48.896 | 0,70% | €0,46 | €159,19 | 3,15% |
| 6 Scatole Collagene Neogela - Scatola 28 buste da 5 grammi | Eligible | 292 | 45.978 | 0,64% | €0,52 | €152,16 | 3,01% |
| Neogela Collagene barattolo 400g + scatola 28 buste 5g | Eligible | 356 | 55.915 | 0,64% | €0,43 | €151,63 | 3,00% |
| 4 Barattoli Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Eligible | 504 | 67.018 | 0,75% | €0,25 | €127,46 | 2,52% |
| 1 Scatola Collagene Neogela - Scatola 28 buste da 5 grammi | Eligible | 227 | 20.978 | 1,08% | €0,24 | €53,41 | 1,06% |
| 4 Scatole Collagene Neogela - Scatola 28 buste da 5 grammi | Eligible | 110 | 15.412 | 0,71% | €0,27 | €29,45 | 0,58% |

**Insight**
- Spesa molto concentrata sul prodotto #1: **1 Barattolo Collagene Neogela 400g - Ideale per Ossa e Articolazioni** (quota 59,41%).
- Senza `Conversions/Conv. value` non possiamo stimare ROAS o CPA dal Product report.

### Prodotti ‘Not eligible’ con spesa > 0 (storico)
| Prodotto | Issue | Click | Impr | CPC | Spesa |
|---|---|---:|---:|---:|---:|
| 1 Barattolo Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Out of stock | 31 | 4.534 | €0,23 | €7,13 |
| 2 Barattoli Collagene Neogela 400g - Ideale per Ossa e Articolazioni | Out of stock | 5 | 556 | €0,35 | €1,77 |
| 2 Neogela + 12 Buste + Borsa frigo | Out of stock | 10 | 1.155 | €0,07 | €0,65 |
| 3 Neogela + 12 Buste + Borsa frigo | Out of stock | 9 | 1.044 | €0,03 | €0,23 |
| 4 Neogela + 12 Buste + Borsa frigo | Out of stock | 7 | 832 | €0,03 | €0,18 |

**Azioni consigliate (Shopping/PMax)**
- Feed: sincronizzare disponibilità (Shopify → Merchant Center) ed escludere automaticamente prodotti `out_of_stock`.
- Struttura: separare best-seller/high-margin in asset group dedicati per evitare cannibalizzazione del budget.
- Controllo query: affiancare Search Brand (exact/phrase) e Non-brand separata; su PMax usare negative (se disponibili) e segmentazioni per proteggere il brand.

## 2) Asset association report (policy & asset)
- Spesa totale asset: €57,231,19 | Click: 379,694 | Impression: 2,320,422 | Conversioni (da report): 11679,96

### Stati asset (Top)
| Asset type | Status | Count |
|---|---|---:|
| Sitelink | Eligible | 15 |
| Callout | Eligible | 12 |
| Image | Eligible | 9 |
| Business logo | Eligible | 5 |
| Business name | Eligible | 4 |
| Call | Eligible | 4 |
| Image | Not eligible | 4 |
| Price | Eligible | 3 |
| Horizontal logo | Eligible | 2 |
| Logo | Eligible | 2 |
| Logo | Limited | 2 |
| Sitelink | Limited | 1 |

### Asset con più spesa (Top)
| Asset type | Level | Status | Spesa | Click | Conv |
|---|---|---|---:|---:|---:|
| Business logo | Account | Eligible | €7.762,44 | 65.638 | 1730,49 |
| Business name | Campaign | Eligible | €5.582,27 | 15.306 | 1559,64 |
| Business logo | Campaign | Eligible | €5.553,48 | 15.223 | 1550,64 |
| Sitelink | Campaign | Eligible | €3.955,65 | 10.578 | 1049,68 |
| Sitelink | Account | Eligible | €3.183,54 | 34.670 | 516,01 |
| Sitelink | Campaign | Limited | €3.130,45 | 8.715 | 730,47 |
| Sitelink | Account | Eligible | €2.646,15 | 17.396 | 510,88 |
| Sitelink | Account | Eligible | €2.268,01 | 26.037 | 364,83 |
| Business name | Campaign | Eligible | €2.234,62 | 50.945 | 181,85 |
| Business logo | Campaign | Eligible | €2.208,96 | 50.415 | 179,85 |
| Callout | Campaign | Eligible | €1.604,96 | 4.136 | 474,08 |
| Image | Campaign | Eligible | €1.581,45 | 4.648 | 394,86 |

### Asset ‘Limited’ / ‘Disapproved’ (azioni)
- Priorità: sostituire asset disapprovati e mitigare limitazioni policy (soprattutto su targeting personalizzato/remarketing).
| Asset type | Level | Status | Reason | Spesa |
|---|---|---|---|---:|
| Sitelink | Campaign | Limited | Approved (limited) | €3.130,45 |
| Logo | Campaign | Limited | Approved (limited) | €213,14 |
| Logo | Campaign | Limited | Approved (limited) | €0,00 |

**Focus: `HEALTH_IN_PERSONALIZED_ADS`**
- Asset impattati: 1
- Suggerimento: usare sitelink/asset verso pagine più neutre (brand/prodotto/FAQ), evitando riferimenti diretti a patologie quando si usa remarketing.

## 3) Dati aggiuntivi consigliati (per ottimizzazione avanzata)
Per andare oltre la lettura a livello campagna (e capire *perché* spendiamo così) conviene esportare anche:
- Report ‘Search terms’ (o insight PMax) per distinguere Brand vs Non-brand e intercettare query sensibili/mediche che generano CPC alto senza vendite.
- Segmentazione per device/geo/ora (se vendite sensibili a fascia oraria o aree) e impression share per Search.

## 4) Strategie migliorative (priorità)
1) **Protezione Brand**: Search Brand (exact/phrase) con RSA + sitelink neutrali; negative su Non-brand/PMax se cannibalizza.
2) **Struttura PMax per bundle/margine**: asset group separati per Barattolo/Buste/Bundle/Pack e `custom_label` per margine e stock.
3) **Compliance**: rimuovere riferimenti a patologie nei percorsi asset di campagne con segnali personalizzati; usare pagine prodotto/FAQ generiche.
4) **Misurazione**: controllare conversion tracking (Purchase, Enhanced Conversions, Consent Mode) e import del valore ordine reale da Shopify.