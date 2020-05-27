"""
https://docs.python.org/3/library/itertools.html
"""

import itertools

# It will repeat the specified value times=x time
counter = itertools.repeat(2, times=5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))

counter = itertools.repeat(2, times=5)
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))
