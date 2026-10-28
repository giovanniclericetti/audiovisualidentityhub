import os
import sys,json
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
(root/'verification/audit').mkdir(parents=True,exist_ok=True)
phase=sys.argv[1]
paths=[str(f.relative_to(root)) for f in sorted([*root.glob('*.html'),*root.glob('documentazione/*.html'),*root.glob('case-studies/*.html')]) if '<main' in f.read_text() and not f.name.startswith('_')]
with sync_playwright() as p:
 browser=p.chromium.launch(channel=os.environ.get('AIH_BROWSER_CHANNEL','chrome'),headless=True)
 page=browser.new_page(device_scale_factor=1,reduced_motion='reduce')
 page.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8000') else r.abort())
 for width in [390,768,1440]:
  page.set_viewport_size({'width':width,'height':900})
  for path in paths:
   page.goto('http://127.0.0.1:8000/'+path);page.evaluate('document.fonts.ready');page.locator('img').evaluate_all('(xs)=>xs.forEach(x=>x.loading="eager")');page.evaluate('Promise.all([...document.images].map(img => img.decode().catch(() => null)))')
   dest=root/'verification/audit'/phase;dest.mkdir(parents=True,exist_ok=True)
   page.screenshot(path=str(dest/(path.replace('/','-')+f'-{width}.png')),full_page=True)
   if path in ['index.html','documentazione/2.3.html','documentazione/3.4.html']:
    for position in ['middle','bottom']:
     page.evaluate('window.scrollTo(0, document.documentElement.scrollHeight '+('/2' if position=='middle' else '')+')')
     page.wait_for_timeout(150)
     page.screenshot(path=str(dest/(path.replace('/','-')+f'-{width}-{position}.png')))
    page.evaluate('window.scrollTo(0,0)')
 page.set_viewport_size({'width':1200,'height':630})
 page.goto('http://127.0.0.1:8000/index.html');page.locator('img').evaluate_all('(xs)=>xs.forEach(x=>x.loading="eager")');page.evaluate('document.fonts.ready');page.evaluate('Promise.all([...document.images].map(img => img.decode().catch(() => null)))')
 page.screenshot(path=str(root/'assets/social-preview.png'))
 print('Screenshots',len(paths)*3,flush=True)
 browser.close()
