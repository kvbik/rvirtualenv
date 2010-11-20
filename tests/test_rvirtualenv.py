
import sys
import os
from os import path
from subprocess import Popen, PIPE
import textwrap
import logging

from helpers import InTempTestCase, get_script_path

import rvirtualenv
from rvirtualenv import main


class TestRVirtualEnv(InTempTestCase):
    def setUp(self):
        super(TestRVirtualEnv, self).setUp()

        self.python = path.join(get_script_path(self.virtualenv), 'python.py')

    def install_venv_in_isolation(self, virtualenv=None):
        '''
        install rvirtualenv itself, but do it in subprocess,
        because of possible interaction with other imported libraries
        (eg: setuptools and its monkeypatching)
        '''
        if virtualenv is None: virtualenv = self.virtualenv
        cmd = ('''%s -c "import sys; sys.path.insert(0, r'%s'); '''
               '''from rvirtualenv import main; main([None, r'%s'])"''') % \
                (sys.executable, self.base, virtualenv)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('', stdout.strip())
        self.failUnlessEqual('', stderr.strip())

    def install_venv(self):
        argv = [None, self.virtualenv]
        main(argv)

    def run_rvirtualenv_command(self, virtualenv):
        os.chdir(self.directory)
        self.install_venv_in_isolation(virtualenv)

        pythonrc = path.join(virtualenv, 'pythonrc.py')
        self.assertTrue(path.exists(pythonrc))

        python = path.join(get_script_path(virtualenv), 'python.py')
        self.assertTrue(path.exists(python))

    def test_rvirtualenv_command_creates_distdirs_given_absolute(self):
        self.run_rvirtualenv_command(self.virtualenv)

    def test_rvirtualenv_command_creates_distdirs_given_relative(self):
        self.run_rvirtualenv_command('PY')

    def run_command(self, cmd):
        shell = sys.platform != 'win32'
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=shell)
        return map(lambda b: b.decode('ascii'), p.communicate())

    def test_python_itself(self):
        self.install_venv()

        cmd = '%s %s -c "print(128)"' % (sys.executable, self.python)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('128', stdout.strip())

    def test_run_python_script(self):
        self.install_venv()

        script = path.join(self.base, 'tests', 'scripts','print.py')
        cmd = '%s %s %s' % (sys.executable, self.python, script)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual('', stdout)

    def test_run_python_script_with_args(self):
        self.install_venv()

        script = path.join(self.base, 'tests', 'scripts','print.py')
        cmd = '%s %s %s a b c' % (sys.executable, self.python, script)
        stdout, stderr = self.run_command(cmd)
        self.failUnlessEqual("['a', 'b', 'c']", stdout.strip())

    def install_some_way(self, inst_type, inst_command='install'):
        self.install_venv()

        os.chdir(path.join(self.base, 'tests', 'installs',
            'venvtest-%s' % inst_type))
        inst = '%s %s setup.py %s' % \
                (sys.executable, self.python, inst_command)
        stdout, stderr = self.run_command(inst)
        os.chdir(self.oldcwd)

        logging.info('stdout:')
        logging.info(stdout)
        logging.info('stderr:')
        logging.info(stderr)

        self.failUnlessEqual('', stderr)

        cmd = '%s %s -c "import venvtest; print(venvtest.__versionstr__)"' % \
                (sys.executable, self.python)
        stdout, stderr = self.run_command(cmd)
        expected = '0.1.0'
        self.failUnlessEqual(expected, stdout.strip())

        cmd = '%s %s -c "import venvtest; print(venvtest.__file__)"' % \
                (sys.executable, self.python)
        stdout, stderr = self.run_command(cmd)
        a = len(self.virtualenv)
        b = -len('venvtest.pyX')
        env = stdout.strip()[:a]
        mod = stdout.strip()[b:]
        pth = stdout.strip()[a:b]

        logging.info(pth)

        self.failUnlessEqual(self.virtualenv, env)
        # it could be *.py or *.pyc - depending on distro
        self.failUnlessEqual('venvtest.py', mod.strip(r'\c/'))

    def test_install_distutils_way(self):
        self.install_some_way('distutils')

    def test_install_setuptools_way(self):
        '''
        this test should skip if you don't have setuptools
        but other tests could fail too..
        '''
        self.install_some_way('setuptools')

    def activate_command_unix(self):
        activate = 'source PY/bin/activate'
        deactivate = 'deactivate'
        run_command = 'sh run'
        run_file = 'run'
        shebang = '#!/bin/sh'
        self.activate_command(activate, deactivate,
            run_command, run_file, shebang)

    def activate_command_win(self):
        activate = 'call PY\\Scripts\\activate.bat'
        deactivate = 'call deactivate.bat'
        run_command = 'run.bat'
        run_file = 'run.bat'
        shebang = '@echo off'
        self.activate_command(activate, deactivate,
            run_command, run_file, shebang)

    def activate_command(self, activate, deactivate,
            run_command, run_file, shebang):
        os.chdir(self.directory)
        self.install_venv()
        f = open(run_file, 'w')
        f.write(textwrap.dedent('''
            %s
            %s
            python -c "import rvirtualenvkeep; print(rvirtualenvkeep.__file__)"
            %s
        ''' % (shebang, activate, deactivate)).strip())
        f.close()
        stdout, stderr = self.run_command(run_command)
        self.failUnlessEqual(stderr.strip(), '')
        self.assertTrue(stdout.strip().startswith(self.directory))
        self.assertTrue(
            stdout.strip().endswith('rvirtualenvkeep.pyo') or \
            stdout.strip().endswith('rvirtualenvkeep.pyc') or \
            stdout.strip().endswith('rvirtualenvkeep.py')
            )

    def test_activate_command(self):
        if sys.platform == 'win32':
            self.activate_command_win()
        else:
            self.activate_command_unix()

    def something_is_bad_on_win32_and_subprocess(self, py, command=None):
        replace_command = command

        if sys.platform == 'win32':
            name = 'pokus.bat'
            command = name
            bat = ('@echo off', 'pokus.py',)
        else:
            name = 'pokus.sh'
            command = 'sh pokus.sh'
            bat = ('#!/bin/sh', 'python pokus.py',)

        if replace_command is not None:
            command = replace_command

        write = '\n'.join(py)
        f = open('pokus.py', 'w'); f.write(write); f.close()

        write = '\n'.join(bat)
        f = open(name, 'w'); f.write(write); f.close()

        shell = True
        p = Popen(command, stdout=PIPE, stderr=PIPE, shell=shell)
        stdout, stderr = map(lambda b: b.decode('ascii'), p.communicate())
        self.failUnlessEqual('128', stdout.strip())

    def test_something_is_bad_on_win32_and_os_system(self):
        py = ('import os', 'os.system("echo 128")')
        self.something_is_bad_on_win32_and_subprocess(py)

    def test_something_is_bad_on_win32_and_popen(self):
        py = (
            'from subprocess import Popen, PIPE',
            'p = Popen("echo 128", shell=True)',
            'p.communicate()',
        )
        self.something_is_bad_on_win32_and_subprocess(py)

    def test_something_is_bad_on_win32_but_this_works(self):
        py = ('import os', 'os.system("echo 128")')
        #command = 'call pokus.bat' # this doesn't work either
        command = '"%s" pokus.py' % sys.executable
        self.something_is_bad_on_win32_and_subprocess(py, command)

