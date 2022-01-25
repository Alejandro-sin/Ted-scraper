#!/usr/bin/env python3

import sys
import urllib.request
from lxml import html

if len(sys.argv) !=4:
    raise SystemExit("Usage: script + topic+ + page + per_page")

topic = sys.argv[1]
page_number = sys.argv[2]
per_page = sys.argv[3]


u = urllib.request.urlopen('https://www.ted.com/search?page={}&per_page={}&q={}'.format(page_number, per_page, topic.replace(" ","+")))

data = u.read()
doc = html.document_fromstring(data)

for title in doc.cssselect("article.search__result h3 a"):
    print(title.text_content())




