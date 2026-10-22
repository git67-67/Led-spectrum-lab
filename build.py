#!/usr/bin/env python3
"""Build the single-file app: python3 build.py  ->  dist/led-spectrum-lab.html and docs/index.html (GitHub Pages)."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_URL = os.environ.get('LSL_REPO_URL', 'https://github.com/YOUR-USER/led-spectrum-lab')   # <- set your repository URL
VERSION = '1.0.0'
r = lambda p: open(os.path.join(ROOT, p), encoding='utf-8').read()
js = ';\n'.join(r('src/' + f) for f in ['data.js', 'core.js', 'ui1.js', 'ui2.js', 'ui3.js', 'ui4.js']).replace('</script', '<\\/script')
html = r('src/index.template.html').replace('__REPO__', REPO_URL)
meta = json.dumps({'repo': REPO_URL, 'version': VERSION, 'license': 'AGPL-3.0-or-later'})
for key, val in (('/*META*/', meta), ('/*CSS*/', r('src/style.css')), ('/*JS*/', js)):
    assert key in html
    html = html.replace(key, '\0', 1).replace('\0', val, 1)
for out in ('dist/led-spectrum-lab.html', 'docs/index.html'):
    os.makedirs(os.path.join(ROOT, os.path.dirname(out)), exist_ok=True)
    open(os.path.join(ROOT, out), 'w', encoding='utf-8').write(html)
print('built', len(html), 'bytes')
