#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple sample module with Skype smileys
"""
import os
import random

random.seed()

emotes = ['angry','headbang','swear','facepalm','smoke']
print "(" + emotes[random.randint(0, len(emotes)-1)] + ")"
