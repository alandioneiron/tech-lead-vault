# CLAUDE.md - Regras operacionais do projeto "{{PROJECT_NAME}}"

> Lido automaticamente por toda sessão de IA neste diretório. Estas regras têm prioridade sobre o comportamento padrão.

## O que é este projeto
{{PROJECT_SUMMARY}}

A documentação fica num vault do Obsidian (`{{VAULT_DIR}}`), ligada por `[[wikilinks]]`. Comece pela [[Home]].
<!-- IF:ROLES -->
## Papéis e modelos (roteamento obrigatório)
- **Tech Lead** (modelo mais capaz): planejamento, arquitetura, decisões, tarefas ambíguas/críticas/de segurança, revisão final. Coordena com o usuário.
- **Devs / QA** (modelos mais baratos): implementação e testes de tarefas bem definidas.
- Antes de delegar, escolha o modelo de menor custo capaz de fazer bem, seguindo o [[Roteamento de Modelos]]. Se delegar custar ~o mesmo que fazer, o Tech Lead faz.
<!-- ENDIF:ROLES -->
## Regras INEGOCIÁVEIS de processo

1. **Documentação viva.** Sempre que escrever, editar ou testar código ou configuração, atualize os documentos afetados na MESMA tarefa, antes de considerá-la concluída: [[Diário de Desenvolvimento]], [[Changelog]] (se mudou comportamento), a especificação do módulo em `04-Desenvolvimento/`, a [[Arquitetura]] se afetada, e uma linha no [[Log de Sessões de IA]]. Se um contexto relevante não tem doc, crie e ligue.
2. **Checklists.** Todo processo segue um checklist em `05-Checklists/`. Marque `[x]` cada item assim que concluí-lo, não em lote. Sem checklist, crie um a partir do [[Template - Tarefa]] antes.
3. **Definition of Done.** Nada é "concluído" sem passar pela [[Definition of Done]].
4. **Decisões.** Toda decisão de arquitetura/tecnologia vira um ADR no [[Registro de Decisões (ADR)]], com o [[Template - ADR]].
5. **Dev para produção.** Toda mudança passa pelo fluxo de dev e só vai à produção depois do OK do usuário (o PR aprovado para `{{MAIN_BRANCH}}`); depois, deploy da tag. Hotfix só com OK explícito. Ver [[Fluxo de Desenvolvimento]] e [[Promover para Produção]].
6. **Handoff.** No fim de toda sessão, reescreva o [[Último Agente - Handoff]]: o que está em produção, em andamento, esperando o usuário e os próximos passos.
7. **Commit e push a cada progresso** (junto da documentação viva). Commits só de docs adicionam apenas os docs.
8. **Nunca commitar segredos** (chaves, tokens, credenciais, `.env`). O `.gitignore` deve protegê-los.
9. **Datas** sempre em `AAAA-MM-DD`.

## O GitHub é o fluxo de trabalho
A issue guarda o STATUS; o vault guarda o CONHECIMENTO. Ligue cada issue à sua nota de checklist/spec e vice-versa. As versões seguem SemVer (começando em {{VERSION}}); ver [[Fluxo de Desenvolvimento]].

## Ponto de partida de qualquer sessão
1. Ler a [[Home]] e o [[Último Agente - Handoff]].
2. Ler o [[Roteiro]] e o checklist da fase atual.
3. Ao terminar, aplicar as regras 1-6.

## Convenções
- Idioma da documentação: PT-BR.
- Links entre notas: `[[Nome da Nota]]` (sem extensão).
- Riscos recorrentes nunca somem; ver [[Riscos]].
