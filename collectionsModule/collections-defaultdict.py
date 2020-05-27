"""
https://docs.python.org/3/library/collections.html

Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class.
It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class.

The first argument provides the initial value for the default_factory attribute; it defaults to None.
All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
"""

from collections import defaultdict

## Example 1

_dict1 = defaultdict(list)
_dict1['a'] = 1
_dict1['b'] = 2

# Will return default value of list
print(_dict1['c'])


## Example 2
_dict2 = defaultdict(int)
_dict2['Red']  = 1
_dict2['Blue'] = 2

# Will return default value of int
print(_dict2['Green'])


## Example 3
_dict3 = defaultdict(dict)
_dict3['Paris'] = 1
_dict3['Tokyo'] = 2
_dict3['Peru']  = 3


# Will return default value of dict
print(_dict3['Green'])







