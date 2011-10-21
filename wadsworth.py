#!/usr/bin/env python

"""
Wadsworth Constant: http://redd.it/kxtzp

This script can apply the Wadsworth Constant to any input -- whether that input
be from `sys.stdin` or `sys.argv`.
"""

import sys


def wadsworth_constant(phrase=None):
    """
    The Wadsworth Constant states the first 30% of any input can be
    removed, yet the overall message remains the same.
    """
    if phrase:
        phrase = phrase.strip()
    elif len(sys.argv) > 1:
        phrase = ' '.join(sys.argv[1:])
    else:
        phrase = sys.stdin.readline().strip()
    index = int(round(len(phrase) * .3))
    first_word = phrase.find(' ', index) + 1
    wadsworth_value = phrase[first_word:]
    wadsworth_value = wadsworth_value[0].upper() + wadsworth_value[1:]
    return wadsworth_value


if __name__ == '__main__':
    print wadsworth_constant()
