# Framework agenti — regole globali

Questa repo è il **framework operativo per gestire clienti social**. Contiene:

- `_template/` — scheletro da copiare per ogni nuovo cliente
- `clients/<slug>/` — dati operativi di un cliente specifico
- `.opencode/` — skill, command e subagent OpenCode che automatizzano il flusso
- `tools/`, `playbook.md`, `glossary.md`, `FLOW.md`, `CHANGELOG.md` — risorse trasversali

Documenti di riferimento obbligatori:
- [FLOW.md](./FLOW.md) — flusso end-to-end del cliente tipo
- [playbook.md](./playbook.md) — regole operative (touch-point email, gap-check, MVI, silenzio-assenso)
- [glossary.md](./glossary.md) — definizioni univoche
- [CHANGELOG.md](./CHANGELOG.md) — versioning del template

---

## REGOLE DI ISOLAMENTO CLIENTI — CRITICHE, MAI VIOLARE

> Lavoriamo in mono-repo con più clienti. Una contaminazione fra clienti = danno legale e di fiducia.
> Queste regole valgono per **te, modello LLM**, e per **ogni subagent** che invochi.

1. **SCOPING ESPLICITO**: ogni operazione su un cliente deve dichiarare `<slug>` in input.
   Non esistono default. Comandi senza slug devono fallire o chiedere.

2. **PATH ASSOLUTI AL REPO**: ogni `@file` reference deve includere `clients/<slug>/...` completo.
   Mai usare path relativi che possano risolvere a un altro cliente.

3. **CROSS-CLIENT BAN**: un agente che sta operando su `clients/A` **NON DEVE** leggere,
   scrivere, citare, riassumere o confrontare con `clients/B` (o qualsiasi altro).
   Se serve un benchmark interno, l'utente lo richiede esplicitamente (e oggi non esiste un comando per farlo).

4. **GAP-CHECK FIRST**: prima di produrre output di una fase, esegui o invoca `/gap-check <slug> <fase>`
   che verifica anche che lo slug esista in `clients/`.

5. **NIENTE COPIA INCROCIATA**: vietato suggerire "questo l'abbiamo già fatto per il cliente X".
   Il context cliente è cliente-specifico. Il know-how trasversale vive in `playbook.md` / `_template/`.

6. **SHARED RESOURCES**: solo le seguenti risorse sono trasversali e leggibili da ogni sessione:
   - `tools/`
   - `_template/`
   - `playbook.md`, `glossary.md`, `FLOW.md`, `CHANGELOG.md`, `AGENTS.md`
   - `.opencode/`

7. **SUBAGENT BOUNDARY**: ogni subagent in `.opencode/agents/` deve rifiutare richieste cross-client
   ed esplicitare nello stesso messaggio quale slug sta usando.

8. **AMBIGUITÀ → CHIEDI**: se lo slug non è chiaro, fermati e chiedi. Mai indovinare.

9. **MULTI-SLUG IN UNA RISPOSTA → RIFIUTA**: se ti viene chiesto di operare su due slug diversi
   nello stesso turno, segnala violazione e chiedi di separare in due turni distinti.

10. **SEGRETI**: i file `context/accesses.md` di ogni cliente non devono contenere credenziali in chiaro.
    Solo riferimenti (es. "vedi 1Password vault X").

---

## Convenzioni

- **Slug cliente**: kebab-case, ascii, es. `muvi-neogela`, `acme-spa`
- **Cartella mese**: `YYYY-MM` (es. `2026-06`) per PED e campaigns
- **Cartella report**: `YYYY-MM-DD` (data fine periodo) per reports
- **Frontmatter `.md`** ogni file di output deve avere: `client`, `phase`, `date`, `status` (`draft|in-review|approved`), `owner`
- **Versione template**: ogni cliente ha `.framework-version`; in caso di bump del template aggiornare con consapevolezza

---

## Quando l'utente apre una sessione

1. Identifica il cliente coinvolto (chiedi se non chiaro)
2. Carica la skill `social-framework` per le procedure
3. Leggi `clients/<slug>/AGENTS.md` per il contesto specifico
4. Procedi rispettando le regole sopra

---

## SYNC GIT — OBBLIGATORIO A FINE SESSIONE

Al termine di ogni sessione in cui hai scritto o modificato file in `clients/<slug>/`,
esegui **sempre** questi comandi prima di chiudere:

```bash
git add .
git commit -m "update(<slug>): <descrizione breve delle modifiche>"
git push
```

Regole per il commit message:
- Usa lo slug del cliente nel prefisso: `update(muvi-neogela): ...`
- Descrizione breve ma leggibile (es. `ped 2026-06 approvato`, `strategy 2026 draft`)
- Se la sessione ha toccato solo risorse trasversali (template, playbook, ecc.): `update(framework): ...`

**Non aspettare che l'utente lo chieda. Fallo tu come ultimo atto della sessione.**
