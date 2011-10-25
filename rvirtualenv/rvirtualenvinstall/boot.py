import sys
from os import path

from rvirtualenvinstall import (
    scheme,
    install,
)
import pythonrc


def boot():
    base = path.abspath(path.dirname(pythonrc.__file__))

    # real_prefix is useful for pip and uninstalling system pkgs
    sys.real_prefix = sys.prefix
    # python uses this almost everywhere
    sys.prefix = base

    if not pythonrc.sitepackages:
        sys.path = sys.__rvirtualenv_prev_path

    this_site_packages = [
        scheme.get_scheme(pythonrc.scheme, 'purelib'),
        scheme.get_scheme(pythonrc.scheme, 'platlib'),
    ]

    scheme.add_to_path(getattr(pythonrc, 'extra_paths', []))
    scheme.add_to_path(this_site_packages)

    install.monkeypatch()

