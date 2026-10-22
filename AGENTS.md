# Cultus Imperialis

Mod principal do autor: religião própria (Omnissiae, com as fés Veritas Imperialis e Lex Omnissiah), culturas, Sanguinis e o elenco de Kensoriel. Prefixo `ci_`, alvo 1.20.x, DLC By God Alone obrigatória. Pasta `...\Crusader Kings III\mod\Imperialis`, descritor `...\mod\Imperialis.mod`.

Regras gerais, caminhos do PC, skills e onde registrar cada coisa: `AGENTS.md` da pasta `mod`, um nível acima. Este arquivo guarda só o que é do Imperialis.

**Leia primeiro:** `Meus Mods CK3\docs\ESTADO - Imperialis.md` (versão, branch, o que falta ver no jogo, decisões de design, relatório-base do Tiger). Lore vigente: a Bíblia V7 em `Meus Mods CK3\Referencia\Biblias\`. Playtests feitos: `docs\Playtests - Imperialis.md`.

## Regras do mod

- **Lore (desde o marco 5):** o agente cria lore e textos com base na Bíblia vigente e conta ao autor o que criou. É a exceção à regra geral do `TODO_LORE`. Nomes de personagens não mudam.
- **Localização:** só chaves exclusivas do Imperialis; nunca `replace` de chaves globais, que mudariam o texto também para os cristãos. Termo que muda só no Imperialis ganha chave ou flavorização própria. Os arquivos de localização do autor ficam fora dos commits do agente.
- DLC obrigatória, sem fallbacks. Sem compatibilidade com saves antigos; campanha nova a cada teste.
- O mod é independente do Legio Imperialis e nunca roda junto com ele.
- **Decisão de teste** (`common/decisions/ci_test_decisions.txt`, `common/scripted_effects/ci_test_effects.txt`, `localization/english/ci_test_l_english.yml`): monta o cenário sem cheat (só o jogador, só Imperialis com `sanguini_5`, sem custo: prestígio e piedade no nível 5, 50.000 de ouro e todos os condados do `e_italy`, criando o `e_italy` se faltar) e fica **comentada** na `main`. Descomentar e comentar de novo só a pedido do autor; o verificador avisa enquanto ela estiver ativa.
- **Cópias do vanilla:** listadas em `COPIES` do `docs\dev\vanilla_drift.py` e refeitas pelos geradores do Imperialis (tabela no `docs\dev\README.md`). A cada atualização do jogo, siga o `docs\Guia - Atualização do jogo e DLC.md`, com dry-run dos geradores primeiro.
- O que ficou fora do escopo por decisão do autor está no ESTADO.

## Git

- Remoto `origin` = github.com/Licaesar/Imperialis. Trabalho novo numa branch a partir da `main`, um commit por fase, push da branch liberado; a `main` muda só por PR que o autor mescla, depois do playtest dele. Publicar no Workshop só a pedido.
- A branch remota `claude/project-thread-4y3dpy` (agentes `.claude/`, CI e hook de commit, feitos numa sessão na nuvem) não foi mesclada, por decisão do autor: na `main` não há CI nem hook.

## Validação

- A cada mudança: `docs\dev\check_imperialis_religion.py`. Regra nova do verificador vem com uma mutação que prove que ela pega o erro.
- Tiger com patch 1.20 comparado pelo `tiger_diff.py` com o relatório-base indicado no ESTADO. O Tiger não conhece `faith_types`, `rite_types`, `rite =` e `doctrine_group_type` e acusa falsos positivos nesses pontos.
- Aceitos e fora de escopo: genes de DNA de mods de genes do autor.
- Numa sessão sem a pasta do jogo (nuvem): UTF-8 com BOM em `.txt` e `.yml`, `descriptor.mod` sem BOM; Tiger e verificador ficam pendentes para o PC, e o resultado não é declarado validado.
