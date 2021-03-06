#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get the definition of a word
"""
import os
import sys
import httplib
import random
import urllib
from pyquery import PyQuery as pq

def getResponse(host, url):
    conn = httplib.HTTPConnection("www.urbandictionary.com")

    conn.request("GET", url, None, {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
    })

    response = conn.getresponse()

    redirect = response.getheader("Location", "")
    if (len(redirect) > 0):
        url = redirect[redirect.rfind('/'):]
        return getResponse(host, url)


    return response

def main(args):
    word = " ".join(args)

    if word == "anthony":
        word = "stupid"

    #if word == "vegan":
    #    word = "pretentious"

    if word == "raja":
        rajaWords = ["crybaby", "woman", "sensitive", "insecure"]
        word = rajaWords[random.randint(0, len(rajaWords)-1)]


    wordParam = urllib.quote_plus(word)
    url = "/define.php?term=" + wordParam

    response = getResponse("www.urbandictionary.com", url)

    doc = pq(response.read())

    print "Definition of: " + word

    meaning = doc.find(".meaning")

    if len(meaning) > 0:
        strippedHtml = meaning.html().replace("<br/>", "\n")
        print pq(strippedHtml).text().encode("utf-8")

    else:
        url = "/definition/" + wordParam
        response = getResponse("m.dictionary.com", url)

        doc = pq(response.read())

        resultItem = doc.find("#embed_dresultitem_r3")

        if len(resultItem) > 0:
            print "Definition of: " + word

            for result in resultItem.children():
                text = ""

                for child in pq(result).children():
                    text += pq(child).text()

                print text.encode("utf-8")
        else:
            print "No definition for " + word + ".  Did Anthony type this one?"


if __name__ == '__main__':
    main(sys.argv[1:])