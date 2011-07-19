
from os.path import join, dirname
from shutil import copytree

import rvirtualenv


def copy(where):
    '''
    main function for copying template/venv into specified new virtualenv
    '''
    base = dirname(rvirtualenv.__file__)
    copytree(join(base, 'template', 'venv'), where)
    copytree(join(base, 'template', 'inst'), join(where, 'src', 'rvirtualenvkeep'))
    copytree(join(base, 'rvirtualenvinstall'), join(where, 'rvirtualenvinstall'))

