
import os
from os import path
from shutil import copy

import rvirtualenv


def generate(where):
    '''
    create dirs and files after virtualenv dir itself is prepared
    '''
    base = path.dirname(rvirtualenv.__file__)
    pybin = path.join(base, 'template', 'bin', 'python.py')

    os.chdir(where)
    os.mkdir('bin')
    copy(pybin, path.join(where, 'bin', 'python.py'))

