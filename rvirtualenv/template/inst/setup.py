import sys
from distutils.core import setup

scripts = (
    'bin/python.py',
    'bin/activate.py',
)

if sys.platform == 'win32':
    scripts += (
        'bin/getpythondist.py',
        'bin/python.bat',
        'bin/activate.bat',
        'bin/activate.bat.template',
        'bin/deactivate.bat',
        'bin/deactivate.bat.template',
    )
else:
    scripts += (
        'bin/python',
        'bin/activate',
        'bin/activate.template',
    )

setup(
    name='rvirtualenvkeep',
    version='0.1',
    py_modules=['rvirtualenvkeep'],
    scripts=scripts,
)

