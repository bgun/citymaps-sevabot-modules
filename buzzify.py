#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import sys
import string

# help text
helptext = "buzzify: create a viral headline"
if len(sys.argv) == 1:
  sys.exit(helptext)
if len(sys.argv) == 2 and sys.argv[1] == "help":
  sys.exit(helptext)


def getNum():
  return ""+str(random.randint(5,50))


def getAdjective():
  adjectives = [
    "incredible",
    "amazing",
    "stunning",
    "most important",
    "mind-blowing",
    "worst"
  ]
  rand = random.randint(0, len(adjectives)-1)
  return adjectives[rand]


def getDescriptor():
  descriptors = [
    "speechless",
    "heartbroken",
    "in tears",
    "in stitches",
    "wanting more"
  ]
  rand = random.randint(0, len(descriptors)-1)
  return descriptors[rand]


def getNSuffix():
  suffixes = [
    "You'll Never Guess #%NUM",
    "#%NUM Is So True!",
    "#%NUM Will Blow Your Mind",
    "#%NUM Left Me %DESC",
    "#%NUM Changed My Life",
    "#%NUM Will Make Your Day"
  ]
  rand = random.randint(0, len(suffixes)-1)
  suffix = suffixes[rand]
  suffix = suffix.replace("%NUM", str(random.randint(1,5)))
  return suffix


def getVideoSuffix():
  suffixes = [
    "Boy, Do I Have A Video For You",
    "Do Yourself A Favor And Watch This",
    "This Video Will Leave You %DESC"
  ]
  rand = random.randint(0, len(suffixes)-1)
  suffix = suffixes[rand]
  return suffix


def main():
  topic = string.join(sys.argv[1:100], " ")

  templates = [
    # listicles
    "%NUM %ADJ tweets about %TOPIC you missed today. %NSUFFIX",
    "%NUM signs you're a %TOPIC fan. %NSUFFIX",
    "%NUM %ADJ Facts About %TOPIC. %NSUFFIX",
    "%NUM %ADJ %TOPIC Memes you'll Ever See. %NSUFFIX",
    "%NUM things about %TOPIC that kids These Days Will Never Understand. %NSUFFIX",
    "%NUM cats who remind us of %TOPIC. %NSUFFIX",
    "%NUM %TOPIC Stereotypes that Are Completely Accurate. %NSUFFIX",
    "Top %NUM most WTF %TOPIC moments. %NSUFFIX",
    "%NUM jokes only %TOPIC fans will understand",
    "%NUM things %TOPIC people secretly love",
    # videos
    "What The Heck Is Happening In This %TOPIC Video? Everyone Stops and Stares",
    "Love %TOPIC? %VSUFFIX",
    "Obsessed With %TOPIC? %VSUFFIX",
    "A 5 Year Old Just Explained %TOPIC In 30 Seconds. %VSUFFIX",
    # other
    "This Is The Hardest %TOPIC Quiz You'll Ever Take",
    "How Obsessed With %TOPIC Are You? Take This Quiz And Find Out",
  ]

  rand = random.randint(0,len(templates)-1)
  template = templates[rand]

  template = template.replace("%NUM", getNum())
  template = template.replace("%TOPIC", topic)
  template = template.replace("%NSUFFIX", getNSuffix())
  template = template.replace("%VSUFFIX", getVideoSuffix())
  template = template.replace("%DESC", getDescriptor())
  template = template.replace("%ADJ", getAdjective())

  return " ".join(w.capitalize() for w in template.split())


if __name__ == '__main__':
  print main()
