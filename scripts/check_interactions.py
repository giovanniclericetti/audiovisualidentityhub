import os
from pathlib import Path
from playwright.sync_api import sync_playwright,expect
import json
root=Path(__file__).resolve().parents[1]
(root/'verification/audit').mkdir(parents=True,exist_ok=True)
checks=[]
def done(name):checks.append(name)
with sync_playwright() as p:
 b=p.chromium.launch(channel=os.environ.get('AIH_BROWSER_CHANNEL','chrome'),headless=True)
 page=b.new_page(viewport={'width':390,'height':844})
 page.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8000') else r.abort())
 for path in ['index.html','about.html','documentazione/1.1.html','documentazione/biblio.html','case-studies/intro-case-studies.html','case-studies/4-raiyoyo.html']:
  page.goto('http://127.0.0.1:8000/'+path)
  toggle=page.locator('.menu-toggle');nav=page.locator('#site-nav')
  expect(toggle).to_be_visible();expect(nav).to_be_hidden()
  toggle.focus();page.keyboard.press('Enter');expect(nav).to_be_visible();expect(toggle).to_have_attribute('aria-expanded','true')
  page.keyboard.press('Tab');expect(nav.locator('a').first).to_be_focused()
  page.keyboard.press('Escape');expect(nav).to_be_hidden();expect(toggle).to_be_focused()
  toggle.click();page.mouse.click(5, 650);expect(nav).to_be_hidden()
  toggle.click();page.locator('main').focus();expect(nav).to_be_hidden()
  toggle.click();page.set_viewport_size({'width':1024,'height':844});expect(toggle).to_have_attribute('aria-expanded','false');expect(nav).to_be_visible()
  page.set_viewport_size({'width':390,'height':844});expect(nav).to_be_hidden()
  done('menu mouse/keyboard/Escape/outside/focus/resize: '+path)
 page.goto('http://127.0.0.1:8000/documentazione/biblio.html')
 page.locator('.chapter-menu summary').click();expect(page.locator('.chapter-menu a[href="/documentazione/3.5.html"]')).to_be_visible()
 expect(page.locator('.chapter-menu a[aria-current=page]')).to_have_attribute('href','/documentazione/biblio.html')
 expect(page.locator('.chapter-pagination')).to_have_count(1)
 page.locator('.chapter-pagination a[rel=prev]').click();expect(page).to_have_url('http://127.0.0.1:8000/documentazione/3.5.html')
 page.locator('.chapter-pagination a[rel=next]').click();expect(page).to_have_url('http://127.0.0.1:8000/documentazione/biblio.html');done('chapter index, active state, previous/next')
 for path in ['index.html','about.html']:
  page.goto('http://127.0.0.1:8000/'+path)
  expect(page.locator('.motion-toggle')).to_have_count(0)
  page.emulate_media(reduced_motion='reduce')
  assert page.locator('.loop-track,.ribbon-track').evaluate_all('(xs)=>xs.every(e=>getComputedStyle(e).animationName==="none")')
  page.emulate_media(reduced_motion='no-preference');done('no pause buttons/reduced motion: '+path)
 page.goto('http://127.0.0.1:8000/case-studies/intro-case-studies.html')
 initial=set(page.locator('.study-card').evaluate_all('(xs)=>xs.map(x=>x.href)'))
 for width in [320,768,1280,1920,390]:
  page.set_viewport_size({'width':width,'height':844});page.wait_for_timeout(100)
  assert set(page.locator('.study-card').evaluate_all('(xs)=>xs.map(x=>x.href)'))==initial
  expect(page.locator('.study-card')).to_have_count(15)
 done('15 archive cards preserved across all column counts')
 page.goto('http://127.0.0.1:8000/about.html');expect(page.locator('.about-ctas a').last).to_have_attribute('href','mailto:audiovisualidentityhub@gmail.com');done('contribution CTA points to official email')
 context=b.new_context(java_script_enabled=False,viewport={'width':320,'height':844})
 fallback=context.new_page()
 fallback.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8000') else r.abort())
 for path in ['index.html','documentazione/1.1.html','case-studies/intro-case-studies.html']:
  fallback.goto('http://127.0.0.1:8000/'+path);expect(fallback.locator('#site-nav')).to_be_visible()
 done('navigation usable without JavaScript')
 touch_context=b.new_context(viewport={'width':390,'height':844},has_touch=True,is_mobile=True)
 touch=touch_context.new_page()
 touch.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8000') else r.abort())
 touch.goto('http://127.0.0.1:8000/index.html')
 touch.locator('.menu-toggle').tap();expect(touch.locator('#site-nav')).to_be_visible()
 touch.locator('#site-nav a').last.tap();expect(touch).to_have_url('http://127.0.0.1:8000/about.html')
 done('touch menu and section navigation')
 b.close()
(root/'verification/audit/interactions.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print('Passed',len(checks),'interaction groups')
