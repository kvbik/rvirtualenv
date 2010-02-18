
import sys, os
from os import path
import string
from shutil import rmtree, copytree
from unittest import TestCase
from tempfile import mkdtemp
from distutils.command.install import INSTALL_SCHEMES


class InTempTestCase(TestCase):
    def setUp(self):
        # store curr path
        self.oldcwd = os.getcwd()

        # create test dir structure
        self.directory = mkdtemp(prefix='test_rvirtualenv_')

        # new rvirtualenv
        self.virtualenv = path.join(self.directory, 'PY')

    def tearDown(self):
        # go back
        os.chdir(self.oldcwd)

        # dir cleanup
        rmtree(self.directory, True)

def get_scheme_name():
    '''
    logic from distutils.command.install:install.finalize_options
    '''
    if os.name == 'posix':
        return 'unix_prefix'
    return os.name

def get_scheme_replacements(base, py_version=None):
    if py_version is None:
        py_version = (string.split(sys.version))[0]
    d = dict(
        base=base,
        usersite=base,
        userbase=base,
        platbase=base,
        dist_name='',
        py_version_short=py_version[0:3],
        py_version_nodot=py_version[0]+py_version[2],
    )
    return d

def get_script_path(base):
    scheme_line = INSTALL_SCHEMES[get_scheme_name()]['scripts']
    t = string.Template(scheme_line)
    d = get_scheme_replacements(base)
    return t.safe_substitute(d)

