
from os import path

from tests.helpers import InTempTestCase, store_directory_structure

import rvirtualenv
from rvirtualenv.generate import generate
from rvirtualenv.copy import copy
from rvirtualenv.rvirtualenvinstall.scheme import get_scheme, guess_scheme


class TestGenerate(InTempTestCase):
    def test_whole_generate(self, layout=None):
        copy(self.virtualenv)
        generate(self.virtualenv, layout=layout)
        structure = store_directory_structure(self.virtualenv, content='<file>')

        if layout is None:
            layout = guess_scheme()

        paths = set((i for i,j in structure))
        vars = {'base': self.virtualenv}
        self.assertTrue(get_scheme(layout, 'purelib', vars=vars) in paths)
        self.assertTrue(get_scheme(layout, 'scripts', vars=vars) in paths)

        pybin = path.join(get_scheme(layout, 'scripts', vars=vars), 'python.py')
        self.assertTrue(path.exists(pybin))

        pyrc = path.join(self.virtualenv, 'pythonrc.py')
        self.assertTrue(path.exists(pyrc))

        content = open(pyrc, 'r').read()
        self.assertFalse("scheme = 'custom'" in content)

