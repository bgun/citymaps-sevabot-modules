#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import requests
import json

baseUrl      = "http://foursquare.com/v"
apiUrl       = "https://api.foursquare.com/v2/venues/search"
clientId     = "DGLPOPEU2IN1ZH2MAWRKTBSGMFV1UZCOO53FNNKYBG1N1IF2"
clientSecret = "HNIIISJIEWUJA1U1JVJ0Z0SPU30EDKECCJ5ZNVARY1MB22FE"


# help text
helptext = "4sq: no query found. Usage: '!4sq babbo' or '!4sq starbuck Chicago,IL'"
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)


# first argument is query, second argument is optional location. Default is "nyc"
if len(sys.argv) == 2:
  q = sys.argv[1]
  n = "nyc"
if len(sys.argv) == 3:
  q = sys.argv[1]
  n = sys.argv[2]


def get4sq(query, near):
  count = 3
  payload = {
      'query': query,
      'near' : near,
      'client_id': clientId,
      'client_secret': clientSecret,
      'v': '20130815'
  }
  r = requests.get(apiUrl, params=payload)
  j = json.loads(r.text)

  resp = ""
  venues = j['response']['venues'][0:count]

  if len(venues) == 0:
    sys.exit("No results found.")

  for v in venues:
    resp = resp + v['name'] + ": "+baseUrl+"/"+v['id']+"\n"

  return resp


print get4sq(q, n)
