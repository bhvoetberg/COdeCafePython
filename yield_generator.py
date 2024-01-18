def mygenerator(n):
    for x in range(n):
        yield x ** 2


values = mygenerator(5)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))


