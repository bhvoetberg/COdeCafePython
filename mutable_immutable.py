# list, set, dict are mutable
x = [1, 2, 3, 4, 5, 6]
y = x

# assigning to a variable results in a reference
x[0] = 9
print(x, y)