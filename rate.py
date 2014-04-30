#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import sys

count = min(int(sys.argv[1]), 10)

flavorText = [
    "Just no. (angry)",
    "You suck. (puke)",
    "Go home. (sleep)",
    "Fail. (doh)",
    "Meh. (dull)",
    "Sigh. (yawn)",
    "Try again. (speechless)",
    "Not bad ;)",
    "Good one. :)",
    "Nice! :D",
    "We have a winner! (rofl)"
]

text = "I give that a " + str(count) + "/10. " + flavorText[count] + "\n"


for i in range(0, count, 1):
    text += "(y)"

if count < 10:
    for i in range(count, 10, 1):
        text += "(n)"

print text.encode("utf-8")
