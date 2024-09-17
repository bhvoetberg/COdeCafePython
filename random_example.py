# https://www.youtube.com/watch?v=CnbgMnUCsUM
# 16:05

from random import choice, choices, sample
names: list[str] = ['Bob', 'Sophia', 'Anna', 'George']

winner: str = choice(names)
print(winner)

winners: list[str] = sample(names, k=2)
print(winners)

random_names: list[str] = choices(names, k=2)
print(random_names)

