======================================
relocatable python virtual environment
======================================

package inspired a lot by ian bicking's virtualenv_ but created in fashion
that it can be relocated freely through the filesystem, renamed, backuped, ...

.. _virtualenv: http://bitbucket.org/ianb/virtualenv/

second nice feature is, that you can customize your python environment
via ``{{ENV}}/pythonrc.py`` in any curious way you want.

works with python3, pypy

install
-------

you can `install this package from pypi`_::

  pip install RVirtualEnv

  # or
  easy_install RVirtualEnv

  # or just clone this repository
  git clone http://github.com/kvbik/rvirtualenv

you should definitely `try development version`__

.. _install this package from pypi: http://pypi.python.org/pypi/RVirtualEnv

__ development_

to create new virtual environment just call::

  rvirtualenv ~/PYENV1

  # or directly from this repo

  ./rvirtualenv.py ~/PYENV2

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
  c:\PYENV1\bin\python.bat [any [params]]

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

 * archlinux with python 3.2
 * archlinux with python 2.7
 * macosx 10.6 python 2.6
 * ms windows with python 2.6
 * ubuntu 10.04 python 2.6
 * debian lenny with python 2.5
 * debian etch with python 2.4

but there is no build environment yet.

why
---

main reasons why this package came into existence:

 * it does not copy python binary
 * it does not symlink core python libraries
 * you can just set up PYTHONPATH env variable
   and you can use any system-wide command (eg: easy_install, pip)
 * you can tune ``pythonrc.py`` file to your needs
   in any curious ways (useful for debugging/testing)

todo
----

you can use the `issue tracker`__ for more (or in `TODO.rst` in this repo)
but some of the long term goals are here

 * test building and installing some c extension
 * test install tools (``pip``, ``easy_install`` and others)
 * better virtualenv inheritance
   (and handle more virtualenvs defined on ``pythonpath``)

__ https://github.com/kvbik/rvirtualenv/issues

development
-----------

see http://github.com/kvbik/rvirtualenv

changelog
---------

0.3.x
~~~~~

aka branch `releases/rvirtualenv-0.3`__

__ https://github.com/kvbik/rvirtualenv/tree/releases/rvirtualenv-0.3

* system-wide installed rvirtualenv does work and creates virtualenvs correctly
  - there were issues with read only fs for non privileged users

0.3.1
~~~~~

* implemented cmd-line virtualenv compatible options
  (``--no-site-packages``, ``--python``, ``--prompt``)
* no site packages option for pythonrc 
* non python data installed to python package (fixed bug introduced in `0.3.0`_)

0.3.0
~~~~~

* `python3`_ support - it really works, tests are passing
* support for `virtualenv wrapper`_ (via: ``source PY/bin/activate``)
* inherit one virtualenv to another
* ``bin/activate`` works, also on windows and relocatable
* complete rewrite of venv
* custom install command so you can define your own layout
* proper functionality on macos and ubuntu

.. _virtualenv wrapper: http://www.doughellmann.com/projects/virtualenvwrapper/
.. _python3: http://diveintopython3.org/

0.2.x
~~~~~

aka branch `releases/rvirtualenv-0.2`__

__ https://github.com/kvbik/rvirtualenv/tree/releases/rvirtualenv-0.2

* installing extensions into virtual environment works
* not released, but merged to 0.3

0.2.3
~~~~~

* fixing problems with relative path when creating virtualenv
* more compatibility with pip and uninstalling system packages (``sys.real_prefix``)
* tests passing with distribute_ (aka setuptools_ fork)

.. _distribute: http://bitbucket.org/tarek/distribute/
.. _setuptools: http://pypi.python.org/pypi/setuptools

0.2.2
~~~~~

initial versions (<=0.2.2)

