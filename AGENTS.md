# Cultus Imperialis

Crusader Kings III mod, prefixo `ci_`. Alvo: 1.20.x (instalado: 1.20.1 Crozier), com a DLC By God Alone obrigatória. Pasta do mod: `C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis`. Descritor do launcher: `...\mod\Imperialis.mod`.

**Leia primeiro:** `C:\Users\rique\Documents\Workspace\Meus Mods CK3\docs\ESTADO - Imperialis.md` (estado do código, branch atual, decisões vigentes, regras de trabalho, ferramentas). Marcos 1 a 6 concluídos; sem marco 7, o foco é desempenho e erros. Checklist ativo: `...\docs\Imperialis - Checklist de playtest marco 6.md`; playtests feitos: `...\docs\Playtests - Imperialis.md`. Lore: Bíblia V7 em `...\Referencia\Biblias`. Não leia por padrão `research_notes`, `reports`, `Referencia` (exceto a Bíblia V7), `DNA` nem `docs\arquivo`: use grep.

Use ck3-modding para script e conteúdo, ck3-gui para interface e ck3-playtest para verificação em jogo. Este arquivo guarda só fatos do projeto.

## Caminhos

| Recurso | Caminho |
|---|---|
| Jogo | `H:\SteamLibrary\steamapps\common\Crusader Kings III` |
| Logs, saves e dumps | `C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\logs` (e `save games`) |
| Workshop (somente leitura) | `H:\SteamLibrary\steamapps\workshop\content\1158310` |
| ck3-tiger com patch 1.20 | `C:\Tools\tiger-src\target\release\ck3-tiger.exe` (usar este; o `C:\Tools\ck3-tiger\ck3-tiger.exe` é o 1.19.0 puro) |
| Docs, bíblias, ferramentas | `C:\Users\rique\Documents\Workspace\Meus Mods CK3` (scripts em `docs\dev`) |

## Convenções

- **Lore:** desde o marco 5, o agente cria lore e textos com base na Bíblia V7 e conta ao autor o que criou. Nomes de personagens não mudam.
- Prefixo `ci_` em arquivos e chaves novas; arquivos antigos com outro prefixo não são renomeados sozinhos. Só chaves de loc exclusivas: nunca `replace` de chaves globais.
- UTF-8 **com BOM** em scripts (`.txt`) e localização (`.yml`); `descriptor.mod` sem BOM. Normalizar CRLF.
- DLC obrigatória, sem fallbacks. Sem compatibilidade com saves antigos; campanha nova a cada teste.
- O mod é independente do LegioImperialis e nunca roda junto com ele.
- Git com remoto `origin` (github.com/Licaesar/Imperialis). A `main` está na versão 1.10 (marcos 1 a 6 e ajustes posteriores). Trabalho novo: branch a partir da `main`, commit por fase, push da branch liberado; a `main` muda só por PR que o autor mescla. A branch em uso e o que falta mesclar estão no ESTADO.
- Mantenha testes e arquivos de desenvolvimento fora da pasta do mod. **Decisão de teste** (`common/decisions/ci_test_decisions.txt`, `common/scripted_effects/ci_test_effects.txt`, `localization/english/ci_test_l_english.yml`): monta o cenário sem cheat; fica **comentada** na `main`. Descomente só para testar e comente de novo antes de mesclar (o verificador avisa enquanto ela estiver ativa).
- Depois de cada atualização do jogo: `docs\dev\vanilla_drift.py` e os geradores `regen_*` (dry-run primeiro).

## Validação e playtest

- Verificação estática própria: `docs\dev\check_imperialis_religion.py` a cada mudança.
- Tiger: `C:\Tools\tiger-src\target\release\ck3-tiger.exe --no-color "<...>\mod\Imperialis.mod" > relatorio.txt`, comparado com `docs\dev\tiger_diff.py` (mostra só o que é novo). Relatório-base atual: `reports\tiger_imperialis_patch120_2026-10-13.txt`. Se o Tiger der "Permission denied", rode de novo (o `tiger_diff.py` recusa relatório vazio).
- Aceitos e fora de escopo: texturas `cat_*` e genes de DNA de mods de heráldica e de genes do autor.
- Ninguém controla o jogo. O autor joga, gera os dumps (`script_docs`, modo debug) e relata; o agente copia o `error.log` antes de tudo (o jogo o sobrescreve ao abrir), lê com `docs\dev\log_errors.py` e `log_mod_blocks.py`, e extrai saves com `docs\dev\extract_save.py`. Resultado estático e resultado em jogo ficam separados nos relatórios.
- Preserve campanhas existentes. Este arquivo não concede permissão para abrir o jogo, mesclar na `main` ou publicar.
