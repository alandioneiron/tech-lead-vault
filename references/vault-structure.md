# Vault layout

| EN | PT-BR | Purpose |
|---|---|---|
| `00-Coordination` | `00-Coordenação` | Decision log (ADRs), model routing, dev-to-production flow |
| `01-Planning` | `01-Planejamento` | Vision, roadmap, risks |
| `02-Knowledge` | `02-Conhecimento` | Glossary and reference notes |
| `03-Agents` | `03-Agentes` | Role descriptions (only when roles are enabled) |
| `04-Development` | `04-Desenvolvimento` | Module specs |
| `05-Checklists` | `05-Checklists` | Definition of Done, release checklist, one per task |
| `06-Logs` | `06-Logs` | Journal, changelog, AI session log, handoff |
| `99-Templates` | `99-Templates` | Task, ADR, module spec, daily log |

`Home` at the vault root links to everything. Notes link with `[[wikilinks]]` (no extension; `[[Note|alias]]` for display text). The vault may sit at the repo root or in `docs/`; the scaffold handles both.
