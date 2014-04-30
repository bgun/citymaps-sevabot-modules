#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Shows a random asian emoticon
"""
import os
import httplib
import random
import sys
import re
from pyquery import PyQuery as pq

def main():
    pages = [
        "happy-japanese",
        "angry-japanese",
        "bear",
        "love-japanese",
        "confused-japanese",
        "whatever-japanese",
        "surprised-japanese",
        "embarrassed-japanese",
        "smug-japanese",
        "worried-japanese",
        "evil-japanese",
        "sad",
        "scared",
        "cat",
        "dog",
        "sea-creature",
        "monkey",
        "pig"
    ]



    type = ""
    if len(sys.argv) > 1:
        input = sys.argv[1]

        if input == "list":
            print "Available pages: "
            for page in pages:
                print page.replace("-japanese", "")

            return

        for page in pages:
            if page.find(input) == 0:
                type = page
                break


    if len(type) == 0:
        type = pages[random.randint(0, len(pages) - 1)]

    page = type + "-emoticons"

    conn = httplib.HTTPConnection("hexascii.com")
    conn.request("GET", "/" + page, None, {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
    })

    response = conn.getresponse()

    doc = pq(response.read())

    emoticons = doc.find(".field-items table td")


    for i in range(0, 3, 1):
        index = random.randint(0, len(emoticons) - 1)
        html = pq(emoticons[index]).text()

        if (html and len(html) > 0):
            html = html.replace("\n", "").strip()
            # replace possible skype emotes
            html = html.replace(":)", ": )") \
                .replace(";)", "; )")

            print html.encode("utf-8")
            return

if __name__ == '__main__':
  main()