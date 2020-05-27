"""
https://docs.python.org/3/library/itertools.html
"""

import itertools

def isEven(num):
    return True if num % 2 == 0 else False


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = itertools.filterfalse(isEven, nums)

print(list(result))
