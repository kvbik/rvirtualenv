import sys
from os import path

import rvirtualenvinstall.install
from rvirtualenvinstall import scheme
import pythonrc

base = path.abspath(path.dirname(pythonrc.__file__))

# real_prefix is useful for pip and uninstalling system pkgs
sys.real_prefix = sys.prefix
# python uses this almost everywhere
sys.prefix = base

this_site_packages = [
    scheme.get_scheme(pythonrc.scheme, 'purelib'),
    scheme.get_scheme(pythonrc.scheme, 'platlib'),
]

scheme.add_to_path(this_site_packages)

