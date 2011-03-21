
import os
import sys
from os import path
from optparse import OptionParser
from subprocess import Popen

import rvirtualenv
from rvirtualenv.copy import copy
from rvirtualenv.generate import generate


VERSION = (0, 3, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


def get_parser():
    '''
    options parser
    '''
    parser = OptionParser(usage="%prog [OPTIONS] DEST_DIR")
    parser.add_option(
        '--no-site-packages', dest='sitepackages', action='store_false', default=True,
        help="Don't give access to the global site-packages dir to the virtual environment"
    )
    parser.add_option(
        '-p', '--python', dest='python', metavar='PYTHON_EXE', default=sys.executable,
        help='The Python interpreter to use, e.g., --python=python2.5 will use the python2.5 '
        'interpreter to create the new environment.  The default is the interpreter that '
        'virtualenv was installed with (%s)' % sys.executable
    )
    '''
    # not implemented yet
    parser.add_option( # pythonrc.py a volat activate.py jinak
        '--prompt=', dest='prompt',
        help='Provides an alternative prompt prefix for this environment'
    )
    '''
    return parser

def get_base():
    '''
    path to rvirtualenv
    '''
    return path.abspath(path.join(path.dirname(rvirtualenv.__file__), path.pardir))

def create_subprocess(python, venv, sitepackages):
    '''
    install rvirtualenv with given interpreter
    '''
    cmd = ('''%s -c "import sys; sys.path.insert(0, r'%s'); '''
           '''from rvirtualenv import create; create(r'%s', %s)"''') % \
            (python, get_base(), venv, sitepackages)
    shell = sys.platform != 'win32'
    p = Popen(cmd, shell=shell)
    return os.waitpid(p.pid, 0)[1]

def create(name, sitepackages):
    '''
    create rvirtualenv
    '''
    venv = path.join(os.getcwd(), name)
    copy(venv)
    generate(venv, sitepackages=sitepackages)

def main(argv=None):
    '''
    main call for rvirtualenv command
    '''
    if argv is None:
        argv = sys.argv

    parser = get_parser()
    options, name = parser.parse_args(argv[1:])

    if len(name) != 1:
        parser.print_help()
        parser.exit('Invalid parameter count.')

    create_subprocess(options.python, name[0], options.sitepackages)

