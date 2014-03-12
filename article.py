#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from random import randint
import requests
import json

# help text
helptext = "article: generate a random piece of hopefully interesting reading material"
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)


def getRedditUrl(sub):
  return "http://reddit.com/r/"+sub+".json"


def getArticle():
  sub = "technology"
  url = getRedditUrl(sub)
  r = requests.get(url)
  j = json.loads(r.text)

  resp = ""
  rawArticles = j['data']['children']

  if len(rawArticles) == 0:
    sys.exit("No results found.")

  articles = []
  for i,a in enumerate(rawArticles):
    if a["data"]["domain"] != "!self"+sub:
      articles.append(a["data"])

  count = len(articles)
  rand = randint(0,count-1)

  return articles[rand]


article = getArticle()
print article["title"] + " - " + article["url"]
