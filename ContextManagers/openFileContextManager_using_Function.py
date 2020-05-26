"""
Write open file context manager using function
"""
from contextlib import contextmanager

@contextmanager
def file_open(filename, mode):
    global fh
    try:
        fh = open(filename, mode)
        yield fh
    finally:
        fh.close()

with file_open('sample1.txt', 'w') as f:
    f.write('This is new sample file!')

print(f.closed)
