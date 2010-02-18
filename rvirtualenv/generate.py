
import os


def generate(where):
    '''
    create dirs and files after virtualenv dir itself is prepared
    '''
    os.chdir(where)
    os.mkdir('bin')

