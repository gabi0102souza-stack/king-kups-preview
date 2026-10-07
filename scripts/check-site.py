"""Dependency-free structural checks for the buildless Pages site."""
from html.parser import HTMLParser
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = []; self.links = []; self.assets = []; self.images = []; self.h1 = 0; self.robots = None; self.labels = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a': self.links.append(a.get('href', ''))
        if tag == 'h1': self.h1 += 1
        if tag == 'meta' and a.get('name') == 'robots': self.robots = a.get('content')
        if tag == 'img':
            self.images.append(a); self.assets.append(a['src'])
            for part in a.get('srcset', '').split(','):
                if part.strip(): self.assets.append(part.strip().split()[0])
        if tag in ('link', 'script'):
            path = a.get('href') if tag == 'link' else a.get('src')
            if path and not path.startswith('data:'): self.assets.append(path)
        if tag == 'label': self.labels.append(a.get('for'))

html = (root / 'index.html').read_text(encoding='utf-8')
p = SiteParser(); p.feed(html)
assert p.h1 == 1, 'Expected exactly one H1'
assert len(p.ids) == len(set(p.ids)), 'Duplicate IDs'
assert p.robots == 'noindex, nofollow', 'Preview indexing safeguard missing'
assert '\u2014' not in html, 'Em dash found in public copy'
for link in p.links:
    assert link, 'Empty link'
    if link.startswith('#') and len(link) > 1: assert link[1:] in p.ids, f'Broken anchor {link}'
for path in set(p.assets): assert (root / path).is_file(), f'Missing local asset {path}'
for img in p.images:
    assert img.get('alt'), 'Missing factual alt'
    assert img.get('width') and img.get('height'), 'Image dimensions missing'
    assert img.get('srcset') and img.get('sizes'), 'Responsive image missing'
for label in p.labels: assert label in p.ids, f'Missing form field for label {label}'
for path in re.findall(r"url\(['\"]?([^)'\"]+)", (root / 'styles.css').read_text(encoding='utf-8')):
    assert (root / path).is_file(), f'Missing CSS asset {path}'
for doc in ['README.md','docs/RESEARCH.md','docs/ASSET_SOURCES.md','docs/QA_REPORT.md','CREATIVE_DIRECTION.md','SITE_STRATEGY.md','SELF_CRITIQUE.md']:
    assert (root / doc).is_file(), f'Missing required document {doc}'
assert (root / '.nojekyll').is_file()
assert 'Disallow: /' in (root / 'robots.txt').read_text()
print(f'PASS: {len(p.links)} links, {len(set(p.assets))} local assets, {len(p.images)} responsive photographs, one H1, unique IDs, noindex, labels and all required docs')
