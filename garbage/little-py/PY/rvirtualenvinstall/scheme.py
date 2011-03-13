import sys
import site
from distutils.util import subst_vars

INSTALL_SCHEMES = {
    'custom': {
        'purelib': '$base/lib/python/site-packages',
        'platlib': '$base/lib/python$py_version_short/site-packages',
        'headers': '$base/include/python$py_version_short/$dist_name',
        'scripts': '$base/bin',
        'data'   : '$base',
        },
    'unix': {
        'purelib': '$base/lib/python$py_version_short/site-packages',
        'platlib': '$base/lib/python$py_version_short/site-packages',
        'headers': '$base/include/python$py_version_short/$dist_name',
        'scripts': '$base/bin',
        'data'   : '$base',
        },
    'windows': {
        'purelib': '$base/Lib/site-packages',
        'platlib': '$base/Lib/site-packages',
        'headers': '$base/Include/$dist_name',
        'scripts': '$base/Scripts',
        'data'   : '$base',
        },
    'os2': {
        'purelib': '$base/Lib/site-packages',
        'platlib': '$base/Lib/site-packages',
        'headers': '$base/Include/$dist_name',
        'scripts': '$base/Scripts',
        'data'   : '$base',
        },
    'darwin': {
        'purelib': '$base/Library/Python$py_version_short/site-packages',
        'platlib': '$base/Library/Python$py_version_short/site-packages',
        'headers': '$base/Include/$dist_name',
        'scripts': '$base/bin',
        'data'   : '$base',
        },
    }

def get_scheme(platform, what, dist_name='UNKNOWN'):
    replace = {
        'base': sys.prefix,
        'py_version_short': sys.version[:3],
        'dist_name': dist_name,
    }
    line = INSTALL_SCHEMES[platform][what]
    return subst_vars(line, replace)

def add_to_path(new_paths):
    "add dirs to the beginnig of sys.path"
    __plen = len(sys.path)
    for i in new_paths:
        if i not in sys.path:
            site.addsitedir(i)
    new = sys.path[__plen:]
    del sys.path[__plen:]
    p = getattr(sys, '__egginsert', 0)
    sys.path[p:p] = new
    sys.__egginsert = p+len(new)

