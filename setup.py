from setuptools import setup
from os import path


VERSION = (0, 3, 1)
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
    test_suite = "tests.test_all.runtests",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)

