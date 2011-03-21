
import os
from os import path
import sys
from subprocess import Popen, PIPE

import rvirtualenv
from rvirtualenv.rvirtualenvinstall.scheme import guess_scheme


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

def generate(where, layout=None, sitepackages=True, prompt=None):
    '''
    create dirs and files after virtualenv dir itself is prepared
    '''
    base = path.dirname(rvirtualenv.__file__)
    inst = path.join(base, 'template', 'inst')

    generate_pythonrc_stuff(where, layout, sitepackages, prompt)
    install_venv_keep_package(where, inst)

def install_venv_keep_package(venv_base, install_dir):
    '''
    install setup.py via distutils
    '''
    run_setup(install_dir, venv_base)

def generate_pythonrc_stuff(venv_base, layout, sitepackages, prompt):
    '''
    insert correct lib dirs into pythonrc.py
    '''
    # load pythonrc.py file
    base = path.dirname(rvirtualenv.__file__)
    f = open(path.join(base, 'template', 'venv', 'pythonrc.py'), 'r')
    content = f.read()
    f.close()

    if layout is None:
        layout = guess_scheme()

    # replace pattern in pythonrc.py
    patrn = "scheme = 'custom'"
    repl = "scheme = '%s'" % layout
    content = content.replace(patrn, repl)

    # update no-site-packages option
    patrn = "sitepackages = True"
    repl = "sitepackages = %s" % sitepackages
    content = content.replace(patrn, repl)

    # set custom prompt
    patrn = "#prompt = '[CUSTOM]' # set your custom prompt prefix (see -p option)"
    repl = "prompt = %r" % prompt
    if prompt is not None:
        content = content.replace(patrn, repl)

    # write it
    f = open(path.join(venv_base, 'pythonrc.py'), 'w')
    f.write(content)
    f.close()

