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


class Dumbo:
    def __init__(self):
        a = 'Naam'


olifant = Dumbo()


def sum_dictionary_values(*args, **kwargs):
    sum = 0
    if len(args) > 0:
        for arg in args:
            if type(arg) in (int, float):
                sum += arg
    if len(kwargs) > 0:
        for key in kwargs:
            if type(kwargs[key]) in (int, float):
                sum += kwargs[key]
    return sum


print(sum_dictionary_values(1, 2, olifant, True, True, 'v', 3.5, a=2, b=3.4, c=5, o={1, 2, 3}, d='d'))
