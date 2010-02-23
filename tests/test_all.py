#!/usr/bin/env python

import sys
from os import path
import nose


def runtests():
    base = path.abspath(path.join(path.dirname(__file__), path.pardir))

    # hack pythonpath to contain dir to load proper module for testing
    oldpath = sys.path[:]
    if base in sys.path:
        sys.path.remove(base)
    sys.path.insert(0, base)

    # hack with argv if we are called from setup.py
    argv = sys.argv[:]
    if 'setup.py' in argv[0] and len(argv) >= 2 and argv[1] == 'test':
        argv = [argv[0]] + argv[2:]
    oldargv = sys.argv[:]
    sys.argv = argv

    nose.run_exit(defaultTest=base)

if __name__ == '__main__':
    runtests()

