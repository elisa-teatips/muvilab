# Neogela — TikTok organico: metriche 30 giugno – 31 luglio 2026

Fonte: TikTok Studio Analytics (tiktok.com/tiktokstudio/analytics), account Neogela, contenuti organici.
Raccolto il 24/08/2026.

## Metriche richieste

| Metrica | Valore |
|---|---|
| Visualizzazioni video | 223.279 (≈223,3K) |
| Visualizzazioni profilo | 717 |
| Pubblico raggiunto (copertura) | 182.043 |
| Follower (variazione netta) | +82 (da 7.137 il 30/6 a 7.219 il 31/7) |
| Mi piace | 979 |
| Commenti | 38 |
| Condivisioni | 150 |
| Click sul link | non disponibile — nessun video del periodo usa la funzione link/CTA |
| Tempo di visualizzazione medio video | non disponibile come aggregato — TikTok Studio lo espone solo per singolo video, non come media di periodo a livello account |

## Metodologia e note

- La tab "Panoramica" di TikTok Studio supporta un range di date personalizzato; da lì sono stati letti direttamente visualizzazioni video, visualizzazioni profilo, mi piace, commenti, condivisioni per il periodo esatto 30/06–31/07/2026.
- Le tab "Spettatori" e "Follower" non supportano un range personalizzato in UI (solo preset 7/28/60/365 giorni). Per ottenerli sul periodo esatto:
  - **Follower**: letto il valore cumulativo dal grafico "Follower totali" nei punti del 30 giugno (7.137) e del 31 luglio (7.219) con vista "Ultimi 60 giorni"; differenza = +82.
  - **Pubblico raggiunto**: recuperato interrogando direttamente l'endpoint dati di TikTok Studio (`aweme/v2/data/insight`, insight `reached_audience_history`, finestra 60 giorni) e sommando i valori giornalieri dal 30/06 al 31/07. I totali di visualizzazioni/mi piace/commenti/condivisioni ottenuti con lo stesso metodo sono stati verificati contro i numeri mostrati in UI e coincidono esattamente, a conferma dell'affidabilità del dato di copertura.
- **Click sul link**: nessun video pubblicato nel periodo ha un link/CTA attivo (l'account non usa questa funzione), quindi la metrica non viene generata da TikTok — non è un limite di raccolta dati.
- **Tempo di visualizzazione medio**: disponibile solo aprendo il dettaglio di ogni singolo video (es. video del 17/08: 1,77s medio), non come aggregato di account per un periodo. Se serve, si può calcolare una media ponderata sui video pubblicati nel periodo aprendo il dettaglio di ciascuno — non ancora fatto.
