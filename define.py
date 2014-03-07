#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get the definition of a word
"""
import os
import sys
import httplib
from pyquery import PyQuery as pq

def main(args):
    conn = httplib.HTTPConnection("m.dictionary.com")

    word = args[0]

    if word == "anthony":
        word = "stupid"

    if word == "vegan":
        word = "pretentious"

    if word == "raja":
        word = "boss"

    url = "/definition/" + word

    conn.request("GET", url, None, {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
    })
    response = conn.getresponse()

    doc = pq(response.read())

    resultItem = doc.find("#embed_dresultitem_r3")

    if len(resultItem) > 0:
        for result in resultItem.children():
            text = ""

            for child in pq(result).children():
                text += pq(child).html()

            print text.encode("ascii", "ignore")
    else:
        print "No definition for " + word + ".  Did Anthony type this one?"


if __name__ == '__main__':
    main(sys.argv[1:])