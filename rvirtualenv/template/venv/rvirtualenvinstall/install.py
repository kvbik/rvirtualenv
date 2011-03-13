import distutils
from distutils.command.install import install as _install

import pythonrc
from rvirtualenvinstall import scheme


class install(_install):
    description = "rvirtualenv's %s" % _install.description
    def finalize_options(self):
        _install.finalize_options(self)

        self.install_purelib = scheme.get_scheme(pythonrc.scheme, 'purelib')
        self.install_platlib = scheme.get_scheme(pythonrc.scheme, 'purelib')
        self.install_headers = scheme.get_scheme(pythonrc.scheme, 'headers', self.distribution.get_name())
        self.install_scripts = scheme.get_scheme(pythonrc.scheme, 'scripts')
        self.install_data = scheme.get_scheme(pythonrc.scheme, 'data')

        if self.distribution.ext_modules: # has extensions: non-pure
            self.install_lib = self.install_platlib
        else:
            self.install_lib = self.install_purelib

# monkey patch for distutils
distutils.command.install.install = install

