# Cultus Imperialis

Mod de Crusader Kings III, prefixo `ci_`, alvo 1.20.x com a DLC By God Alone obrigatória.

**Leia primeiro:** `Meus Mods CK3\docs\ESTADO - Imperialis.md`, a fonte do estado atual (versão, branch em andamento, checklist ativo, Bíblia vigente). Este arquivo guarda só o que não muda de semana para semana. Material de consulta (`Referencia`, `reports`, `DNA`, bíblias antigas) se lê com grep, por trecho.

## Skills e Tiger em todo trabalho de mod

| Trabalho | Obrigatório |
|---|---|
| Script, eventos, decisões, localização, histórico | skill `ck3-modding` |
| Interface (`gui/`, `.gui`, `gfx/interface/`) | skill `ck3-gui` |
| Playtest, logs, saves, verificação em jogo | skill `ck3-playtest` |
| Qualquer mudança no mod, antes do commit | Tiger com patch 1.20 + `tiger_diff.py` contra o relatório-base do `ESTADO`, e `check_imperialis_religion.py` |

As skills trazem o método geral e ficam no perfil do autor, no PC e na nuvem (lá aparecem como `anthropic-skills:ck3-modding` e assim por diante; use o nome que a lista de skills da sessão mostrar). Este arquivo traz só o que é do Imperialis. O Tiger e o verificador precisam da pasta do jogo e rodam no PC: numa sessão na nuvem, rode-os por Remote Control no PC do autor quando ele permitir; sem essa rodada, escreva no PR "Tiger e verificador pendentes no PC" e não declare o resultado validado.

O que as skills pedem ao projeto:

| A skill pede | No Imperialis |
|---|---|
| Caminhos do jogo, logs, Workshop e Tiger | tabela Caminhos, abaixo |
| Configuração do Tiger | sem arquivo próprio: `ck3-tiger.exe --no-color "<...>\mod\Imperialis.mod" > novo.txt`, depois `tiger_diff.py <relatório-base do ESTADO> novo.txt`; falsos positivos conhecidos em Validação |
| Dump `script_docs` fresco | o autor gera em modo debug; fica em `logs\` |
| Cenário, ferramentas e autorização de playtest | decisão de teste (Convenções); scripts de `docs\dev` (tabela no `README.md` dessa pasta); abrir o jogo só a pedido do autor |
| Formato do registro de playtest | tabela no topo de `docs\Playtests - Imperialis.md`, com os status da `ck3-playtest` (`NOT RUN`, `PASS`, `FAIL`, `BLOCKED`, `SUPERSEDED`) |

## Agentes e skills do repositório

Delegue aos agentes de `.claude/agents/` o trabalho que lê muito e devolve pouco; eles rodam em contexto próprio e só o relatório volta.

| Agente | Quando |
|---|---|
| `ck3-triagem` | O autor trouxe `error.log`, save ou CSVs de desempenho |
| `ck3-lore` | A tarefa precisa de nome, fato ou decisão de lore antes de escrever texto |
| `ck3-revisor` | Uma fase terminou e o diff vai para commit ou PR |
| `ck3-vanilla` | O jogo mudou de versão (precisa da pasta do jogo: PC ou Remote Control) |

Skill `ck3-publicacao` (`.claude/skills/`): fechar uma versão e preparar o PR para a `main`.

## Onde registrar cada coisa

| O quê | Onde |
|---|---|
| Fato estável do mod (caminho, convenção, regra) | este `AGENTS.md` |
| Estado atual, pendências, decisões de design | `docs\ESTADO - Imperialis.md` (curto: o que acabou sai) |
| Resultado de playtest | topo de `docs\Playtests - Imperialis.md`; no `ESTADO` fica só o que falta ver |
| Lore | Bíblia vigente em `Referencia\Biblias\`; versão nova manda a anterior para `arquivo\` |
| Fase ou marco concluído | `docs\arquivo\`, com o checklist dele |
| Saves extraídos, logs copiados | pasta temporária fora do workspace, apagada depois da análise |

## Caminhos

| Recurso | Caminho |
|---|---|
| Mod (este repositório) | `C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis`, descritor `...\mod\Imperialis.mod` |
| Jogo | `H:\SteamLibrary\steamapps\common\Crusader Kings III` |
| Logs, saves e dumps | `C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\logs` (e `save games`) |
| Workshop (somente leitura) | `H:\SteamLibrary\steamapps\workshop\content\1158310` |
| Tiger com patch 1.20 | `C:\Tools\tiger-src\target\release\ck3-tiger.exe` |
| Docs, bíblias, ferramentas | `C:\Users\rique\Documents\Workspace\Meus Mods CK3` (scripts em `docs\dev`); repositório privado `Licaesar/Meus-Mods-CK3`, clonado também nas sessões na nuvem |

## Convenções

- Lore: crio textos com base na Bíblia vigente e conto ao autor o que criei. Nomes de personagens ficam como estão.
- Prefixo `ci_` em arquivos e chaves novas; arquivos antigos com outro prefixo mantêm o nome.
- Localização: só chaves exclusivas do Imperialis. Para mudar um termo só no Imperialis, crie chave ou flavorização própria e deixe as chaves globais do vanilla intactas.
- UTF-8 **com BOM** em `.txt` e `.yml`; `descriptor.mod` sem BOM.
- DLC obrigatória, sem fallbacks. Campanha nova a cada teste, sem compatibilidade com saves antigos.
- O mod é independente do Legio Imperialis e nunca roda junto com ele.
- Testes e arquivos de desenvolvimento ficam fora da pasta do mod.
- **Decisão de teste** (`common/decisions/ci_test_decisions.txt`, `common/scripted_effects/ci_test_effects.txt`, `localization/english/ci_test_l_english.yml`): monta o cenário sem cheat e fica comentada inteira na `main`. O CI reprova PR para a `main` com ela ativa.

## Git

- Remoto `origin` = github.com/Licaesar/Imperialis.
- Trabalho novo numa branch a partir da `main`, um commit por fase.
- Push da branch de trabalho liberado (decisão do autor, 14/10/2026): ao fechar uma fase, envie a branch.
- A `main` muda só por PR que o autor mescla, depois do playtest dele.

## Validação

- **CI** (`.github/workflows/check.yml`, em todo push e PR): `.github/scripts/check_mod.py` confere BOM, chaves `{ }`, cabeçalho e chaves repetidas da localização e a decisão de teste. Roda sem a pasta do jogo; local: `python .github/scripts/check_mod.py . [--publicacao]`.
- **No PC, a cada mudança:** `docs\dev\check_imperialis_religion.py` (referências cruzadas contra o vanilla instalado) e o Tiger comparado com `docs\dev\tiger_diff.py` contra o relatório-base indicado no `ESTADO`. O Tiger não conhece `faith_types`, `rite_types`, `rite =` e `doctrine_group_type`, e acusa falsos positivos nesses pontos.
- Aceitos e fora de escopo: genes de DNA de mods de genes do autor.
- O autor joga, gera os dumps (`script_docs`, modo debug) e relata; o agente lê logs frescos e saves com os scripts de `docs\dev`. Relatórios separam resultado estático de resultado em jogo.
- Preserve campanhas e playsets existentes. Abrir o jogo ou publicar no Workshop exige pedido do autor.
