
import os
from os import path

from helpers_in_temp_test import InTempTestCase

from rvirtualenv.copy import copy


class TestCopy(InTempTestCase):
    def test_whole_copy(self):
        copy(self.virtualenv)

        pythonrc = path.join(self.virtualenv, 'pythonrc.py')
        self.assertTrue(path.exists(pythonrc))

