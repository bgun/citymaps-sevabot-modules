#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import string
import re

# help text
helptext = "math: evaluates a mathematical expression"
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)

# get first 100 arguments in the form of one long string
params = string.join(sys.argv[1:100], ' ')
# sanitize. Sorry, no algebra. Also no commas because Python turns it into a list.
clean = re.sub(r'[a-z,A-Z]','',params).strip()
# python power operator is "**", but I prefer "^"
expr = re.sub(r'\^','**',clean)

print clean + " = " + str(eval(expr))
