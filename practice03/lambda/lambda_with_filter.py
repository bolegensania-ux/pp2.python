# filter() is used to select elements from iterables (lists, tuples, etc) based on a condition, for which function returns True

# Basic syntax:

# filter(function, iterable)

"""
Example:

keep even numbers:

num = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
"""
"""
Explanation:

lambda x: x % 2 == 0

If True → keep the number

If False → remove it

Output:

[2, 4, 6]
"""
"""
Example with strings:

animals = ["cat", "elephant", "dog", "tiger"]
result = list(filter(lambda x: len(x) > 4, animals))
print(result)
"""

# the lambda inside a filter():
# must return true or false;
# if true -> element stays
# if false -> element disappears