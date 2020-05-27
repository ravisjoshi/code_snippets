"""
https://docs.python.org/3/library/collections.html#collections.Counter

A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts.
"""

from collections import Counter

_string = 'aaaabbccccccdddd'
_count_occurance = Counter(_string)

# Elements as dictionary keys and their counts as dictionary values
print(_count_occurance)

# List elements
print(list(_count_occurance.elements()))

# Find most common element
print(_count_occurance.most_common(1))

# Find top 3 most common elements
print(_count_occurance.most_common(3))
