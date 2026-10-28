import os
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[1]
(root/'verification/audit').mkdir(parents=True,exist_ok=True)
files=[str(f.relative_to(root)) for f in sorted([*root.glob('*.html'),*root.glob('documentazione/*.html'),*root.glob('case-studies/*.html')]) if '<main' in f.read_text() and not f.name.startswith('_')]
results=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel=os.environ.get('AIH_BROWSER_CHANNEL','chrome'),headless=True)
 page=b.new_page(reduced_motion='reduce')
 page.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8000') else r.abort())
 for width in [390,1440]:
  page.set_viewport_size({'width':width,'height':900})
  for f in files:
   page.goto('http://127.0.0.1:8000/'+f);page.evaluate('document.fonts.ready')
   page.add_script_tag(path=os.environ['AIH_AXE_SCRIPT'])
   r=page.evaluate('''async()=>{const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}});return r.violations.map(v=>({id:v.id,impact:v.impact,help:v.help,nodes:v.nodes.map(n=>({target:n.target,summary:n.failureSummary}))}))}''')
   results.append({'file':f,'width':width,'violations':r})
  print('Axe completed',width,flush=True)
 b.close()
(root/'verification/audit/accessibility.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
from collections import Counter
print(dict(Counter(v['id'] for r in results for v in r['violations'])),flush=True)
