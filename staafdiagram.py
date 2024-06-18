import random
import string

print("hallo", end=" ")
print("hallo", end=" ")

lijst = [random.choice(string.ascii_lowercase) for x in range(10000)]

print(lijst)
print(lijst[2])
print(lijst[3])

letterFreq = {}

for x in range(0, 1000):
    if lijst[x] in letterFreq.keys():
        newValue = letterFreq.get(lijst[x]) + 1
        letterFreq.update({lijst[x]: newValue})
    else:
        letterFreq.update({lijst[x]: 1})

print(letterFreq)
sorted_letter_freq = sorted(letterFreq)
print(sorted_letter_freq)

# letterFreq['c'] = 1
# print(letterFreq)
# print(letterFreq.get('c'))
# letterFreq.update({"c": letterFreq.get("c") + 1})
# print(letterFreq)

print(len(letterFreq))
