#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Wheel of lunch!
"""
import sys
import random

progname = 'lunch'


def main(args):
    """The program entry point."""

    random.seed()
    defaultCousines = ['Chinese', 'Indian', 'Thai', 'Japanese', 'BBQ', 'Salad', 'Sandwiches', 'Mediterranean', 'Mexican', 'Italian']

    if len(args) <= 0:
        # Pick a random cousine from the default list
        print defaultCousines[random.randint(0, len(defaultCousines)-1)]
        return

    cmd = args[0]

    if cmd == 'help':
        print 'Usage:'
        print '       !lunch'
        print '       !lunch [comma seperated list of cousines or places]'
        return
    else:
        # Select possible cousine types
        cousines = cmd.split(",")
        cousines = filter(None,cousines)
        print cousines[random.randint(0, len(cousines)-1)]
        return

if __name__ == '__main__':
    main(sys.argv[1:])
