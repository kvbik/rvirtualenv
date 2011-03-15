
import os
import sys
from os import path

from rvirtualenv.copy import copy
from rvirtualenv.generate import generate


VERSION = (0, 3, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


def main(argv=None):
    '''
    main call for rvirtualenv command
    '''
    if argv is None:
        argv = sys.argv

    if len(argv) < 2:
        raise NotImplementedError

    venv = path.join(os.getcwd(), argv[1])

    copy(venv)
    generate(venv)

