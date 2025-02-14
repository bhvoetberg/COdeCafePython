from itertools import groupby
from typing import Any, Iterator

numbers: list[list[int]] = [[1], [2,3,4], [5,6], [6,7,8], [9]]
sorted_numbers: list[list[int]] = sorted(numbers, key=len)
grouped_numbers: groupby = groupby(sorted_numbers, key=len)

for length, group in grouped_numbers:
    print(f'{length}, {list(group)}')

words: list[str] = ['Cat', 'Cougar', 'Dog', 'Cow', 'Mouse', 'Bear', 'Snake', 'Eagle', 'Frog', 'Giraffe', 'Chimpansee', ]
grouped_words: groupby = groupby(sorted(words), key = lambda s: s[0])

for letter, group in grouped_words:
    print(f"Starts with '{letter}': {list(group)}")