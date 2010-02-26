======================================
relocatable python virtual environment
======================================

package inspired a lot by ian bicking's virtualenv_ but created in fashion
that it can be relocated freely through the filesystem, renamed, backuped, ...

.. _virtualenv: http://bitbucket.org/ianb/virtualenv/

second nice main feature is, that you can customize your python environment
via ``{{ENV}}/pythonrc.py`` in any curious way you want.

install
-------

you can install this package from pypi::

  pip install RVirtualEnv

  # or

  easy_install RVirtualEnv

  # or just clone this repository
  git clone http://github.com/kvbik/rvirtualenv

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

package was tested on:

 * archlinux with python 2.6
 * ms windows with python 2.6
 * debian lenny with python 2.5
 * debian etch with python 2.4

but there is no build environment yet.

why
---

main reasons why this package came into existence::

 * it does not copy python binary
 * it does not symlink core python libraries
 * you can just set up PYTHONPATH env variable
   and you can use any system-wide command (eg: easy_install, pip)
 * you can tune ``pythonrc.py`` file to your needs
   in any curious ways (useful for debugging/testing)

todo
----

it does not have all the features, that ian's virtualenv has,
because i don't know, which one of them are important..

probably ``no-site-packages`` is important and it can be simulated
by patching your ``pythonrc.py`` file right now.

``boot scripts`` even ian does not like very much and i think
there should be some init scripts only or installation of some package should be called.

