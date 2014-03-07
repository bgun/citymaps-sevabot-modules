#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Adam'

import sys
import httplib
from HTMLParser import HTMLParser

class CustomParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.found = False
        self.nextIsPun = False
        self.punText = ""
        self.done = False

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for attr in attrs:
                if attr[0] == "class" and attr[1] == "dropshadow1":
                    self.found = True

        if tag == "p" and self.found:
            self.nextIsPun = True

    def handle_data(self, data):
        if self.nextIsPun and not self.done:
            self.punText = data
            self.done = True

def main():
    conn = httplib.HTTPConnection("www.punoftheday.com")

    conn.request("GET", "/cgi-bin/randompun.pl")
    response = conn.getresponse()

    parser = CustomParser()

    parser.feed(response.read())

    print parser.punText




if __name__ == '__main__':
    main()