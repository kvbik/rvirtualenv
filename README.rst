======================================
relocatable python virtual environment
======================================

package inspired a lot by ian bicking's virtualenv but created in fashion
that it can be relocated freely through the filesystem.

you can install this package from pypi::

  pip install RVirtualEnv

  # or

  easy_install RVirtualEnv

  # or just clone this repository

to create new virtual environment just call::

  virtualenv ~/PYENV1

  # or directly from this repo

  ./virtualenv.py ~/PYENV2

to enable environment, do::

  # on unix
  export PYTHONPATH=~/PYENV1:$PYTHONPATH

  # on windows
  set PYTHONPATH=c:\PYENV1;%PYTHONPATH%

after that, you can call any python command (eg: ``pip`` or ``easy_install``, ``ipython``, ...)
and it will have access to your virtual environment.

if you don't want to mess up with environment, just call our wrapper::

  # on unix
  ~/PYENV1/bin/python [any [params]]

  # on win
  c:\PYENV1\Scripts\python.bat [any [params]]

it should work with mod-wsgi ``python-path`` option as well,
and you can enable it in runtime via ``site.addsitedir(venv_directory)``.

