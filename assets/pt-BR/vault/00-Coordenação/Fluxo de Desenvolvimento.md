---
tags: [coordenacao, processo]
---
# Fluxo de Desenvolvimento (dev para produção)

Como uma mudança sai da ideia e chega à produção.

## Ambientes
| Ambiente | Branch | Notas |
|---|---|---|
| Local / CI | qualquer | testes automáticos, dados fictícios |
<!-- IF:DEVENV -->| Dev | `{{DEV_BRANCH}}` | dados de teste; o dono experimenta a mudança aqui |
<!-- ENDIF:DEVENV -->| Produção ({{PRODUCTION}}) | `{{MAIN_BRANCH}}` | dados reais; só releases com tag |

## O caminho de uma mudança
1. **Pedido** vira uma issue no GitHub (ver [[Template - Tarefa]]) e uma nota de checklist.
2. **Código** numa branch de feature; testes verdes; revisão de segurança quando mexe em permissão, login, envio automático ou entrada externa.
3. **Pull request** para `{{DEV_BRANCH}}`; docs vivas atualizadas; [[Definition of Done]] marcada.
4. **Aprovação** ({{APPROVAL}}): o PR aprovado `{{DEV_BRANCH}}` para `{{MAIN_BRANCH}}` é o OK para ir à produção.
5. **Release**: tag `vX.Y.Z`, release em rascunho com as notas do [[Changelog]], deploy da TAG, conferência com [[Promover para Produção]], publicar a release.
6. **Rollback** = deploy da tag anterior.
7. **Docs**: [[Diário de Desenvolvimento]], [[Changelog]], [[Log de Sessões de IA]], [[Último Agente - Handoff]].

## Regras
- Nada vai à produção sem o OK do usuário. Exceção: hotfix com OK explícito.
- `{{MAIN_BRANCH}}` é a produção; sem commit direto, salvo o merge da promoção e hotfixes.
- Segredos nunca no git. Dados reais nunca no dev.
- O CI só roda testes: sem segredos, sem deploy de produção.
