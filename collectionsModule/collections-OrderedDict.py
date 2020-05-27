"""
https://docs.python.org/3/library/collections.html#collections.OrderedDict

Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations.
They have become less important now that the built-in dict class gained the ability to remember insertion order (this new behavior became guaranteed in Python 3.7).
"""

from collections import OrderedDict

o_dict = OrderedDict()
colors = ['White', 'Red', 'Green', 'Blue', 'Yellow', 'Pink', 'Black']

# Remembers in which order the items were inserted
for index, color in enumerate(colors):
    o_dict.update({color: index})

print(o_dict)

# The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
# The pairs are returned in LIFO order if last is true or FIFO order if false.

# print(o_dict.popitem())
# print(o_dict.popitem(last=False))

## If we want to add an item to Ordered Dict
new_val = {'Violet': 7}
o_dict.update(new_val)
print(o_dict)

# If we want to add new items to Ordered Dict
new_colors = ['Crimson', 'Grey', 'Orange', 'Magenta']
for index, color in enumerate(new_colors, start=8):
    o_dict.update({color: index})

print(o_dict)

# If we read something and want to move it to last or starting - LRU algorithm
# Like we read Yellow color - we need to move it to last
o_dict.move_to_end('Yellow')
print(o_dict)

# Like we read Blue color - we need to move it to start
o_dict.move_to_end('Yellow', last=False)
print(o_dict)

