#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pulls the latest from citymaps-sevabot-modules.
# Modules are executed from the sevabot directory, hence "cd modules".
# I'm lazy so just using a nested git folder, not a real submodule.
import os
resp = os.system("cd modules;git pull origin master;chmod 775 *")

print resp
