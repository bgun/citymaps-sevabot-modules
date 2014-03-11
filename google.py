#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import os
import sys
import urllib

query = urllib.quote_plus(" ".join(sys.argv[1:]))

print "https://www.google.com/search?q=" + query