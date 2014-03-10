#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Shows a random asian emoticon
"""
import os
import httplib
import random
from pyquery import PyQuery as pq

conn = httplib.HTTPConnection("www.emoticonfun.org")

conn.request("GET", "/", None, {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
})

response = conn.getresponse()

doc = pq(response.read())

emoticons = doc.find(".emoteitem .emote")

index = random.randint(0, len(emoticons) - 1)

print pq(emoticons[index]).html().encode("utf-8")
