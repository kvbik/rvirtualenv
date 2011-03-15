
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
        a = list(store_directory_structure('.'))
        rvirtinst = base
        os.chdir(rvirtinst)
        b = store_directory_structure('.')
        b = [ i for i in b if 'rvirtualenvinstall' in i[0] ]
        b = [ i for i in b if '__pycache__' not in i[0] ]
        b = [ i for i in b if 'template' not in i[0] ]
        expected = sorted(a+b)

        copy(self.virtualenv)

        os.chdir(self.virtualenv)
        c = store_directory_structure('.')
        c = [ i for i in c if '__pycache__' not in i[0] ]
        got = sorted(c)

        self.failUnlessEqual(expected, got)

