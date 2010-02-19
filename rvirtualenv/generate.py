
import os
from os import path
from shutil import copy, rmtree, copytree
import sys
from distutils.core import setup

import rvirtualenv
from rvirtualenv.helpers import get_distutils_schema


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

    scripts = ['bin/python.py']
    if sys.platform == 'win32':
        scripts.append('bin/python.bat')
    else:
        scripts.append('bin/python')

    dist = setup(
        name='rvirtualenvkeep',
        version='0.1',
        py_modules=['rvirtualenvkeep'],
        scripts=scripts,
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

    # install setup.py via distutils
    copytree(inst, tmp)
    run_setup(tmp, where)
    rmtree(tmp)

    # insert correct lib dirs into pythonrc.py
    f = open(path.join(base, 'template', 'venv', 'pythonrc.py'), 'r')
    content = f.read()
    f.close()

    patrn = '# INSERT LIB DIRS HERE'
    libs = '\n'.join(map(lambda x: '    %s' % x, (
        "path.join(base, '%s'), # generated purelib" % get_distutils_schema('')['purelib'][1:],
        "path.join(base, '%s'), # generated platlib" % get_distutils_schema('')['platlib'][1:],
    )))
    content = content.replace(patrn, libs)

    f = open(path.join(where, 'pythonrc.py'), 'w')
    f.write(content)
    f.write('')
    f.close()

