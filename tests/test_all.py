#!/usr/bin/env python

'''
poor man's nosetests
'''

import sys
from os import path
import unittest


def runtests():
    base = path.abspath(path.join(path.dirname(__file__), path.pardir))

    # hack pythonpath to contain dir to load proper module for testing
    oldpath = sys.path[:]
    if base in sys.path:
        sys.path.remove(base)
    sys.path.insert(0, base)

    r = unittest.TextTestRunner()
    l = unittest.TestLoader()

    m = [
        'tests.test_copy',
        'tests.test_generate',
        'tests.test_rvirtualenv',
    ]

    result = r.run(l.loadTestsFromNames(m))
    sys.exit(not result.wasSuccessful())

if __name__ == '__main__':
    runtests()

