# Tuple: ongeordend en onveranderlijk
y = (1, 2, 3, 4)

print(y[2])
print(len(y))

y = ("appel", "konijn", "manderijn", "aardbei", "peer", "peer")
z = ("appel", "konijn", "manderijn", "aardbei", "peer", "peer")

print(' +++')
print(y.__contains__("appel"))
print(y)
print(' +++')

a, b, c, d, e, f = y
print(a, c, b)
print('+++')
print(type(y))
print(y)

print(y.count(f))

# tuple van 1 element
mini_tuple = ("1",)
print(mini_tuple)
print(type(mini_tuple))

# met slicing en reassign wel 'veranderlijk'
y = y[2:-1]  # nieuwe y wordt oorspronkelijke y vanaf index 2 tot voorlaatste element
print(y)



integers = [1, 2, 3]
letters = ["a", "b", "c"]
floats = [4.0, 5.0, 6.0]

for i, l, f in zip(integers, letters, floats):
    a = (i, l, f)
    print(a)
    print(type(a))


print([5, 6, 7] < [5])