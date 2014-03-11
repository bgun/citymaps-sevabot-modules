#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Shows a random asian emoticon
"""
import os
import httplib
import random
from pyquery import PyQuery as pq

conn = httplib.HTTPConnection("www.fortunecookiemessage.com")

conn.request("GET", "/", None, {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
})

response = conn.getresponse()

doc = pq(response.read())

fortune = pq(doc.find("table p[align='center'] a")[0])

if len(fortune.children()) > 0:
    print pq(fortune.children()[0]).html().encode("utf-8")
else:
    print fortune.html().encode("utf-8")

