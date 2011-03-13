
import os
from os import path
from shutil import copy, rmtree, copytree
import sys
from distutils.core import setup
from subprocess import Popen, PIPE

import rvirtualenv
from rvirtualenv.helpers import get_distutils_schema


def run_setup(base, prefix):
    '''
    install couple of helper modules via distutils
    because it creates its directory (via the correct schema)

    it must be called in subprocess
    because of possible setuptools monkeypatching
    '''
    os.environ['PYTHONPATH'] = prefix
    install = [
        '"%s"' % sys.executable,
        path.join(base, 'setup.py'),
        'install',
    ]
    install = ' '.join(install)

    shell = sys.platform != 'win32'
    stdout = stderr = PIPE
    p = Popen(install, stdout=stdout, stderr=stderr, shell=shell)
    stdoutdata, stderrdata = p.communicate()

    return stdoutdata, stdoutdata

def generate(where, layout=None):
    '''
    create dirs and files after virtualenv dir itself is prepared
    '''
    base = path.dirname(rvirtualenv.__file__)
    inst = path.join(base, 'template', 'inst')

    generate_pythonrc_stuff(where)
    install_venv_keep_package(where, inst)

def install_venv_keep_package(venv_base, install_dir):
    '''
    install setup.py via distutils
    '''
    run_setup(install_dir, venv_base)

def generate_pythonrc_stuff(venv_base):
    '''
    insert correct lib dirs into pythonrc.py
    '''
    # load pythonrc.py file
    base = path.dirname(rvirtualenv.__file__)
    f = open(path.join(base, 'template', 'venv', 'pythonrc.py'), 'r')
    content = f.read()
    f.close()

    # replace pattern in pythonrc.py
    patrn = "scheme = 'custom'"
    repl = "scheme = 'unix'"
    content = content.replace(patrn, repl)

    # write it
    f = open(path.join(venv_base, 'pythonrc.py'), 'w')
    f.write(content)
    f.close()

