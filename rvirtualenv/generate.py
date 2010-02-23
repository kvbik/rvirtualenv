
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
    install = [
        '"%s"' % sys.executable,
        '-c',
        '''"import sys; sys.prefix='%s'; __file__='setup.py'; execfile('setup.py')"''' % prefix,
        'install',
    ]
    install = ' '.join(install)

    oldpath = os.getcwd()
    os.chdir(base)

    shell = sys.platform != 'win32'
    stdout = stderr = PIPE
    p = Popen(install, stdout=stdout, stderr=stderr, shell=shell)
    stdoutdata, stderrdata = p.communicate()

    os.chdir(oldpath)

    return stdoutdata, stdoutdata

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

