import sys
def gen(n):
    for i in range(n):
        yield i**2

g = gen(1000)
value = 10000000

x = [i ** 2 for i in range(value)]
g = gen(value)

for 

# Compare size
print(sys.getsizeof(x))
print(sys.getsizeof(g))