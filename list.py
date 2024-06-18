# List: geordend en veranderlijk
x = [1, 2, 2, 2, 3, 4]
tweedelijst = [5, 6, 7]

print(len(x))

# Laatste element
print(x[-1])

# Voorlaatste element
print(x[-2])

x[2] = 6
print(x)

x[0] = tweedelijst

print(x[0][0])

x.append("Rober")
print(x)
x.insert(3, "Mirjam")
print(x)

x.pop()
print(x)

# haalt eerste entry met getal 2 weg, herhalen indien nodig
x.remove(2)
print(x)

x.remove([5, 6, 7])

x.extend(tweedelijst)
print(x)

# print van tot in lijst
print(x[2:4])
print(x[2:-1])
# print(x[-1])
x.remove('Mirjam')

y = x * 3
print(set(sorted(y)))


# Replace by index method
fruits = ["apple", "banana", "orange", "kiwi", "grape"]
fruits[fruits.index("kiwi")] = "mango"
print(fruits)

# remove and add to front
index = fruits.index("mango")
item = fruits.pop(index)
fruits.insert(0, item)
print(fruits)

fruits1 = ["apple", "banana"]
fruits2 = ["orange", "kiwi", "grape"]
all_fruits = fruits1 + fruits2
print(all_fruits)


print(0.6 + 0.7)