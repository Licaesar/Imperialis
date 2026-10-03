# Cultus Imperialis

Crusader Kings III mod. Target build: 1.20.x (instalado: 1.20.0.3 Crozier), com a DLC By God Alone obrigatória. Source folder: C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis. Launcher descriptor: C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis.mod. Prefix: ci_.

Use ck3-modding for script and content work, ck3-gui for interface work, and ck3-playtest for runtime verification. These skills provide the reusable workflow. This file holds project-specific facts.

## Machine paths

| Resource | Path |
|---|---|
| Installed game directory | H:\SteamLibrary\steamapps\common\Crusader Kings III |
| CK3 logs | C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\logs |
| Launcher mod directory | C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod |
| Workshop sources, if used | H:\SteamLibrary\steamapps\workshop\content\1158310 (somente leitura) |
| ck3-tiger executable | C:\Tools\ck3-tiger\ck3-tiger.exe (1.19.0; o jogo está na 1.20.0.3) |
| Docs, bíblias e relatórios | C:\Users\rique\Documents\Workspace\Meus Mods CK3 |

## Project conventions

- Design pillars: Kensoriel Liphe (deus encarnado), a linhagem Sanguinis e o culto imperial. Ver a Bíblia mais recente em `Workspace\Meus Mods CK3\Referencia\Biblias`. Não inventar lore: texto novo usa o marcador `TODO_LORE` até o autor elaborar.
- Modelagem religiosa (decisão 03/10/2026): religião `imperialis_religion` com uma única fé `imperialis` e quatro ritos: `imperialis` (principal), `sororitas` (Cultus Undómiel), `omnissiah` e `homus` (Cultus Harmoniae). O `k_sol` (Adeptus Ministorum) é `head_of_rite`, sem `religious_head`.
- Sistemas em mudança e pontos de entrada: `common/religion/` (religion_types, faith_types, rite_types, doctrine_types, doctrine_group_types), `history/faiths/`, `common/customizable_localization/00_liphe_custom_loc.txt`, `common/landed_titles/00_landed_titles_liphe.txt` e `history/characters/ci_founders.txt`.
- Filename and script-key prefix: ci_. Arquivos antigos com outras convenções não são renomeados automaticamente.
- Encoding: UTF-8 com BOM em scripts (.txt) e em localização (.yml), como já está em todos os arquivos do mod e como o jogo exige. O descriptor.mod fica sem BOM.
- Compatibility: a DLC By God Alone é obrigatória (sem fallbacks). Sem compatibilidade com saves anteriores; usar campanha nova. O mod é independente do LegioImperialis e nunca roda junto com ele.
- Shipping folder: C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis. Keep test captures and development files outside it.
- Git: o repositório da pasta do mod já existe. A migração para a 1.20 acontece na branch `migracao-1.20`, com commits locais por fase e sem push sem pedido do autor.

## Validation and playtesting

- Validator command: `C:\Tools\ck3-tiger\ck3-tiger.exe --no-color "C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod\Imperialis.mod"`. O Tiger 1.19.0 avisa que o jogo é mais novo e erra em `rite`, `faith_types`, leis novas e registros da DLC. Esses falsos positivos são esperados; separá-los de erros reais.
- Baseline de referência (03/10/2026, antes da migração, no estado da 1.19): 0 fatal, 297 erros, 176 avisos, 3 untidy. Relatório em `Workspace\Meus Mods CK3\reports\tiger_imperialis_baseline_2026-10-03.txt`.
- Falsos positivos e diagnósticos aceitos fora do escopo do marco 1: texturas `cat_*` dos mods de heráldica do autor, genes dos mods no DNA (`dna_data`), `landless_adventurer_succession_law` (origem Legio), campos de `regeneratio_event.txt` e `sanguini.txt` (Ascensão e Sanguinis, marco posterior).
- Checklist e notas de sessão: `Workspace\Meus Mods CK3\docs`.
- Campanha de teste separada, com save base nomeado: criar antes do primeiro playtest do marco 1; nunca testar em campanha existente.
- Ferramentas de controle do jogo: nenhuma autorizada. O autor abre o jogo, gera os dumps `script_docs` e executa os checklists; o agente lê os logs frescos.
- Correções aguardando recarga: nenhuma.

Preserve existing campaigns. Read fresh logs after reproduction. Keep static validation and runtime results separate. This file grants no additional permission to launch, operate, commit, or publish.
