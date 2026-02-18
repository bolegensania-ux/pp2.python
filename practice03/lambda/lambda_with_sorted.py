# What is sorted?
# sorted() - sorts element of an iterable(list, tuple, etc) without modifying the original list, it sorts the copy of the original list

# basic syntax: sorted(iterable, key = None, reverse = False) key - function that decides how to sort

# usual sorting using sorted():
"""
nums = [1, 2, 3, 4]                                       output: [4, 3, 2, 1]
result = sorted(nums, reverse = True) #descending order
print(result)
"""

# using lambda:
"""
example: sort by the length of the word

words = ["cat", "elephant", "dog"]
result = sorted(words, key = lambda x: len(x))
print(result)

output:
["cat", "dog", "elephant"]
"""

"""
example: sort by the second element in tuples

scores = [("Saniya", 95), ("Alikhan", 89), ("Aruzhan", 90)]
result = sorted(scores, key = lambda x: s[1])
print(results)

output:
[("Alikhan", 89), ("Aruzhan", 90), ("Saniya", 95)]
"""