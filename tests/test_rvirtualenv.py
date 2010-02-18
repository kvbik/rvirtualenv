
import os
from os import path

from helpers import InTempTestCase, get_script_path

import rvirtualenv
from rvirtualenv import main


class TestRVirtualEnv(InTempTestCase):
    def test_whole_rvirtualenv_command(self):
        argv = [None, self.virtualenv]
        main(argv)

        pythonrc = path.join(self.virtualenv, 'pythonrc.py')
        pybin = path.join(get_script_path(self.virtualenv), 'python.py')

        self.assertTrue(path.exists(pythonrc))
        self.assertTrue(path.exists(pybin))

