#!/usr/bin/env python

import sys
from os import path

def get_prompt(vname_path, vname):
    sys.path.insert(0, vname_path)
    import pythonrc
    prompt = getattr(pythonrc, 'prompt', '(%s)' % vname)
    return prompt

def get_subst_values():
    base = path.dirname(__file__)
    vname_path = path.abspath(path.join(base, path.pardir))
    vname = path.split(vname_path)[-1]
    bin_path = path.split(base)[-1]
    prompt = get_prompt(vname_path, vname)
    return {
        '__VIRTUAL_PROMPT__': prompt,
        '__VIRTUAL_WINPROMPT__': prompt, 
        '__VIRTUAL_ENV__': vname_path,
        '__VIRTUAL_NAME__': vname,
        '__BIN_NAME__': bin_path,
    }

def generate(ftemplt, foutput):
    ftemplt = open(ftemplt, 'r').read()
    for k, v in get_subst_values().items():
        ftemplt = ftemplt.replace(k, v)
    f = open(foutput, 'w')
    f.write(ftemplt)
    f.close()

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 3:
        raise NotImplementedError
    generate(argv[1], argv[2])

if __name__ == '__main__':
    main()

