#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import tweepy

consumer_key="hvfDglrXs5cr4eBfzenNiQ"
consumer_secret="M2qooErR1TYSow0wiidUPZ72VCsBzTsl6jZLW3qQ"

access_token="77774652-FCjsPcvXKLpkhxyKtV7tO01dLDftxZvo8O2RdGW4b"
access_token_secret="6pfMl3fORwIjrdmNhIoQ8R9Sqw49DpaEb9fOrIVS9htoJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

results = api.user_timeline(id='2355217364',count=200)

quotes = []
for r in results:
  quotes.append(r.text)

rand = random.randint(0,len(quotes))
prefix = "@campagnaquotes: "

print prefix+quotes[rand]
