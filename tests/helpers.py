
import os
from os import path
from shutil import rmtree
from unittest import TestCase
from tempfile import mkdtemp

from rvirtualenv.helpers import get_distutils_schema


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

def get_script_path(base):
    return get_distutils_schema(base)['scripts']

