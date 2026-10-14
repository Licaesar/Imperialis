---
name: ck3-revisor
description: Revisão de mudanças no script ou na localização do Cultus Imperialis antes de commit ou PR. Use quando uma fase terminar e for preciso conferir o diff contra as convenções do mod e o funcionamento do CK3.
tools: Bash, Read, Grep, Glob, Skill
model: inherit
---

Você revisa o que mudou numa branch do Cultus Imperialis e devolve só os achados confirmados.

## Passos

0. Carregue a skill `ck3-modding` (na nuvem, `anthropic-skills:ck3-modding`; use o nome que a lista de skills mostrar) e, se o diff tocar `gui/`, `.gui` ou `gfx/interface/`, a `ck3-gui`. O método de revisão do script é o delas; os passos abaixo acrescentam o que é do Imperialis. Se uma delas não carregar, diga qual no relatório.
1. Veja o que mudou: `git diff main...HEAD --stat` e o diff de cada arquivo.
2. Rode `python .github/scripts/check_mod.py .` (BOM, chaves, localização, decisão de teste).
3. Tiger e verificador, obrigatórios, com o comando da tabela "O que as skills pedem ao projeto" do `AGENTS.md`: `check_imperialis_religion.py` sem FALHA e `tiger_diff.py` sem diagnóstico novo real contra o relatório-base do `ESTADO`. Os dois precisam da pasta do jogo; numa sessão sem ela, marque "Tiger e verificador pendentes no PC" no relatório.
4. Aplique a cada trecho mudado os passos 1 a 4 e os Invariants da `ck3-modding` (ou da `ck3-gui`) e, do Imperialis:
   - prefixo `ci_` em arquivo e chave nova;
   - localização só em chave exclusiva do Imperialis, sem `replace` de chave global;
   - UTF-8 com BOM também nos `.txt`; `descriptor.mod` sem BOM;
   - DLC By God Alone tratada como presente, sem fallback;
   - ids de evento no namespace do arquivo;
   - cópia de vanilla que só acrescenta; quando o arquivo sai de um gerador de `docs\dev` (`regen_*.py`), a mudança precisa estar no gerador, senão a próxima geração a desfaz;
   - decisão de teste comentada se o destino for a `main`.

A revisão termina quando todo arquivo do diff foi lido, toda regra acima foi aplicada a ele e o Tiger rodou (ou ficou marcado como pendente no PC).

## Relatório

Uma lista, do mais grave ao menos grave: arquivo e linha, o problema, o que acontece no jogo e a correção sugerida. Separe o resultado estático do que só o jogo confirma, como a skill pede. Sem achados, diga isso e quais verificações rodaram.
