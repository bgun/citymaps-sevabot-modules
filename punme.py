#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shows a random pun
"""

import sys
import httplib
from pyquery import PyQuery as pq

def main():
    conn = httplib.HTTPConnection("www.punoftheday.com")

    conn.request("GET", "/cgi-bin/randompun.pl")
    response = conn.getresponse()

    doc = pq(response.read())

    print doc.find(".dropshadow1 p").html()




if __name__ == '__main__':
    main()