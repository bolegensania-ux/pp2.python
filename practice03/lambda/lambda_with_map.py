# What is map()?
# map() is used to apply a function to the every element in an iterable(list, tuple, etc)
# unlike filter(), map() does not remove elements, it transforms them 

# basic syntax: map(function, iterable)
# when using the map() functuion, we usually convert it to a list. list(map(...))

"""
Example:

nums = [1, 2, 3, 4]
res = list(map(lambda x: x * 2, nums))
print(res)
"""