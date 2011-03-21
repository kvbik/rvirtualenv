
import os
import sys
from os import path
from optparse import OptionParser

from rvirtualenv.copy import copy
from rvirtualenv.generate import generate


VERSION = (0, 3, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


def get_parser():
    parser = OptionParser(usage="%prog [OPTIONS] DEST_DIR")
    parser.add_option(
        '--no-site-packages', dest='sitepackages', action='store_false', default=True,
        help="Don't give access to the global site-packages dir to the virtual environment"
    )
    '''
    # not implemented yet
    parser.add_option( # call different main()
        '-p', '--python', dest='python', metavar='PYTHON_EXE', default=sys.executable,
        help='The Python interpreter to use, e.g., --python=python2.5 will use the python2.5 '
        'interpreter to create the new environment.  The default is the interpreter that '
        'virtualenv was installed with (%s)' % sys.executable
    )
    parser.add_option( # pythonrc.py a volat activate.py jinak
        '--prompt=', dest='prompt',
        help='Provides an alternative prompt prefix for this environment'
    )
    '''
    return parser

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

    venv = path.join(os.getcwd(), name[0])

    copy(venv)
    generate(venv, sitepackages=options.sitepackages)

