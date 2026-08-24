# Google Ads — import settimanale Neogela

Ogni lunedì mattina prima delle 8:00 esporta da Google Ads e salva qui i CSV.

## Come esportare

Per ciascuno dei 4 report, vai su Google Ads → sezione corrispondente → Download (icona ↓) → CSV.

Nomina i file così (sostituisci le date):

| Report | Nome file |
|---|---|
| Campagne | `campaigns_2026-06-08_2026-06-14.csv` |
| Gruppi di annunci | `adgroups_2026-06-08_2026-06-14.csv` |
| Asset | `assets_2026-06-08_2026-06-14.csv` |
| Keyword | `keywords_2026-06-08_2026-06-14.csv` |

## Colonne necessarie (selezionale nell'export)

**Campagne:** Campaign, Campaign status, Budget, Cost, Impressions, Clicks, CTR, Avg. CPC, Conversions, Conv. value, Search impr. share

**Gruppi di annunci:** Campaign, Ad group, Ad group status, Cost, Impressions, Clicks, CTR, Avg. CPC, Conversions

**Asset:** Campaign, Ad group, Asset, Asset type, Performance label, Impressions, Clicks, CTR

**Keyword:** Campaign, Ad group, Keyword, Match type, Cost, Impressions, Clicks, CTR, Avg. CPC, Conversions, Quality Score
