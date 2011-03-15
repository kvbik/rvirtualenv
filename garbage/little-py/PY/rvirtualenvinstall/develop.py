import setuptools
from setuptools.command.develop import develop as _develop


class develop(_develop):
    description = "rvirtualenv's %s" % _develop.description
    def run(self):
        print('WTF')

# don't know why isn't it overriden by entry_points
setuptools.command.develop.develop = develop

