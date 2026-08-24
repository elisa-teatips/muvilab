---
client: muvi-neogela
type: process-optimization
status: draft
owner: elisa@teatips.it
last_updated: 2026-07-02
---

# Piano di ottimizzazione — Neogela, 3h/settimana

Analisi della struttura operativa reale di `clients/muvi-neogela/` (fasi, mail, report degli ultimi 9 mesi) per capire dove va il tempo e cosa tagliare, ora che Neogela è l'unico cliente Muvi e il budget è 3h/settimana (~12h/mese).

## Cosa consuma tempo oggi, in ordine di impatto

**1. Il reporting mensile è il collo di bottiglia più grande.** Il ciclo di giugno (`phases/05-reports/2026-06-08/`) mostra oltre 40 CSV scaricati a mano da quattro fonti diverse (Meta Ads, Meta organico IG/FB, TikTok, Google Ads), più un file `.rtfd` e un KPI book. È un lavoro di raccolta ed export manuale che probabilmente assorbe da solo diverse ore per ciclo. In più, la cadenza si è scollata dal mensile previsto dal contratto e dal playbook: gli ultimi report sono usciti il 30 aprile, il 31 maggio e l'8 giugno — quasi ogni due settimane invece che a fine mese — e per lo stesso periodo esistono tre documenti paralleli che raccontano più o meno la stessa cosa (`email-team-report-giugno2026.md`, `recap-call-team-26-06-2026.md`, `Report giugno.rtfd`), oltre al `report.md` standard del framework che in questo ciclo manca del tutto.

**2. L'automazione email è rotta da metà giugno e nessuno se n'è accorto.** Lo script `tools/campaign-reporting/report.py` invia via Gmail un report settimanale Meta, ma il token Meta è scaduto il 15 giugno (`Session has expired on Monday, 15-Jun-26`) e da allora ogni run fallisce silenziosamente — l'ultimo tentativo registrato è del 21 giugno. Google Ads e TikTok, inoltre, non sono mai partiti: le cartelle `imports/neogela/google-ads/` e `imports/neogela/tiktok-ads/` non hanno mai ricevuto i CSV richiesti dal flusso. Un'automazione che si rompe senza avviso e resta ferma per settimane non fa risparmiare tempo, lo costa.

**3. Il PED duplica il lavoro.** Ogni mese esistono sia un `posts.md` consolidato sia singoli file in `posts/` per ogni contenuto (es. febbraio 2026 ha 8 file singoli approvati più un `posts.md` ancora in draft). Di fatto il lavoro reale vive nei file singoli; il consolidato è scritto due volte per lo stesso contenuto.

**4. C'è un arretrato amministrativo di sei mesi.** Da novembre 2025 ad aprile 2026, quasi tutti i `ped.md`, `mail.md` e `results.md` di fase sono fermi su `status: draft`, anche quando i singoli post erano già approvati e pubblicati. Non blocca nulla operativamente, ma tiene il repo in uno stato che non riflette la realtà — e se un giorno serve ricostruire lo storico (es. per il rinnovo contratto), va districato.

**5. Ci sono rivoli a basso ritorno rispetto al budget ADV.** Il budget Meta è €1.500/mese, eppure nel report di giugno emergono diversi fronti aperti dispendiosi in tempo: sblocco del Business Center TikTok, verifica pixel TikTok, correzione feed Google Merchant Center per i multipack, oltre ad analisi extra come `google-ads-analysis.md` e ricerche di trend (`last30days-settore-collagene.md`). Sono tutte cose legittime, ma su un budget di 3h/settimana non c'è spazio per rincorrerle ogni mese.

## Cosa tenere così com'è

La sospensione di LynUp (dal 23/5) ha già dimezzato il perimetro reale: oggi si lavora solo su Neogela, quindi l'overhead di isolamento multi-brand è già sparito. La cadenza mensile di PED + campagne resta corretta e in linea col contratto. La pratica — già emersa da sola nella mail di giugno/luglio — di accorpare in un'unica mail cliente la pianificazione di due mesi insieme (PED+campagne) è buona e va resa la norma, non l'eccezione.

## Cosa tagliare o cambiare

| Area | Azione | Perché |
|---|---|---|
| Reporting | Un solo `report.md` a fine mese, cadenza rigorosamente mensile. Eliminare i doppioni (`email-team-report`, `recap-call-team`, `.rtfd` paralleli) — la mail di reporting prevista dal playbook (5 blocchi) sostituisce già la sintesi interna | Tre versioni dello stesso contenuto = tre volte il tempo |
| Reporting | Report "snello": solo i KPI contrattuali (CPL Meta, ROAS conversione) + una riga per canale. Analisi approfondite (creative-level, demografiche) solo se un KPI è fuori target — è già il meccanismo previsto dal playbook per il "loop strategico" | Il framework stesso dice di non fare deep-dive ogni volta, va solo applicato |
| Automazione | Rigenerare subito il token Meta in `.env` (5 minuti) per far ripartire lo script | È già pagato in setup, oggi non rende nulla |
| Automazione | Portare la frequenza dello script da settimanale a mensile, agganciata al ciclo di report — meno scadenze token da monitorare, un solo output da controllare | Il settimanale non è richiesto da contratto (SLA = mensile) ed è la causa della rottura silenziosa |
| Automazione | Google Ads e TikTok restano manuali: se non c'è tempo per caricare i CSV ogni settimana, non forzarlo — va bene raccoglierli solo al momento del report mensile | Le cartelle import sono vuote da mesi: il flusso automatico lì non sta succedendo comunque |
| PED | Eliminare `posts.md` consolidato, tenere solo i file singoli in `posts/`. `ped.md` diventa un indice leggero (titolo + una riga + link), non un secondo copy | Dimezza la scrittura mensile del piano editoriale |
| Touch-point | Un'unica mail mensile che copre PED + campagne (come già fatto per giugno/luglio) invece di due mail separate | Meno cicli di approvazione da gestire |
| Arretrato | Una singola sessione di pulizia: marcare come `approved`/archiviati i mesi nov'25–apr'26 già pubblicati, poi non tornarci più | Costo una tantum, elimina il rumore permanente |
| Scope | TikTok Ads/Shop (sblocco Business Center, attivazione conversione) resta "fase 2 opzionale" da contratto: segnalarlo al cliente come azione loro, non inseguirlo nel proprio monte ore | Budget TikTok (€500-700, mai attivato) non giustifica il tempo già speso a inseguirlo |
| Scope | Ricerche extra (trend, competitor, Google Ads deep-dive) → cadenza trimestrale, non mensile | Non richieste da contratto con quella frequenza |

## Ritmo settimanale proposto (~12h/mese)

- **Settimana 1** (~4h): pianificazione PED + campagne del mese, mail unica al cliente con validazione
- **Settimana 2** (~2h): monitoraggio leggero, passaggio brief a grafico/video (fuori perimetro, solo brief)
- **Settimana 3** (~2h): check budget/creatività ADV, nessun deep-dive salvo alert KPI
- **Settimana 4** (~3-4h): report mensile snello + mail + prep call di revisione

Non c'è margine per extra: se emerge un fronte nuovo (es. feed Merchant Center, TikTok Business Center), va deciso cosa esce dal ritmo sopra per farci spazio, non aggiunto sopra.

## Prossimi passi concreti

1. Rigenerare il token Meta in `tools/campaign-reporting/.env` e verificare un run pulito
2. Decidere se tenere lo script settimanale o passarlo a mensile (consigliato: mensile)
3. Chiudere in un colpo solo lo stato draft di nov'25–apr'26
4. Da luglio in poi: un solo `report.md` per fine mese, niente doppioni
