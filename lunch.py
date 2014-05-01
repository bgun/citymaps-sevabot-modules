#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Wheel of lunch!
"""
import sys
import random

progname = 'lunch'


def main(args):
	print "This is why we can't have nice things..."
	return
    """The program entry point."""

    random.seed()
    defaultCuisines = ['Chinese', 'Indian', 'Thai', 'Japanese', 'BBQ', 'Salad', 'Sandwiches', 'Mediterranean', 'Mexican', 'Italian']

    if len(args) <= 0:
        # Pick a random cuisines from the default list
        print defaultCuisines[random.randint(0, len(defaultCuisines)-1)]
        return

    cmd = args[0]

    if cmd == 'help':
        print 'Usage:'
        print '       !lunch'
        print '       !lunch [comma seperated list of cuisines or places]'
        return
    else:
        # Select possible cuisines types
        args = " ".join(args)
        cuisines = args.split(",")
        print cuisines[random.randint(0, len(cuisines)-1)]
        return

if __name__ == '__main__':
    main(sys.argv[1:])