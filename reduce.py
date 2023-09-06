
from functools import reduce

def my_add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]

print(reduce(my_add, numbers, 100))