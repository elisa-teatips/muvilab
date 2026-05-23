---
description: Crea un nuovo cliente copiando _template/ in clients/<slug>/
agent: build
---

Crea il nuovo cliente con slug `$ARGUMENTS`.

Prerequisiti (verifica prima):
- `$ARGUMENTS` non vuoto e in formato kebab-case ascii. Se vuoto o malformato → STOP, chiedi.
- `clients/$ARGUMENTS/` NON deve esistere. Se esiste → STOP, segnala.

Procedura:
1. Copia ricorsivamente `_template/` → `clients/$ARGUMENTS/` (preserva struttura).
2. Leggi versione corrente da `CHANGELOG.md` (riga `## [vX.Y.Z]` più recente).
3. Scrivi `clients/$ARGUMENTS/.framework-version` con la versione letta + data odierna.
4. Nei file copiati, sostituisci ogni occorrenza di `<slug>` con `$ARGUMENTS`.
5. Output finale: albero `clients/$ARGUMENTS/` + prossimi step suggeriti (compilare `context/brand.md`, `context/accesses.md`, `context/contracts/contract.md`).

Regole AGENTS.md: opera SOLO su `clients/$ARGUMENTS/` e `_template/` in lettura. Nessun altro cliente.
