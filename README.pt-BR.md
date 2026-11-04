# tech-lead-vault

Uma skill do Claude Code que faz a IA trabalhar como o **Tech Lead** do seu projeto de software: um **vault do Obsidian é a memória** (conhecimento, decisões, logs, checklists) e o **GitHub é o fluxo de trabalho** (issues, quadro, PRs, releases SemVer).

English version: [README.md](README.md)

## O que faz

- **Instalação guiada** (primeiro uso no projeto): faz até 4 perguntas por vez (projeto, idioma, conta/visibilidade no GitHub, Obsidian, tipo de produção, ambiente dev, quem aprova, comando dos testes, quadro e proteção da `main`, papéis de agentes, versão inicial), mostra o plano e só cria depois do seu OK. Nunca pede nem grava segredos.
- **Monta o vault**: `00-Coordenação` ... `99-Templates`, com `Home`, modelos (tarefa, ADR, especificação de módulo, log diário), Definition of Done, registro de decisões, diário, changelog, log de sessões de IA e o handoff, ligados por `[[wikilinks]]`. Em português (pt-BR) ou inglês.
- **Escreve o `CLAUDE.md` do projeto** com as regras inegociáveis: documentação viva na mesma tarefa, checklist por processo, Definition of Done, toda decisão vira ADR, dev para produção só com o seu OK, handoff no fim de cada sessão, commit e push a cada passo, sem segredos, datas `AAAA-MM-DD`.
- **GitHub como fluxo** (via `gh`, cada passo confirmado): etiquetas, milestones, quadro do Projects (A fazer, Em andamento, Em dev, Esperando OK, Em produção), modelos de issue e de PR, proteção da `main` e um workflow do Actions só com testes. A issue guarda o status; o vault guarda o conhecimento.
- **Releases (SemVer)**: PR `dev` para `main` aprovado = o OK, tag, release em rascunho com as notas do changelog, deploy da tag, conferência, publicar, rollback = tag anterior.
- **Fluxos do dia a dia**: abrir tarefa, registrar decisão, preparar release, fechar a sessão.

## Instalar a skill

Copie a pasta para o diretório de skills:

```bash
git clone <url-deste-repositorio> ~/.claude/skills/tech-lead-vault
```

(Ou copie a pasta do repositório para `~/.claude/skills/tech-lead-vault`, ou use um plugin que empacote skills.) Requisitos: Python 3 para o script de montagem; `gh` (GitHub CLI, logado com `gh auth login`) para os passos do GitHub.

## Exemplo

Na pasta do projeto, diga ao Claude:

> Configure este projeto com o tech-lead-vault.

O Claude faz as perguntas e mostra o plano, algo como:

```
would create 25 files:
  + docs/Home.md
  + docs/00-Coordenação/Registro de Decisões (ADR).md
  ...
  + CLAUDE.md
  + .github/workflows/tests.yml
```

Depois do seu OK ele cria os arquivos e percorre os passos do GitHub um a um. Depois:

> Abra uma tarefa para o endpoint de login. / Registre a decisão de usar PostgreSQL. / Prepare a release v0.2.0. / Feche a sessão.

Também dá para rodar o script direto:

```bash
python scripts/scaffold.py --config minha-config.json --target . --dry-run
```

## Estrutura

```
SKILL.md          instruções principais
references/       questionário, regras, fluxo do GitHub, releases, fluxos, roteamento
scripts/          scaffold.py, gh_setup.sh
assets/en/        notas do vault, CLAUDE.md, arquivos .github (inglês)
assets/pt-BR/     o mesmo em português
```

## Licença

MIT, veja [LICENSE](LICENSE).
