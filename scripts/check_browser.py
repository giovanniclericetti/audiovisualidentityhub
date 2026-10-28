import os
from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[1]
(root/'verification/audit').mkdir(parents=True,exist_ok=True)
files=[str(f.relative_to(root)) for f in sorted([*root.glob('*.html'),*root.glob('documentazione/*.html'),*root.glob('case-studies/*.html')]) if '<main' in f.read_text() and not f.name.startswith('_')]
results=[];errors=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel=os.environ.get('AIH_BROWSER_CHANNEL','chrome'),headless=True)
 page=browser.new_page(device_scale_factor=1,reduced_motion='reduce')
 page.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8000') else r.abort())
 page.on('pageerror',lambda e:errors.append(str(e)))
 for w in [320,375,390,430,768,1024,1280,1440,1920]:
  page.set_viewport_size({'width':w,'height':900})
  for f in files:
   page.goto('http://127.0.0.1:8000/'+f,wait_until='load');page.evaluate('document.fonts.ready')
   page.locator('img').evaluate_all('(xs)=>xs.forEach(x=>x.loading="eager")')
   page.evaluate('Promise.all([...document.images].map(img => img.decode().catch(() => null)))')
   result=page.evaluate('''()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,
    overflow:[...document.querySelectorAll('main *,footer *,header *')].filter(e=>{const r=e.getBoundingClientRect();return r.width && (r.right>innerWidth+1 || r.left < -1) && !e.closest('.loop-track,.ribbon-track,.study-art,.research-visual') && getComputedStyle(e).position!=='fixed'}).map(e=>({tag:e.tagName,cls:e.className,text:e.textContent.slice(0,70),width:e.getBoundingClientRect().width})).slice(0,12),
    broken:[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.getAttribute('src')),
    hiddenNav:innerWidth<768 && getComputedStyle(document.querySelector('.menu-toggle')).display==='none',
    h1:document.querySelectorAll('h1').length})''')
   results.append({'page':f,**result})
  print('Completed width',w,flush=True)
 browser.close()
(root/'verification/audit/responsive.json').write_text(json.dumps({'results':results,'errors':errors},ensure_ascii=False,indent=2))
fail=[x for x in results if x['scroll']>x['width'] or x['broken'] or x['hiddenNav']]
print('FAILURES',json.dumps(fail,ensure_ascii=False), 'ERRORS',errors,flush=True)

if fail or errors:
 raise SystemExit(1)
