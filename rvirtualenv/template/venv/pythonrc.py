# main virtual env conf file
# activation of this venv is done here

import sys
from os import path
import site

base = path.abspath(path.dirname(__file__))

# python uses this almost everywhere
sys.prefix = base

# add default python lib dirs, to the beggining of sys.path
this_site_packages = [
# INSERT LIB DIRS HERE
]

for i in reversed(this_site_packages):
    if i not in sys.path:
        site.addsitedir(i)

