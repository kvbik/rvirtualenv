from setuptools import setup
from os import path


VERSION = (0, 2, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(path.join(path.dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()


setup(
    name = 'RVirtualEnv',
    description = "relocatable python virtual environment",
    url = "http://github.com/kvbik/rvirtualenv",
    long_description = long_description,
    version = __versionstr__,
    author = "Jakub Vysoky",
    author_email = "jakub@borka.cz",
    license = "BSD",
    packages = ['rvirtualenv'],
    entry_points = {
        'console_scripts': [
            'rvirtualenv = rvirtualenv:main',
        ],  
    },
    zip_safe = False,
    include_package_data = True,
    setup_requires = [
        'setuptools_dummy',
    ],  
    test_suite = "tests.test_all.runtests",
)   

