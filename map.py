s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))


def double(value):
    return value * 2


t = [5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(map(double, t)))
