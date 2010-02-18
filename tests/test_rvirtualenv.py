
import os
from os import path

from helpers_in_temp_test import InTempTestCase

from rvirtualenv import main


class TestRVirtualEnv(InTempTestCase):
    def test_whole_rvirtualenv_command(self):
        argv = [None, self.virtualenv]
        main(argv)

        pythonrc = path.join(self.virtualenv, 'pythonrc.py')
        pybin = path.join(self.virtualenv, 'bin', 'python.py')

        self.assertTrue(path.exists(pythonrc))
        self.assertTrue(path.exists(pybin))

