from itertools import batched, zip_longest

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]

batches = batched(numbers, 3)
try:
    batch = next(batches)
    while batch:
        print(batch)
        batch = next(batches)
except StopIteration:
    print('Exhausted iterator')

names: list[str] = ['John', 'Arrissa', 'Lisa']
numbers: list[int] = ['1', '2', '3', '4', '5']
symbols: list[str] = ['@', '&', '*', '#']

print(list(zip_longest(names, numbers, symbols, fillvalue=False)))


def count_vowels(string: str) -> int | TypeError:
    if type(string) is str:
        vowels = 'aeiouAEIOU'
        return sum(1 for char in string if char in vowels)
    else:
        raise TypeError(f'Input should be a string, got %s' % type(string))


some_string: str = 3
print(type(some_string))
print(count_vowels(some_string))
