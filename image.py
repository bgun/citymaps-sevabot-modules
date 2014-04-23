#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Performs a Google Image search and returns an image URL.
This API is deprecated by Google so who knows how long it'll last...

Parameters:
  query - use quotes for multiple words
  index - from 0 to 7, since 8 is the max size of a single page of results
"""

import sys
import string
import random
import requests
import json

# help text
helptext = "Returns the first response from a Google Image search."
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)


query = sys.argv[1]
index = 0
if len(sys.argv) > 2:
  try:
    index = int(sys.argv[2])
    if index > 7:
      index = 7
  except ValueError:
    print "Second parameter should be a number from 0 to 7. Use quotes for multi-word searches."


def getFirstGoogleImageUrl(q):
  url = "http://ajax.googleapis.com/ajax/services/search/images"
  payload = {
    'v'   : '1.0',
    'q'   : q,
    'rsz' : 8
  }
  r = requests.get(url, params=payload)
  j = json.loads(r.text)
  return j['responseData']['results'][index]['url']


if __name__ == '__main__':
  print getFirstGoogleImageUrl(query)
