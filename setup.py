from setuptools import setup


VERSION = (0, 2, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


setup(
    name = 'RVirtualEnv',
    description = "relocatable python virtual environment",
    url = "http://github.com/kvbik/rvirtualenv",
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

