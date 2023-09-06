letters = []
for letter in "jurre":
    letters.append(letter)
print(letters)

# vs

letters = [letter for letter in "jurre"]

print(letters)

ascii_ = [str(chr(letter)) for letter in range(97 - 32, 150)]
print(ascii_)

ascii_vowels = [str(chr(letter)) for letter in range(97 - 32, 150) if str(chr(letter)) in 'aeiouAEIOU']
print(ascii_vowels)

# Dictionary comprehension
squares = {i: i * i for i in range(10)}
print(squares)


# walrus operator
import random
def get_weather_data():
    return random.randrange(0, 40)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 28]
print(hot_temps)
