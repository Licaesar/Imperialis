# Cultus Imperialis

Crusader Kings III mod, prefixo `ci_`. Alvo: 1.20.x (instalado: 1.20.0.3 Crozier), com a DLC By God Alone obrigatória. Pasta do mod: `C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis`. Descritor do launcher: `...\mod\Imperialis.mod`.

**Leia primeiro:** `C:\Users\rique\Documents\Workspace\Meus Mods CK3\docs\ESTADO - Imperialis.md` (estado do código, decisões vigentes, plano do marco 2, ferramentas). Depois o checklist ativo `...\docs\Imperialis - Checklist de playtest marco 2.md`. Lore: Bíblia V4 em `...\Referencia\Biblias`. Não leia por padrão `research_notes`, `reports`, `Referencia` (exceto a Bíblia V4) nem `DNA`: use grep.

Use ck3-modding para script e conteúdo, ck3-gui para interface e ck3-playtest para verificação em jogo. Este arquivo guarda só fatos do projeto.

## Caminhos

| Recurso | Caminho |
|---|---|
| Jogo | `H:\SteamLibrary\steamapps\common\Crusader Kings III` |
| Logs, saves e dumps | `C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\logs` (e `save games`) |
| Workshop (somente leitura) | `H:\SteamLibrary\steamapps\workshop\content\1158310` |
| ck3-tiger | `C:\Tools\ck3-tiger\ck3-tiger.exe` (1.19.0; o jogo é mais novo) |
| Docs, bíblias, ferramentas | `C:\Users\rique\Documents\Workspace\Meus Mods CK3` (scripts em `docs\dev`) |

## Convenções

- **Não inventar lore.** Texto novo usa `TODO_LORE`; o autor elabora depois. Nomes de personagens não mudam.
- Prefixo `ci_` em arquivos e chaves novas; arquivos antigos com outro prefixo não são renomeados sozinhos.
- UTF-8 **com BOM** em scripts (`.txt`) e localização (`.yml`); `descriptor.mod` sem BOM.
- DLC obrigatória, sem fallbacks. Sem compatibilidade com saves antigos; campanha nova a cada teste.
- O mod é independente do LegioImperialis e nunca roda junto com ele.
- Git local sem remoto: commit por fase na branch de trabalho (hoje `marco-2`), sem push sem o autor pedir. Mantenha testes e arquivos de desenvolvimento fora da pasta do mod.

## Validação e playtest

- O Tiger 1.19.0 não conhece `faith_types`, `rite_types`, `rite =`, `doctrine_group_type` etc. e gera falsos positivos esperados. Use `docs\dev\check_imperialis_religion.py` (verificação estática própria) e `docs\dev\tiger_diff.py` (só o que é novo). Baseline do Tiger: `reports\tiger_imperialis_baseline_2026-10-03.txt`.
- Aceitos e fora de escopo: texturas `cat_*` e genes de DNA de mods de heráldica e de genes do autor; `regeneratio` (Ascensão, será refeita na fase c do marco 2).
- Ninguém controla o jogo. O autor joga, gera os dumps (`script_docs`, modo debug) e relata; o agente lê logs frescos (`docs\dev\log_errors.py`) e saves (`docs\dev\extract_save.py`). Resultado estático e resultado em jogo ficam separados nos relatórios.
- Preserve campanhas existentes. Este arquivo não concede permissão para abrir o jogo, comitar com push ou publicar.
