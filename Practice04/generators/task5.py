# Implement a generator that returns all numbers from (n) down to 0

def ret_val(n):
    i = n
    while i >= 0:
        yield i
        i -= 1

for nums in ret_val(int(input())):
    print(nums)