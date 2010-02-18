
import sys
import os
from os import path
from subprocess import Popen, PIPE

from helpers import InTempTestCase, get_script_path

import rvirtualenv
from rvirtualenv import main



class TestRVirtualEnv(InTempTestCase):
    def setUp(self):
        super(TestRVirtualEnv, self).setUp()

        self.python = path.join(get_script_path(self.virtualenv), 'python.py')

    def install_venv(self):
        argv = [None, self.virtualenv]
        main(argv)

    def test_whole_rvirtualenv_command(self):
        self.install_venv()

        pythonrc = path.join(self.virtualenv, 'pythonrc.py')

        self.assertTrue(path.exists(pythonrc))
        self.assertTrue(path.exists(self.python))

    def run_command(self, cmd):
        shell = sys.platform != 'win32'
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=shell)
        return p.communicate()

    def test_python_itself(self):
        self.install_venv()

        cmd = '%s %s -c "print 128"' % (sys.executable, self.python)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('128', stdout.strip())

    def test_run_python_script(self):
        self.install_venv()

        script = path.join(self.oldcwd, 'tests', 'scripts','print.py')
        cmd = '%s %s %s' % (sys.executable, self.python, script)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('', stdout)

    def test_run_python_script_with_args(self):
        self.install_venv()

        script = path.join(self.oldcwd, 'tests', 'scripts','print.py')
        cmd = '%s %s %s a b c' % (sys.executable, self.python, script)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual("['a', 'b', 'c']", stdout.strip())

    def install_some_way(self, inst_type, inst_command='install'):
        self.install_venv()

        os.chdir(path.join(self.oldcwd, 'tests', 'installs', 'venvtest-%s' % inst_type))
        inst = '%s %s setup.py %s' % (sys.executable, self.python, inst_command)
        stdout, stderr = self.run_command(inst)
        os.chdir(self.oldcwd)

        print 'stdout:'
        print stdout
        print 'stderr:'
        print stderr

        self.failUnlessEqual('', stderr)

        cmd = '%s %s -c "import venvtest; print venvtest.__versionstr__"' % (sys.executable, self.python)
        stdout, stderr = self.run_command(cmd)
        expected = '0.1.0'
        self.failUnlessEqual(expected, stdout.strip())

        cmd = '%s %s -c "import venvtest; print venvtest.__file__"' % (sys.executable, self.python)
        stdout, stderr = self.run_command(cmd)
        a = len(self.virtualenv)
        b = -len('venvtest.pyc')
        env = stdout.strip()[:a]
        mod = stdout.strip()[b:]
        pth = stdout.strip()[a:b]

        print pth

        self.failUnlessEqual(self.virtualenv, env)
        self.failUnlessEqual('venvtest.pyc', mod)

    def test_install_distutils_way(self):
        self.install_some_way('distutils')

    def test_install_setuptools_way(self):
        self.install_some_way('setuptools')

