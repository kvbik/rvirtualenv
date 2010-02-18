
import os
from os import path

from helpers_in_temp_test import InTempTestCase

import rvirtualenv
from rvirtualenv.generate import generate


class TestGenerate(InTempTestCase):
    def setUp(self):
        super(TestGenerate, self).setUp()
        os.mkdir(self.virtualenv)

    def test_whole_generate(self):
        generate(self.virtualenv)

        pybin = path.join(self.virtualenv, 'bin', 'python.py')
        self.assertTrue(path.exists(pybin))

