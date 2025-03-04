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


class Dumbo:
    def __init__(self):
        a = 'Naam'


olifant = Dumbo()

print("Dumbo example: ", sum_dictionary_values(1, 2, olifant, True, True, 'v', 3.5, a=2,
                            b=3.4, c=5, o={1, 2, 3}, d='d'))


def my_sum(*numbers) -> int:
    result = 0
    for x in numbers:
        result += x
    return result


print(my_sum(1, 2, 3))


def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

my_list = [1, 2, 3]
print("Mylist")
print(my_list)
print(*my_list)


def my_sum(*args):
    if type(args[0]) == str:
        result = ""
    else:
        result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2))

tupie = ('a', 'b', 'c')
boolie = [False, False, True]
print('tupie', my_sum(*tupie))
print('list3', my_sum(*list3))
print('boolie', my_sum(*boolie))

a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
d = a + b
print('c: ', c)
print('d: ', d)


def combi(*args, **kwargs):
    print('This series:')
    print("args: ", args)
    print("kwargs: ", kwargs)
    return "Done!"


print("Combi")
a = [1, 2, 3]
b = {"a": 1, "b": 2, "c": 3}

q = combi(a)
w = combi(b)
e = combi(a, b)
