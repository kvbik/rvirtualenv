import distutils
from distutils.command import install

class install(install.install):
    description = "hacked - %s" % install.install.description
    def run(self):
        print('WTF')

# monkey patch for distutils
distutils.command.install.install = install

