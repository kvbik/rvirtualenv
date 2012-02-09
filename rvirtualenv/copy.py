
from os.path import join, dirname, isfile
from os import makedirs, walk, remove
import shutil

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

def remove_ignored(src, dst, ignore=None):
    for base, dirs, files in walk(dst):
        ignored = set()
        if ignore is not None:
            ignored = ignore(base.replace(dst, src), dirs+files)
        for i in ignored:
            f = join(base, i)
            if not isfile(f):
                shutil.rmtree(f, True)
            else:
                remove(f)

def copytree(src, dst, symlinks=False, ignore=None):
    shutil.copytree(src, dst, symlinks)
    remove_ignored(src, dst, ignore)

def copy(where):
    '''
    main function for copying template/venv into specified new virtualenv
    '''
    base = dirname(rvirtualenv.__file__)
    copytree(join(base, 'template', 'venv'), where, ignore=ignore)
    makedirs(join(where, 'src'))
    copytree(join(base, 'template', 'inst'), join(where, 'src', 'rvirtualenvkeep'), ignore=ignore)
    copytree(join(base, 'rvirtualenvinstall'), join(where, 'rvirtualenvinstall'), ignore=ignore)

