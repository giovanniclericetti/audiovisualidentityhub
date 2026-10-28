import os
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import json,collections
root=Path(__file__).resolve().parents[1]
(root/'verification/audit').mkdir(parents=True,exist_ok=True)
files=[*root.glob('*.html'),*root.glob('documentazione/*.html'),*root.glob('case-studies/*.html')]
issues=[];external=set();media=set();counts=collections.Counter()
for f in files:
 s=BeautifulSoup(f.read_text(),'html.parser');name=str(f.relative_to(root))
 if not s.main:continue
 for tag in s.select('[href],[src]'):
  url=tag.get('href',tag.get('src',''));u=urlsplit(url)
  if u.scheme in ['http','https']:
   if 'audiovisualidentityhub.vercel.app' not in u.netloc:external.add(url)
   continue
  if u.scheme:continue
  target=(root/u.path.lstrip('/') if u.path.startswith('/') else f.parent/u.path) if u.path else f
  if target.is_dir():target=target/'index.html'
  if not target.exists():issues.append([name,'missing path',url]);continue
  if u.fragment and target.suffix=='.html':
   other=BeautifulSoup(target.read_text(),'html.parser')
   if not other.find(id=unquote(u.fragment)):issues.append([name,'missing anchor',url])
 for img in s.select('img'):
  media.add(img.get('src',''))
  if not all(img.has_attr(x) for x in ['alt','width','height']):issues.append([name,'image attributes',str(img)[:200]])
 if len(s.select('h1'))!=1:issues.append([name,'h1 count',len(s.select('h1'))])
 for title in s.select('title'):counts[title.get_text()]+=1
 ids=[x['id'] for x in s.select('[id]')]
 if len(ids)!=len(set(ids)):issues.append([name,'duplicate ids',''])
print(json.dumps(issues,ensure_ascii=False,indent=2))
(root/'verification/audit/static-issues.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2))
(root/'verification/audit/external-urls.json').write_text(json.dumps(sorted(external),ensure_ascii=False,indent=2))
print('Pages',len(files),'external urls',len(external),'image sources',len(media),'duplicate titles',[x for x,v in counts.items() if v>1])

if issues:
 raise SystemExit(1)
