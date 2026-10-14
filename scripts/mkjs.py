import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
old = open(r'C:\Users\DELL\AppData\Local\Temp\old-index.html', encoding='utf-8').read() if pathlib.Path(r'C:\Users\DELL\AppData\Local\Temp\old-index.html').exists() else None
if old is None:
    import subprocess
    old = subprocess.check_output(['git', 'show', '42805f6:index.html'], cwd=root).decode('utf-8')
def blk(a, b):
    return old[old.index(a):old.index(b)]
S = blk('const S=[', 'let cur=0')
E = blk('const E=[', 'let em=0')
P = blk('const P=[', 'let pi=0')
t = (root / 'scripts' / 'df.tpl.js').read_text(encoding='utf-8')
t = t.replace('/*@S*/', S).replace('/*@E*/', E).replace('/*@P*/', P)
(root / 'js' / 'df.js').write_text(t, encoding='utf-8')
print('ok', len(t))
