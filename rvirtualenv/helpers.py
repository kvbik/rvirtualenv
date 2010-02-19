
import sys, os
import string
from distutils.command.install import INSTALL_SCHEMES


def get_scheme_name():
    '''
    simplified logic from distutils.command.install:install.finalize_options
    '''
    if os.name == 'posix':
        return 'unix_prefix'
    return os.name

def get_scheme_replacements(base, py_version=None):
    '''
    returns dictionary for replacement of $base, $py_version_short & so on..
    '''
    if py_version is None:
        py_version = (string.split(sys.version))[0]
    d = dict(
        base=base,
        usersite=base,
        userbase=base,
        platbase=base,
        dist_name='',
        py_version_short=py_version[0:3],
        py_version_nodot=py_version[0]+py_version[2],
    )
    return d

def get_distutils_schema(base, name=None, py_version=None):
    '''
    get install schema with patterns replaced
    '''
    if name is None:
        name = get_scheme_name()
    schema = INSTALL_SCHEMES[name]
    d = get_scheme_replacements(base, py_version)
    r = {}
    for k, v in schema.iteritems():
        t = string.Template(v)
        r[k] = t.safe_substitute(d)
    return r

