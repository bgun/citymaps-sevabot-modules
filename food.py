#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shows lunch choices from yelp.
"""

import sys
import httplib
from pyquery import PyQuery as pq

def main():
    conn = httplib.HTTPConnection("http://www.yelp.com")

    conn.request("GET", "/search?find_desc="+sys.argv[0]+"&find_loc=10065&ns=1#sortby=rating")
    response = conn.getresponse()
    html = pq(response.read())

    print html.find(".search-result-title").text()


if __name__ == '__main__':
    main()