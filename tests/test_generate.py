
import os
from os import path
import sys

from tests.helpers import InTempTestCase, get_script_path, store_directory_structure

import rvirtualenv
from rvirtualenv.generate import generate, install_venv_keep_package
from rvirtualenv.copy import copy
from rvirtualenv.rvirtualenvinstall.scheme import get_scheme, guess_scheme


class TestGenerate(InTempTestCase):
    def test_whole_generate(self):
        copy(self.virtualenv)
        generate(self.virtualenv)

        pybin = path.join(get_script_path(self.virtualenv), 'python.py')
        self.assertTrue(path.exists(pybin))

        pyrc = path.join(self.virtualenv, 'pythonrc.py')
        self.assertTrue(path.exists(pyrc))

        content = open(pyrc, 'r').read()
        self.assertFalse("scheme = 'custom'" in content)

    def test_whole_generate_scheme(self, layout=None):
        copy(self.virtualenv)
        generate(self.virtualenv, layout=layout)
        structure = store_directory_structure(self.virtualenv, content='<file>')

        if layout is None:
            layout = guess_scheme()

        paths = set((i for i,j in structure))
        self.assertTrue(get_scheme(layout, 'purelib', vars={'base': self.virtualenv}) in paths)
        self.assertTrue(get_scheme(layout, 'scripts', vars={'base': self.virtualenv}) in paths)

