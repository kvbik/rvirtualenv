
import os
from os import path
import sys

from tests.helpers import InTempTestCase, get_script_path, store_directory_structure
from tests.sysconfig32 import get_path

import rvirtualenv
from rvirtualenv.generate import generate, install_venv_keep_package


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

    def test_whole_generate_scheme(self, layout=None):
        generate(self.virtualenv, layout=layout)
        structure = store_directory_structure(self.virtualenv, content='<file>')

        paths = set((i for i,j in structure))
        self.assertTrue(get_path('stdlib', vars={'base': self.virtualenv}) in paths)
        self.assertTrue(get_path('scripts', vars={'base': self.virtualenv}) in paths)

    def test_install_venv_keep_package(self):
        inst = path.join(self.base, 'rvirtualenv', 'template', 'inst')
        install_venv_keep_package(self.virtualenv, inst, keep=True)

        l = os.listdir(self.virtualenv)
        self.assertTrue(len(l) > 1)

