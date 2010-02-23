import sys
from distutils.core import setup

scripts = ['bin/python.py']
if sys.platform == 'win32':
    scripts.append('bin/python.bat')
else:
    scripts.append('bin/python')

setup(
    name='rvirtualenvkeep',
    version='0.1',
    py_modules=['rvirtualenvkeep'],
    scripts=scripts,
)


