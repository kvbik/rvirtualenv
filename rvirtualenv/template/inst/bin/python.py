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

def prepare_command(argv=[]):
    '''
    prepare command to run
    '''
    cmd = [sys.executable] + argv
    cmd = map(lambda s: '"%s"' % s.replace('"', '\\"'), cmd)
    cmdstr = ' '.join(cmd)
    return cmdstr

def run(cmd):
    os.system(cmd)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    inject_pythonpath()
    cmd = prepare_command(argv)
    if sys.platform == 'win32':
        cmd = '"%s"' % cmd
    run(cmd)

if __name__ == '__main__':
    main()

