
import os
from os import path

from helpers_in_temp_test import InTempTestCase

import rvirtualenv
from rvirtualenv.copy import copy


class TestCopy(InTempTestCase):
    def store_directory_structure(self, mypath):
        '''
        recursivelly traverse directory and store it in format:
        (
          (mypath, None),
          (mypath/to, None),
          (mypath/to/dir, None),
          (mypath/to/dir/file.txt, {{ file's content }}),
        )
        '''
        d = {}
        for base, dirs, files in os.walk(mypath):
            d[base] = None
            for i in files:
                fn = path.join(base, i)
                f = open(fn, 'r')
                d[fn] = f.read()
                f.close()
        return d.items()

    def test_whole_copy(self):
        base = path.dirname(rvirtualenv.__file__)
        venv = path.join(base, 'template', 'venv')
        os.chdir(venv)
        expected = sorted(self.store_directory_structure('.'))

        copy(self.virtualenv)

        os.chdir(self.virtualenv)
        got = sorted(self.store_directory_structure('.'))

        self.failUnlessEqual(expected, got)

