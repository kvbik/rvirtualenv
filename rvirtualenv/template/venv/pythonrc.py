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
    path.join(base, 'lib', 'python%s' % sys.version[:3], 'site-packages') # TODO: not everywhere the same
]
for i in this_site_packages:
    site.addsitedir(i)

