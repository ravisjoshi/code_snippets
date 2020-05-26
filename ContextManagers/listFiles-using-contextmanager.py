import os
import sys
from contextlib import contextmanager

@contextmanager
def list_file(dir_name):
    global cwd
    try:
        cwd = os.getcwd()
        os.chdir(dir_name)
        yield
    finally:
        os.chdir(cwd)

for _dir in ['../tips-and-ticks', '../ContextManagers', '../WebScraping']:
    with list_file(_dir):
        print(os.listdir())
