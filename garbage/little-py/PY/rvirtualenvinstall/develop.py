import setuptools
from setuptools.command import develop

class develop(develop.develop):
    description = "hacked - %s" % develop.develop.description
    def run(self):
        print('WTF')

# don't know why isn't it overriden by entry_points
setuptools.command.develop.develop = develop

