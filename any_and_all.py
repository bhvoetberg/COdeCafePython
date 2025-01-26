a = [1, 2, 3, 4, 5]

if all(x > 0 for x in a):
    print("All greater than zero")


b = [True, False, False]

if any(b):
    print("At least one True")

c = [False, False]

if not any(c):
    print("None are True")