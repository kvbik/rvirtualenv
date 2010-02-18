
import os
from os import path
from shutil import rmtree, copytree

import rvirtualenv


def copy(where):
    '''
    main function for copying template/venv into specified new virtualenv
    '''
    base = path.dirname(rvirtualenv.__file__)
    venv = path.join(base, 'template', 'venv')

    copytree(venv, where)

