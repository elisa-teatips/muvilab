# Framework template changelog

Versioning del template `_template/`. Ogni cliente memorizza la versione adottata in `clients/<slug>/.framework-version`.

## v1.0 — 2026-05-23

Prima release.

- Struttura cliente-centrica `clients/<slug>/`
- 5 fasi: presales, strategy, ped, campaigns, reports
- Ogni fase con `inputs/` (`_scratch.md`, `feedbacks.md`) e `outputs/` (artefatto, `mail.md`, `TODO.md`)
- Frontmatter obbligatorio su ogni `.md` di output
- 5 subagent specializzati: strategist, ped-creator, campaign-planner, reporter, mail-drafter
- 7 comandi OpenCode: new-client, new-month, start-phase, gap-check, send-mail, status, migrate
- Skill `social-framework` per istruzioni on-demand
- Regole di isolamento cliente in `AGENTS.md`
