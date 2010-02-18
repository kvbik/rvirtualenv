
import sys

from rvirtualenv.copy import copy
from rvirtualenv.generate import generate


def main(argv=None):
    '''
    main call for rvirtualenv command
    '''
    if argv is None:
        argv = sys.argv

    if not len(argv):
        raise NotImplementedError

    venv = argv[1]

    copy(venv)
    generate(venv)

