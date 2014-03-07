#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import tweepy

consumer_key="hvfDglrXs5cr4eBfzenNiQ"
consumer_secret="M2qooErR1TYSow0wiidUPZ72VCsBzTsl6jZLW3qQ"

access_token="77774652-FCjsPcvXKLpkhxyKtV7tO01dLDftxZvo8O2RdGW4b"
access_token_secret="6pfMl3fORwIjrdmNhIoQ8R9Sqw49DpaEb9fOrIVS9htoJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

name = ""
if len(sys.argv) > 1:
  name = sys.argv[1]

screen_name = ""
if name == "margot":
  screen_name = "margotquotes"
if name == "campagna":
  screen_name = "campagnaquotes"

if screen_name != "":
  results = api.user_timeline(screen_name=screen_name,count=200)

  quotes = []
  for r in results:
    quotes.append(r.text)

  rand = random.randint(0,len(quotes))
  prefix = "@"+screen_name+": "

  print prefix+quotes[rand]

else:
  print "I don't know who '"+name+"' is."
