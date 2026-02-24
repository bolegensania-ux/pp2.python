# Create a generator that generates the squares of numbers up to some number N.

def square_of_nums(N):
    i = 1
    while i <= N:
        yield i ** 2
        i += 1

for num in square_of_nums(5):
    print(num)


"""
def square_of_nums(N):
    for i in range(1, N+1):
        yield i**2

for num in square_of_nums(5):
    print(num)
"""