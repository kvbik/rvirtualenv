======================================
relocatable python virtual environment
======================================

package inspired a lot by ian bicking's virtualenv but created in fashion
that it can be relocated freely through the filesystem.

install
-------

you can install this package from pypi::

  pip install RVirtualEnv

  # or

  easy_install RVirtualEnv

  # or just clone this repository

to create new virtual environment just call::

  virtualenv ~/PYENV1

  # or directly from this repo

  ./virtualenv.py ~/PYENV2

usage
-----

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

tests
-----

if you are interested in testing this package, it should support many standard ways of running tests.
nose is used for test discovery.

you can run any of these commands:

 * ``python setup.py test``
 * ``nosetests``
 * ``./tests/test_all.py``

in the ``setup.py`` case you just have to wait a little, until setuptools_dummy_ are downloaded,
because it is a build dependency.

.. _setuptools_dummy: http://pypi.python.org/pypi/setuptools_dummy/

i tested this package on:

 * archlinux with python 2.6
 * ms windows with python 2.6
 * debian lenny with python 2.5
 * debian etch with python 2.4

i don't have any automated testing set up yet.

