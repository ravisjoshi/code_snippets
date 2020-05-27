"""
https://docs.python.org/3/library/itertools.html
"""

from itertools import permutations, combinations

## Permutations example
text = 'abc'
print('Permutations of {} are: '.format(text))
for word in permutations(text):
    print(word, end=' ')

## Combinations example
text = 'abcd'
print('\n\nCombinations of {} are: '.format(text))
for word in combinations(text, 3):
    print(word, end=' ')
