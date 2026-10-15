"""Hook PreToolUse do Claude Code: valida o mod antes de cada `git commit`.

Sempre: .github/scripts/check_mod.py (BOM, chaves, localização, decisão de teste).
No PC, com a pasta do jogo: check_imperialis_religion.py e o Tiger comparado por tiger_diff.py
contra o relatório-base. Sem a pasta do jogo (nuvem), avisa que a validação ficou pendente.
Bloqueia o commit (exit 2) quando algo falha. Commits só de .claude/, .github/ ou .md passam direto.

Caminhos (variáveis de ambiente, com os do PC do autor como padrão):
  CK3_WORKSPACE    pasta Meus Mods CK3
  CK3_TIGER        ck3-tiger.exe com o patch 1.20
  CK3_TIGER_BASE   relatório-base do Tiger, relativo ao workspace ou absoluto
  CK3_GAME_ROOT, CK3_MODS_DIR  lidos pelo config.py do workspace
"""
import json, os, re, subprocess, sys, tempfile

WORKSPACE = os.environ.get('CK3_WORKSPACE', r'C:\Users\rique\Documents\Workspace\Meus Mods CK3')
TIGER = os.environ.get('CK3_TIGER', r'C:\Tools\tiger-src\target\release\ck3-tiger.exe')
TIGER_BASE = os.environ.get('CK3_TIGER_BASE', os.path.join('reports', 'tiger_imperialis_patch120_2026-10-13.txt'))
GAME_ROOT = os.environ.get('CK3_GAME_ROOT', r'H:\SteamLibrary\steamapps\common\Crusader Kings III')
MODS = os.environ.get('CK3_MODS_DIR', r'C:\Users\rique\Documents\Paradox Interactive\Crusader Kings III\mod')


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', **kw)


def bloquear(msg):
    sys.stderr.write(msg.strip() + '\n')
    sys.exit(2)


def contexto(msg):
    print(json.dumps({'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'additionalContext': msg}}, ensure_ascii=False))
    sys.exit(0)


def arquivos_do_mod(repo):
    st = run(['git', '-C', repo, 'status', '--porcelain', '-uall']).stdout
    nomes = [linha[3:].split(' -> ')[-1].strip('"') for linha in st.splitlines() if len(linha) > 3]
    return [n for n in nomes if not n.startswith(('.claude/', '.github/')) and not n.endswith('.md')]


def main():
    try:
        dados = json.load(sys.stdin)
    except ValueError:
        return
    cmd = dados.get('tool_input', {}).get('command', '')
    if not re.search(r'\bgit\b[^|;&\n]*\bcommit\b', cmd):
        return
    repo = os.environ.get('CLAUDE_PROJECT_DIR') or dados.get('cwd') or os.getcwd()
    if not arquivos_do_mod(repo):
        return

    py = sys.executable or 'python'
    r = run([py, os.path.join(repo, '.github', 'scripts', 'check_mod.py'), repo])
    if r.returncode != 0:
        bloquear('check_mod.py reprovou o commit:\n' + (r.stdout + r.stderr)[-3000:])

    dev = os.path.join(WORKSPACE, 'docs', 'dev')
    if not (os.path.isdir(os.path.join(GAME_ROOT, 'game')) and os.path.isdir(dev)):
        contexto('check_mod.py OK. Verificador e Tiger NÃO rodaram (sem a pasta do jogo ou do workspace nesta máquina). '
                 'Escreva no PR "Tiger e verificador pendentes no PC" e não declare o resultado validado.')

    env = dict(os.environ, CK3_MOD_DIR=repo)
    r = run([py, os.path.join(dev, 'check_imperialis_religion.py')], env=env, cwd=dev)
    if r.returncode != 0:
        falhas = '\n'.join(l for l in r.stdout.splitlines() if l.startswith('FALHA'))
        bloquear('check_imperialis_religion.py reprovou o commit:\n' + (falhas or r.stdout[-3000:] + r.stderr[-1000:]))

    if not os.path.isfile(TIGER):
        contexto(f'check_mod.py e verificador OK. Tiger NÃO rodou: {TIGER} não existe. Rode o Tiger antes do PR.')
    descritor = os.path.join(MODS, 'Imperialis.mod')
    base = TIGER_BASE if os.path.isabs(TIGER_BASE) else os.path.join(WORKSPACE, TIGER_BASE)
    aviso = ''
    if os.path.normcase(os.path.realpath(repo)) != os.path.normcase(os.path.realpath(os.path.join(MODS, 'Imperialis'))):
        aviso = f' Atenção: o Tiger leu {descritor}, que aponta para a pasta do mod, não para {repo}.'
    with tempfile.TemporaryDirectory() as tmp:
        novo = os.path.join(tmp, 'tiger.txt')
        for _ in range(2):  # o Tiger às vezes sai com "Permission denied"; uma nova tentativa resolve
            r = run([TIGER, '--no-color', descritor])
            with open(novo, 'w', encoding='utf-8') as f:
                f.write(r.stdout)
            if r.stdout.count('\n') > 10:
                break
        d = run([py, os.path.join(dev, 'tiger_diff.py'), base, novo], cwd=dev)
    m = re.search(r'novos diagnosticos distintos:\s*(\d+)', d.stdout)
    if not m:
        bloquear('tiger_diff.py não conseguiu comparar os relatórios:\n' + (d.stdout + d.stderr)[-3000:])
    if int(m.group(1)) > 0:
        bloquear(f'Tiger com {m.group(1)} diagnóstico(s) novo(s) contra {base}:\n' + d.stdout[-4000:] + aviso)
    contexto(f'check_mod.py OK, verificador OK, Tiger 0 diagnóstico novo contra {os.path.basename(base)}.{aviso}')


if __name__ == '__main__':
    main()
