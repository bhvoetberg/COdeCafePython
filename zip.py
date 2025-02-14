a = [1, 2, 3, 4, 5, 6]
b = [3, 4, 5, 6]

c = list(zip(a, b))

print(c)

if all(x < y for x, y in c):
    print("All increasing")
else:
    print("Not all increasing")