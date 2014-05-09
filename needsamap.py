#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import tweepy

# help text
helptext = "Filter the public Twitter timeline for people who need Citymaps!"
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)

# twitter auth
consumer_key="hvfDglrXs5cr4eBfzenNiQ"
consumer_secret="M2qooErR1TYSow0wiidUPZ72VCsBzTsl6jZLW3qQ"
access_token="77774652-FCjsPcvXKLpkhxyKtV7tO01dLDftxZvo8O2RdGW4b"
access_token_secret="6pfMl3fORwIjrdmNhIoQ8R9Sqw49DpaEb9fOrIVS9htoJ"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twapi = tweepy.API(auth)

streaming = False
if len(sys.argv) == 2 and sys.argv[1] == "stream":
  streaming = True


def render(status):
  text = "%s\n@%s, %s via %s" % (status.text, 
                                 status.author.screen_name, 
                                 status.created_at, 
                                 status.source)
  return text.encode("utf-8")


class CustomStreamListener(tweepy.StreamListener):

  def on_status(self, status):
      
    # We'll simply print some values in a tab-delimited format
    # suitable for capturing to a flat file but you could opt 
    # store them elsewhere, retweet select statuses, etc.
    try:
      print render(status)

    except Exception, e:
      print >> sys.stderr, 'Encountered Exception:', e
      pass

    #sys.exit()

  def on_error(self, status_code):
    print >> sys.stderr, 'Encountered error with status code:', status_code
    return True # Don't kill the stream

  def on_timeout(self):
    print >> sys.stderr, 'Timeout...'
    return True # Don't kill the stream


# Terms to track or search
track = [
    "where can i find a place",
    "suggest restaurant",
    "suggest food",
    "suggest place",
    "suggest hotel",
    "help recommend restaurant",
    "help recommend food",
    "help recommend place",
    "help recommend hotel",
    "restaurant near",
    "good hotel in",
    "cheap hotel in",
]

# if "stream" is the first parameter, wait for a new tweet using Realtime API instead of searching
if streaming:
  streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

  # Optionally filter the statuses you want to track by providing a list
  # of users to "follow".

  print >> sys.stderr, 'Filtering the public timeline'

  streaming_api.filter(follow=None, track=track)

else:
  rand = random.randint(0,len(track)-1)
  rs = track[rand]

  results = twapi.search(rs)
  if len(results) > 0:
    for s in results:
      if s.text.find("http") == -1 and s.text.find("RT @") == -1:
        status = s
        break

    if status:
      print render(status)

  else:
    print "No results found"
