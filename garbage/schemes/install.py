
import distutils.command.install
import distutils.core
from distutils import command, core

i = command.install.install(core.Distribution())

i.initialize_options()
i.finalize_options()

for a in dir(i):
    if a.startswith('install_'):
        print '%s: %s' % (a, getattr(i, a))

