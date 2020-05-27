"""
https://docs.python.org/3/library/itertools.html
"""

import itertools

print('itertools.islice(iterable, stop)')
for num in itertools.islice(range(10), 5):
    print(num)

print('\nitertools.islice(iterable, start, stop)')
for num in itertools.islice(range(10), 2, 7):
    print(num)

print('\nitertools.islice(iterable, start, stop, step)')
for num in itertools.islice(range(10), 2, 7, 2):
    print(num)

# Slice specific section from an iterable
with open('sample.txt', 'r') as fh:
    file_content = itertools.islice(fh, 3, 10, 2)  ## itertools.islice(iterable, start, end, step)
    for line in file_content:
        print(line, end='')
