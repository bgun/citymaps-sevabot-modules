#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shows lunch choices from yelp.
"""

import sys
import httplib
from pyquery import PyQuery as pq

def main():
    conn = httplib.HTTPConnection("www.yelp.com")

    url = "/search?find_desc="+sys.argv[1]+"&find_loc=10065&ns=1#sortby=rating"
    
    conn.request("GET", url, None, {
      "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"
    })

    response = conn.getresponse()
    html = pq(response.read(), parser ="html")

    print i.text() for i in html.items(".biz-name")

if __name__ == '__main__':
    main()