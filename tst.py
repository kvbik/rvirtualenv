
# poor man's nosetests

import unittest

r = unittest.TextTestRunner()
l = unittest.TestLoader()

m = [
    'tests.test_copy',
    'tests.test_generate',
    'tests.test_rvirtualenv',
]

r.run(l.loadTestsFromNames(m))

