
import os
from os import path
from shutil import copy, rmtree, copytree
import sys
from distutils.core import setup

import rvirtualenv


def run_setup(what, where):
    '''
    install couple of helper modules via distutils
    because it creates its directory (via the correct schema)
    '''
    oldpath = os.getcwd()
    oldprefix = sys.prefix
    oldargv = sys.argv

    sys.prefix = where
    sys.argv = ['setup.py', 'install']
    os.chdir(what)

    dist = setup(
        name='rvirtualenvkeep',
        version='0.1',
        py_modules=['rvirtualenvkeep'],
        scripts=['bin/python.py'],
    )

    os.chdir(oldpath)
    sys.prefix = oldprefix
    sys.argv = oldargv

    return dist

def generate(where):
    '''
    create dirs and files after virtualenv dir itself is prepared
    '''
    base = path.dirname(rvirtualenv.__file__)
    inst = path.join(base, 'template', 'inst')
    tmp = path.join(where, 'tmp_inst')

    copytree(inst, tmp)
    run_setup(tmp, where)
    rmtree(tmp)

