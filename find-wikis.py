#!/usr/bin/env python

import urllib2
import re
import sys

print("find-wikis.py (c) 2020 v@fandom.com")

wikis = sys.stdin.readlines()

if len(wikis) == 0:
  sys.exit('Need list of wiki URLs in stdin')

for wiki_url in wikis:
  wiki_url = wiki_url.strip()
  html_content = urllib2.urlopen(wiki_url).read()
  # find wiki_id from ads tags
  matches = re.findall(r"\"wikiId\": ?(\d+)", html_content)
  wiki_id = 0

  if len(matches) > 0:
    wiki_id = matches[0]

  print("{}\t{}".format(wiki_url, wiki_id))
