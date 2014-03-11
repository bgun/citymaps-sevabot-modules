#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import os
import sys
import urllib

query = " ".join(sys.argv[1:]).strip().replace(" ", "_")

print "https://en.wikipedia.org/wiki/" + query