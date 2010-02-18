
import os
from os import path

from helpers_in_temp_test import InTempTestCase

from rvirtualenv.generate import generate


class TestGenerate(InTempTestCase):
    def setUp(self):
        super(TestGenerate, self).setUp()
        os.mkdir(self.virtualenv)

    def test_whole_generate(self):
        generate(self.virtualenv)

        pydir = path.join(self.virtualenv, 'bin')
        self.assertTrue(path.exists(pydir))

