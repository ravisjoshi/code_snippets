"""
https://docs.python.org/3/library/itertools.html
"""

import itertools

# Chaining different kind of data
letters = ['a', 'b', 'c', 'd', 'e']
number = [1, 2, 3, 4]
cities = ['Bangalore', 'New York', 'Sydney', 'Paris', 'Tokyo']

combined_data = itertools.chain(letters, number, cities)

for item in combined_data:
    print(item)
