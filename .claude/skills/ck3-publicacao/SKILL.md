---
name: ck3-publicacao
description: Publicar uma versão do Cultus Imperialis na main. Use quando o autor pedir para fechar, lançar ou publicar uma versão, ou para mesclar uma branch de trabalho depois do playtest.
---

# Publicar uma versão do Cultus Imperialis

A `main` muda só por PR que o autor mescla. Esta skill prepara a branch e o PR; o merge é do autor.

1. **Branch em dia.** Na branch de trabalho, traga a `main` (`git merge origin/main`) e resolva conflitos.
2. **Decisão de teste comentada.** Os três arquivos (`common/decisions/ci_test_decisions.txt`, `common/scripted_effects/ci_test_effects.txt`, `localization/english/ci_test_l_english.yml`) ficam no repositório com todas as linhas comentadas. Feito quando `python .github/scripts/check_mod.py . --publicacao` sai sem FALHA.
3. **Verificação completa no PC.** Revisão do diff com o agente `ck3-revisor` (que segue a skill `ck3-modding`), `check_imperialis_religion.py` sem FALHA e Tiger com patch 1.20 + `tiger_diff.py` sem diagnóstico novo real contra o relatório-base do `ESTADO`. Na nuvem, diga ao autor que essa etapa fica para o PC dele e não declare a versão validada.
4. **Versão.** Suba `version` no `descriptor.mod` (sem BOM) conforme o autor indicar; sem indicação, pergunte.
5. **Commit e push** da branch, com mensagem "Versão X.Y".
6. **PR para a `main`** com o que entra na versão (as fases da branch) e o resultado das verificações, separando o estático do que o playtest do autor confirmou.
7. **Registro, depois do merge:** atualize o `ESTADO` (seção 1 e "Onde estamos agora") e crie a tag `vX.Y` no commit mesclado quando o autor pedir.

A publicação está pronta para o autor quando o PR tem CI verde, a decisão de teste comentada e a verificação do PC relatada.
