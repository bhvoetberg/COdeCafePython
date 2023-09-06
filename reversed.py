
# reversed() is lazy, change during process will be reflected
numbers = [1, 2, 3]

reversed_numbers = reversed(numbers)
print(next(reversed_numbers))
numbers[1] = 222
print(next(reversed_numbers))
print(next(reversed_numbers))



# *.reverse() reverses the original object

digits = [1, 2, 3, 4]
print(digits)
print(id(digits))

reversed_digits = digits.reverse()
print(reversed_digits)
print(digits)
print(id(digits))