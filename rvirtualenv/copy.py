
from os import path
from shutil import copytree

import rvirtualenv


def copy(where):
    '''
    main function for copying template/venv into specified new virtualenv
    '''
    base = path.dirname(rvirtualenv.__file__)
    venv = path.join(base, 'template', 'venv')
    copytree(venv, where)
    venv = path.join(base, 'rvirtualenvinstall')
    copytree(venv, path.join(where, 'rvirtualenvinstall'))

