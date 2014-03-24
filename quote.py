#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import tweepy

# help text
helptext = "quote: Try '!quote campagna' or '!quote margot'."
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)

# twitter auth
consumer_key="hvfDglrXs5cr4eBfzenNiQ"
consumer_secret="M2qooErR1TYSow0wiidUPZ72VCsBzTsl6jZLW3qQ"
access_token="77774652-FCjsPcvXKLpkhxyKtV7tO01dLDftxZvo8O2RdGW4b"
access_token_secret="6pfMl3fORwIjrdmNhIoQ8R9Sqw49DpaEb9fOrIVS9htoJ"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


name = sys.argv[1]

names = {
  "margot"  : "margotquotes",
  "anthony" : "campagnaquotes",
  "campagna": "campagnaquotes",
  "kanye"   : "kanyewest",
  "jaden"   : "officialjaden"
}

screen_name = ""
for k,v in names.iteritems():
  if name == k:
    screen_name = v

# unrecognized name
if screen_name == "":
  sys.exit("I don't know who '"+name+"' is.")


results = api.user_timeline(screen_name=screen_name,count=200)

quotes = []
for r in results:
  quotes.append(r.text)

rand = random.randint(0,len(quotes)-1)
prefix = "@"+screen_name+": "

print prefix+quotes[rand]
