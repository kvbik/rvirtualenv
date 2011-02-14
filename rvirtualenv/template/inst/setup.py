import sys
from distutils.core import setup

scripts = [
    'bin/python.py',
    'bin/activate.py',
]
if sys.platform == 'win32':
    scripts.append('bin/getpythondist.py')
    scripts.append('bin/python.bat')
    scripts.append('bin/activate.bat')
    scripts.append('bin/activate.bat.template')
    scripts.append('bin/deactivate.bat')
    scripts.append('bin/deactivate.bat.template')
else:
    scripts.append('bin/python')
    scripts.append('bin/activate')
    scripts.append('bin/activate.template')

setup(
    name='rvirtualenvkeep',
    version='0.1',
    py_modules=['rvirtualenvkeep'],
    scripts=scripts,
)


