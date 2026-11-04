---
tags: [checklist, release]
---
# Promover para Produção

- [ ] Todo o trabalho da versão integrado em `{{DEV_BRANCH}}`; milestone completo
- [ ] [[Definition of Done]] marcada em cada tarefa
- [ ] [[Changelog]] "Não lançado" lista as mudanças
- [ ] PR `{{DEV_BRANCH}}` para `{{MAIN_BRANCH}}` aprovado pelo dono (este é o OK)
- [ ] Backup feito (se há dados envolvidos)
- [ ] Tag `vX.Y.Z` criada; release em rascunho com as notas do Changelog
- [ ] Deploy da TAG feito
- [ ] Conferência: health check, fluxos principais, logs limpos
- [ ] Release publicada ("Latest" = o que roda em produção)
- [ ] "Não lançado" do Changelog renomeado para a versão e a data
- [ ] Issues movidas para em-produção e fechadas
- [ ] [[Último Agente - Handoff]] atualizado

Rollback: deploy da tag anterior e registro no [[Diário de Desenvolvimento]].
