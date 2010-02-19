
import os
from os import path

from helpers import InTempTestCase, get_script_path

import rvirtualenv
from rvirtualenv.generate import generate


class TestGenerate(InTempTestCase):
    def setUp(self):
        super(TestGenerate, self).setUp()
        os.mkdir(self.virtualenv)

    def test_whole_generate(self):
        generate(self.virtualenv)

        pybin = path.join(get_script_path(self.virtualenv), 'python.py')
        self.assertTrue(path.exists(pybin))

        pyrc = path.join(self.virtualenv, 'pythonrc.py')
        self.assertTrue(path.exists(pyrc))

        content = open(pyrc, 'r').read()
        self.assertFalse('# INSERT LIB DIRS HERE' in content)

