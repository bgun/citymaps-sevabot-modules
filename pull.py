#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from subprocess import call
resp = call(["git", "pull", "origin", "master"])

print resp
