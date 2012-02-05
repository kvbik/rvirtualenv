
from os.path import join, dirname
from os import makedirs
from shutil import copytree

import rvirtualenv


def ignore(src, names):
    def invalid(s):
        if '__pycache__' in s:
            return True
        if s.endswith('pyc'):
            return True
        return False
    ignored = set()
    ignored.update(( i for i in names if invalid(i) ))
    return ignored

def copy(where):
    '''
    main function for copying template/venv into specified new virtualenv
    '''
    base = dirname(rvirtualenv.__file__)
    copytree(join(base, 'template', 'venv'), where, ignore=ignore)
    makedirs(join(where, 'src'))
    copytree(join(base, 'template', 'inst'), join(where, 'src', 'rvirtualenvkeep'), ignore=ignore)
    copytree(join(base, 'rvirtualenvinstall'), join(where, 'rvirtualenvinstall'), ignore=ignore)

