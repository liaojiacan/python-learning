#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a usecase of sys module'

__author__ = 'liaojiacan'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello , world!'
    elif len(args) == 2:
        print 'hello , %s' %args[1]
    else:
        print 'too many arguments'


if __name__ == '__main__':
    test()
