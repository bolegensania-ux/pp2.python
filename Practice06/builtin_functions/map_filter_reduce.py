# map exercise

nums = list(map(int, input().split()))

res = list(map(lambda x: x**3, nums))
print(res)

# filter exercise

lst = list(map(int, input().split()))

result = list(filter(lambda x: x % 2 == 0, lst))
print(result)

# reduce exercise

from functools import reduce
s = list(map(int, input().split()))
r = reduce(lambda x, y: x * y, s)
print(r)