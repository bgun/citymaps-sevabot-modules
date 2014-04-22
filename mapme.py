#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Links to a random Citymaps map
"""

import sys
import random
import requests
import json

def getCitymapsUsermap():
    queries = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    query = queries[random.randint(0,len(queries)-1)]
    url = "http://coresearch.citymaps.com/search/whatWhere/"+query
    payload = {
        'radius'    : 10,
        'businesses': 0,
        'locations' : 0,
        'user_maps' : 1,
        'users'     : 0,
        'where'     : 1000
    }
    r = requests.get(url, params=payload)
    j = json.loads(r.text)
    count = j['count']
    if count == 0:
      return None
    else:
      rand = random.randint(0,count-1)
      return j['items'][rand]


def formatResponse(usermap):
  if usermap == None:
    return "No usermap found"
  else:
    return "\"{0}\" by @{1} - ({2} markers). {3}".format(
      usermap['name'],
      usermap['owner_username'],
      usermap['num_markers'],
      "http://citymaps.com/m/"+usermap['object_id']
    )


if __name__ == '__main__':
    print formatResponse(getCitymapsUsermap()).encode("utf-8")
