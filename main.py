# Single line comment

"""
Multi line comment
Multi line comment
"""

x = 1
print(x)

x += 1

print(x)

x = "Word"

print(x)


def proces_numbers(numbers: list[int]) -> list[int]:
    return [number + 1 for number in numbers]
