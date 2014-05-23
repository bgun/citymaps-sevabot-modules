#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
It's stupid.
"""
import os
import sys
import random

# help text
helptext = "What's stupid today?"
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)

phrase = " ".join(sys.argv[1:100])

if phrase[len(phrase)-1] == 's':
  plural = "are"
else:
  plural = "is"

template = "Anthony thinks {} {} stupid."
print template.format(phrase, plural)
