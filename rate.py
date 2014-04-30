#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys

count = int(sys.argv[1])

text = ""


for i in range(0, count, 1):
    text += "(y)"

if count < 10:
    for i in range(count, 10, 1):
        text += "(n)"

print text.encode("utf-8")
