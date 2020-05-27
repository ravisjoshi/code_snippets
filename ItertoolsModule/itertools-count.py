"""
https://docs.python.org/3/library/itertools.html
"""

import itertools

# We can set start value and step
counter = itertools.count(start=11, step=2)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# We can use zip to run till shortest iterable is exhausted
counter = itertools.count()
data = [100, 200, 300, 400, 500]
daily_data = list(zip(counter, data))
print(daily_data)

# We can set start value and step - in float
counter = itertools.count(start=10, step=2.5)
names = ['Ron', 'Harry', 'Tom', 'Eric', 'John']

for key, value in zip(counter, names):
    print('{:4} - {}'.format(key, value))

print(25*'-')

# We can set start value and step - in negative float
counter = itertools.count(start=10, step=-2.5)
names = ['Ron', 'Harry', 'Tom', 'Eric', 'John']

for key, value in zip(counter, names):
    print('{:4} - {}'.format(key, value))