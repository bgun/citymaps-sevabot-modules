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
  

class CustomStreamListener(tweepy.StreamListener):

  def on_status(self, status):
      
    # We'll simply print some values in a tab-delimited format
    # suitable for capturing to a flat file but you could opt 
    # store them elsewhere, retweet select statuses, etc.
    self.render(status)

  def render(self, status):
    try:
      print "%s\n@%s, %s via %s" % (status.text, 
                                status.author.screen_name, 
                                status.created_at, 
                                status.source,)
    except Exception, e:
      print >> sys.stderr, 'Encountered Exception:', e
      pass

    sys.exit()

  def on_error(self, status_code):
    print >> sys.stderr, 'Encountered error with status code:', status_code
    return True # Don't kill the stream

  def on_timeout(self):
    print >> sys.stderr, 'Timeout...'
    return True # Don't kill the stream


# Terms to track or search
track = [
    "where can i find a",
    "cheap food",
    "recommend restaurant"
    "recommend food",
    "recommend hotel",
    "hotel near",
    "restaurant nyc",
    "restaurant chicago",
    "restaurant seattle",
    "hotel vegas",
    "recommend nyc",
    "recommend chicago",
    "recommend seattle",
    "recommend vegas",
]

if streaming:
  streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)

  # Optionally filter the statuses you want to track by providing a list
  # of users to "follow".

  print >> sys.stderr, 'Filtering the public timeline'

  streaming_api.filter(follow=None, track=track)

else:
  r = random.randint(0,len(track)-1)
  rs = track[r]

  results = twapi.search(rs)
  status  = results[0]

  print "Searching for "+rs

  print "%s\t%s\t%s\t%s" % (status.text, 
                            status.author.screen_name, 
                            status.created_at, 
                            status.source,)
