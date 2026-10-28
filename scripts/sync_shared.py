#!/usr/bin/env python3
"""Render shared navigation/footer into static HTML; no browser or build dependency."""
import argparse
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/navigation.json').read_text())
CHAPTERS = [c for group in DATA['groups'] for c in group['chapters']]

def link(item, current, numbered=False):
    destination = item['href']
    section = destination.split('/')[1]
    state = 'page' if destination == current else 'location' if not numbered and section in ('documentazione', 'case-studies') and current.startswith('/'+section+'/') else None
    active = f' aria-current="{state}"' if state else ''
    return f'<a href="{html.escape(destination)}"{active}>{html.escape(item["title"])}</a>'

def render(source, current):
    nav = '<nav aria-label="Navigazione principale" id="site-nav">' + ''.join(link(x, current) for x in DATA['primary']) + '</nav>'
    source = re.sub(r'<nav\b[^>]*id="site-nav"[^>]*>.*?</nav>', lambda _: nav, source, flags=re.S)
    footer = (ROOT / 'templates/footer.html').read_text().strip()
    footer = footer.replace('{{emailDisplay}}', DATA['email'].replace('@', '<wbr>@'))
    for key in ('email', 'copyrightYear'):
        footer = footer.replace('{{'+key+'}}', str(DATA[key]))
    source = re.sub(r'<footer class="site-footer">.*?</footer>', lambda _: footer, source, flags=re.S)
    if current.startswith('/documentazione/'):
        chapter_nav = '<details class="chapter-menu" open><summary>Indice della ricerca</summary><nav aria-label="Capitoli della ricerca">'
        for group in DATA['groups']:
            chapter_nav += '<h2>' + html.escape(group['title']) + '</h2>'
            chapter_nav += ''.join(link(c, current, True) for c in group['chapters'])
        chapter_nav += '</nav></details>'
        source = re.sub(r'<details\b[^>]*class="chapter-menu"[^>]*>.*?</details>', lambda _: chapter_nav, source, flags=re.S)
        source = re.sub(r'<nav\b[^>]*class="chapter-pagination"[^>]*>.*?</nav>', '', source, flags=re.S)
        source = re.sub(r'<a class="reading-next"[^>]*>.*?</a>', '', source, flags=re.S)
        index = next(i for i, c in enumerate(CHAPTERS) if c['href'] == current)
        pagination = '<nav class="chapter-pagination" aria-label="Navigazione tra capitoli">'
        for offset, rel, text, arrow in [(-1, 'prev', 'Capitolo precedente', '←'), (1, 'next', 'Prosegui la lettura', '→')]:
            adjacent = index + offset
            if 0 <= adjacent < len(CHAPTERS):
                c = CHAPTERS[adjacent]
                label = f'{text}: {c["title"]}'
                pagination += f'<a class="reading-next" href="{c["href"]}" rel="{rel}" aria-label="{html.escape(label)}">{text} <span aria-hidden="true">{arrow}</span></a>'
        pagination += '</nav>'
        source = source.replace('</article>', pagination + '</article>')
    return source

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if generated shared content is out of date')
    args = parser.parse_args()
    stale = []
    for path in sorted([*ROOT.glob('*.html'), *ROOT.glob('documentazione/*.html'), *ROOT.glob('case-studies/*.html')]):
        source = path.read_text()
        if '<main' not in source:
            continue
        result = render(source, '/' + path.relative_to(ROOT).as_posix())
        if source != result:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.write_text(result)
    if args.check and stale:
        raise SystemExit('Shared content is out of date: ' + ', '.join(stale))
    urls = []
    for path in sorted([*ROOT.glob('*.html'), *ROOT.glob('documentazione/*.html'), *ROOT.glob('case-studies/*.html')]):
        content = path.read_text()
        if '<main' not in content or 'noindex' in content:
            continue
        urls.append('https://audiovisualidentityhub.vercel.app/' + path.relative_to(ROOT).as_posix())
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += ''.join(f'  <url><loc>{html.escape(url)}</loc></url>\n' for url in urls) + '</urlset>\n'
    sitemap_path = ROOT / 'sitemap.xml'
    if args.check:
        if not sitemap_path.exists() or sitemap_path.read_text() != sitemap:
            raise SystemExit('Sitemap is out of date')
    else:
        sitemap_path.write_text(sitemap)
    print(f'Shared content {"checked" if args.check else "updated"}: {len(stale)} differing pages')

if __name__ == '__main__':
    main()
