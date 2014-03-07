#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get the definition of a word
"""
import os
import sys
import httplib
import xml.etree.ElementTree as ET

def main(args):
    conn = httplib.HTTPConnection("www.dictionaryapi.com")

    word = args[0]

    if word == "anthony":
        word = "stupid"

    url = "/api/v1/references/collegiate/xml/" + word + "?key=673c6f58-cdd8-4d1d-8ba1-4cb5aeebcc2f"

    conn.request("GET", url)
    response = conn.getresponse()

    data = response.read()

    root = ET.fromstring(data)

    if (len(root) > 0):
        print "Definition of: " + word

        entries = root.findall("entry")

        i = 1
        for entry in root.findall("entry"):
            print "\nEntry " + str(i) + ":\n"

            for d in entry.findall("def"):
                for dt in d.findall("dt"):
                    if (len(dt.text) > 1):
                        text = dt.text[1:]

                        print "- " + text

            i += 1
    else :
        print "No definition found for: " + word


if __name__ == '__main__':
    main(sys.argv[1:])