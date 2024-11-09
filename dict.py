# Dictionary: geordend en veranderlijk, geen duplicaten (sleutel)
# key: value
d = {'a': 1, 'b': 2, 'c': 3}

print(d.values())
print(d.keys())
print(d['a'])

# lege dictionary
d1 = {}
d2 = dict()

print(type(d2))
print(d.get("b"))

# get kan ook gebruikt worden als de key niet bestaat
print(d.get('e'))

print('b' in d.keys())
print('b' in d)
print(2 in d.values())