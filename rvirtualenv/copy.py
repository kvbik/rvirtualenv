
import os
from os import path
from shutil import rmtree, copytree


def copy(where):
    '''
    main function for copying template/venv into specified new virtualenv
    '''
    base = path.dirname(__file__)
    venv = path.join(base, 'template', 'venv')
    copytree(venv, where)

