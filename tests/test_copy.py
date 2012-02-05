
import os
from os import path

from tests.helpers import InTempTestCase, store_directory_structure

import rvirtualenv
from rvirtualenv.copy import copy, ignore


class TestCopy(InTempTestCase):
    def test_ignore(self):
        names = [
            'abc.txt',
            'koko/koko.pyc',
            'keke/__pycache__',
            'def.py',
        ]
        expected = set([
            'koko/koko.pyc',
            'keke/__pycache__',
        ])
        self.failUnlessEqual(expected, ignore(None, names))

    def test_whole_copy(self):
        base = path.dirname(rvirtualenv.__file__)

        os.chdir(path.join(base, 'template', 'venv'))
        a = list(store_directory_structure('.'))

        os.chdir(base)
        b = store_directory_structure('.')
        # filter only rvirtualenvinstall
        b = [ i for i in b if 'rvirtualenvinstall' in i[0] ]
        # extract not wanted
        b = [ i for i in b if 'template' not in i[0] ]

        os.chdir(path.join(base, 'template'))
        c = store_directory_structure('.')
        patrn = path.join('.', 'inst')
        repl = path.join('.', 'src', 'rvirtualenvkeep')
        c = [ (i.replace(patrn, repl),j) for (i,j) in c if patrn in i ]

        d = [(path.join('.', 'src'), None)]

        expected = sorted(a+b+c+d)
        # extract not wanted - aka those that are ignored
        expected = [ i for i in expected if '__pycache__' not in i[0] ]
        expected = [ i for i in expected if not i[0].endswith('pyc') ]

        copy(self.virtualenv)

        os.chdir(self.virtualenv)
        x = store_directory_structure('.')
        x = [ i for i in x if '__pycache__' not in i[0] ]
        got = sorted(x)

        self.failUnlessEqual([i for (i,j) in expected], [i for (i,j) in got])
        self.failUnlessEqual(expected, got)

