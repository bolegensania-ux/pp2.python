# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_num(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i

for num in even_num(int(input())):
    print(num, end=", ")