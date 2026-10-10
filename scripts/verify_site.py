#!/usr/bin/env python3
"""Check generated links, assets, anchors, layouts, and documentation hierarchy.

Uses only the Python standard library. Run after `bundle exec jekyll build`.
An optional baseurl argument verifies a build served below a URL prefix.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import json

ROOT = Path('_site')
PREFIX = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else ''


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids, self.classes = [], set(), set()
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        self.classes.update(attrs.get('class', '').split())
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


pages = {path: Page(path) for path in ROOT.rglob('*.html')}
errors = []
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target_url = unquote(url.path)
        if target_url.startswith('/'):
            if PREFIX and not target_url.startswith(PREFIX + '/'):
                errors.append(f'{path}: URL missing baseurl: {link}')
                continue
            target = ROOT / target_url.removeprefix(PREFIX).lstrip('/')
        else:
            target = path.parent / target_url if target_url else path
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{path}: missing target: {link}')
        elif url.fragment and target.suffix == '.html':
            parsed = pages.get(target) or Page(target)
            if unquote(url.fragment) not in parsed.ids:
                errors.append(f'{path}: missing anchor: {link}')

home = pages[ROOT / 'index.html']
assert 'home-page' in home.classes and 'side-bar' not in home.classes
assert [link for link in home.links if link.endswith('.js')] == [f'{PREFIX}/assets/js/theme.js']
spec_names = ['concepts', 'terminology', 'sync-client', 'media-player', 'networking',
              'coordination', 'protocols', 'data-saver']
for name in ['', *spec_names]:
    path = ROOT / 'spec' / name / 'index.html'
    page = pages[path]
    assert 'side-bar' in page.classes and 'main-content' in page.classes, path
    assert 'search-input' in page.ids, path
    assert 'project-nav' in page.classes, path
    for child in spec_names:
        assert f'{PREFIX}/spec/{child}/' in page.links, (path, child)
    if name:
        assert 'breadcrumb-nav' in page.classes, path
data_saver = pages[ROOT / 'spec/data-saver/index.html']
assert f'{PREFIX}/spec/protocols/' in data_saver.links
assert 'Protocols' in (ROOT / 'spec/data-saver/index.html').read_text()
for path, page in pages.items():
    assert f'{PREFIX}/assets/css/syncnuke.css' in page.links, path
    assert 'project-nav' in page.classes, path
    assert 'theme-toggle' in page.classes, path
    if 'home-page' not in page.classes:
        assert 'night-theme' in page.ids, path
    assert f'{PREFIX}/assets/js/theme.js' in page.links, path
    text = path.read_text()
    assert 'This site uses' not in text and '>Just the Docs<' not in text, path
assert (ROOT / 'CNAME').read_text().strip() == 'syncnuke.com'
search_data = json.loads((ROOT / 'assets/js/search-data.json').read_text())
search_urls = {item['url'] for item in search_data.values()}
assert not any(url.rstrip('/') == 'https://syncnuke.com' + PREFIX for url in search_urls)
for name in spec_names:
    assert any(url.endswith(f'/spec/{name}/') for url in search_urls), name
assert '--sn-accent' in (ROOT / 'assets/css/syncnuke.css').read_text()
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Verified {len(pages)} pages: links, anchors, assets, layouts, search, and hierarchy.')
