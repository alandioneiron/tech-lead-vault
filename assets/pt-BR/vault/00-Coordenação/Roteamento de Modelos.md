---
tags: [coordenacao, custo]
requires: roles
---
# Roteamento de Modelos

Gastar o mínimo de tokens sem perder qualidade. O Tech Lead decide quem faz o quê.

Pontue a tarefa de 1 (baixo) a 3 (alto) em: **ambiguidade**, **amplitude de contexto**, **risco** (segurança, dados pessoais, dinheiro, difícil de reverter).

| Soma | Quem |
|---|---|
| 3-4 | modelo pequeno/rápido: trabalho mecânico, renomear, stubs, atualizar logs e checklists |
| 5-6 | modelo médio: implementar algo bem especificado, escrever testes, corrigir bug com repro claro |
| 7-9 | Tech Lead: arquitetura, segurança, trabalho ambíguo ou crítico, revisão final |

**Regra de break-even:** se explicar e revisar o que o delegado fez custa ~o mesmo que fazer, o Tech Lead faz.

Registre quem fez o quê no [[Log de Sessões de IA]]. Ver [[Tech Lead]].
