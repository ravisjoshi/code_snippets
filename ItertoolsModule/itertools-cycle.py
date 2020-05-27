"""
https://docs.python.org/3/library/itertools.html
"""

import itertools


counter = itertools.cycle([1, 2, 3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


counter = itertools.cycle(['On', 'Off'])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))