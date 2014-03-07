#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import sys
import string

# help text
helptext = "bobify: what would Bob name it?"
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)

params = sys.argv[1:100]
words = [
  "dev",
  "dev-core",
  "dev-search",
  "core",
  "core-admin",
  "core-api",
  "play"
]

#first word
rand = random.randint(0,len(words)-1)
resp = words[rand]

#interpolate words between all params
for p in params:
  rand = random.randint(0,len(words)-1)
  resp = string.join([resp, words[rand], p], '-')

# finally
rand = random.randint(0,len(words)-1)
resp = string.join([resp, words[rand]], '.')

print resp
