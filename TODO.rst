
some more todos
---------------

 * do not fork so many processes, try to exec script in python
   something like ``python -c '__file__="neco.py"; execfile("neco.py")'`` (eg in ``pip/req.py``)

 * find the difference between pip installed and setup.py installed rvirtualenv -
   - all the \*.py files are executable in the second case on debian etch
   probably some distribute (setuptools fork) behaviour

 * add logging

 * clean up ``run_command`` (in ``rvirtualenv``, ``tests.test_rvirtualenv``)
   and use it for ``rvirtualenv.generate.run_setup``

 * once ``distutils.install`` command is monkey-patched,
   do the same for ``setuptools.develop``

 * run_command cleanup and tests
   test run_command
   use run_command from rvirtualenv in tests
   generate.run_setup VS run_command

 * use os.pathsep variable in python.py

 * virtualenv inheritance
   if you create one venv inside another it should take precedence
   not ready yet, try::

     ./rvirtualenv.py PY1
     source PY1/bin/activate
     ./rvirtualenv.py PY2
     ./PY2/bin/python -c "import rvirtualenvkeep; print(rvirtualenvkeep.__file__)"

   it should return rvirtualenvkeep from PY2
   .. i repaired this one, but sys.path is ugly sometimes now..

 * investigate and improve site.py execution

