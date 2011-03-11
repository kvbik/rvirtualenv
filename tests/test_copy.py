
import os
from os import path

from tests.helpers import InTempTestCase, store_directory_structure

import rvirtualenv
from rvirtualenv.copy import copy


class TestCopy(InTempTestCase):
    def test_whole_copy(self):
        base = path.dirname(rvirtualenv.__file__)
        venv = path.join(base, 'template', 'venv')
        os.chdir(venv)
        expected = sorted(store_directory_structure('.'))

        copy(self.virtualenv)

        os.chdir(self.virtualenv)
        got = sorted(store_directory_structure('.'))

        self.failUnlessEqual(expected, got)

