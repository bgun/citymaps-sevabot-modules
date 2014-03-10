#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys

text = ""
for arg in sys.argv[1:]:
    text += arg + " "

print text.encode("utf-8")
