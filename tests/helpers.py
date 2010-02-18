
import sys, os
from os import path
from shutil import rmtree, copytree
from unittest import TestCase
from tempfile import mkdtemp
from subprocess import Popen, PIPE


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

