#!/usr/bin/env python

'''
use this file directly, or just set PYTHONPATH to your virtualenv directory
and run system wide python instance
'''

import os, sys
from os import path
from os.path import join, dirname, pardir, abspath


def get_this_path():
    '''
    we do expect scripts are installed just one level deeper from venv
    '''
    base = dirname(__file__)
    thispath = abspath(join(base, pardir))
    return thispath

def inject_pythonpath():
    '''
    insert virtualevn path into pythonpath
    '''
    pypath = os.environ.get('PYTHONPATH', '').split(path.pathsep)
    thispath = get_this_path()
    try:
        pypath.remove('')
        pypath.remove(thispath)
    except ValueError:
        pass
    pypath.insert(0, thispath)
    os.environ['PYTHONPATH'] = path.pathsep.join(pypath)

def prepare_argv(argv=[]):
    '''
    prepare argv to run
      * windows platform needs add quotes around arguments with spaces
    '''
    def q(s):
        return '"%s"' % s.replace('"', '\\"')
    if sys.platform == 'win32':
        argv = map(q, argv)
    return tuple(argv)

def run(argv):
    os.execvp(sys.executable, argv)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    inject_pythonpath()
    run(prepare_argv(argv))

if __name__ == '__main__':
    main()

