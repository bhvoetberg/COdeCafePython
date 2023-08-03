def my_sum(*integers):
    result = 0
    for x in integers:
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
print(my_sum(*tupie))
print(my_sum(*list3))
print(my_sum(*boolie))


