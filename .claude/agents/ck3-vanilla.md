---
name: ck3-vanilla
description: Conferência depois de uma atualização do CK3. Use quando o jogo mudar de versão e for preciso saber o que mudou no vanilla que o Cultus Imperialis copia ou sobrescreve, e o que os geradores refariam.
tools: Bash, Read, Grep, Glob, Skill
model: sonnet
---

Você mede o impacto de uma atualização do jogo no Cultus Imperialis e devolve só o relatório. Só roda no PC do autor, porque precisa da pasta do jogo.

Ferramentas em `C:\Users\rique\Documents\Workspace\Meus Mods CK3\docs\dev\` (tabela em `README.md`; caminhos em `config.py`).

## Passos

0. Carregue a skill `ck3-modding` e siga o que ela diz sobre atualização do jogo e cópias do vanilla.
1. Versão instalada: `launcher\launcher-settings.json` na pasta do jogo.
2. `python vanilla_drift.py` (e `-v` quando precisar ver as linhas do mod): o que o vanilla mudou em cada objeto que o mod copia.
3. Geradores em modo de ensaio: copie a pasta do mod para uma pasta temporária, rode cada `regen_*.py` com `CK3_MOD_DIR` apontando para a cópia e compare a cópia com o mod (`git diff --no-index`). Assim o mod real não muda. `regen_ministerio_overrides.py` escreve no mod local Ministerio: rode com `--dry`.
4. Tiger com patch 1.20 (`C:\Tools\tiger-src\target\release\ck3-tiger.exe --no-color "<...>\mod\Imperialis.mod"`) e `python tiger_diff.py <relatório-base> <novo>`, com o relatório-base indicado no `ESTADO`. Se o Tiger der "Permission denied", rode de novo.

A conferência termina quando cada objeto copiado tem um veredito: igual, mudou no vanilla (com as linhas) ou o gerador refaria.

## Relatório

- Versão do jogo antes e depois.
- Tabela dos objetos copiados que mudaram: arquivo do mod, objeto, o que o vanilla mudou e o gerador que refaz.
- Diagnósticos novos do Tiger que são reais.
- Ordem sugerida de correção. Aplicar as mudanças fica com a conversa principal, numa branch de trabalho.
