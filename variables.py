x = 1

print(type(x))


print("hallo" +str(x))

#Sinds Python 3.8?
print(f"Hallo {x}")
# vs
print("Hallo {x}")

#input is always string
age = input("What age? ")
print(f"Next year {int(age) + 1}")


first = float(input("Eerste cijfer"))
second = float(input("Tweede cijfer"))
third = float(input("Derde cijfer"))
fourth = float(input("Vierde cijfer"))

average = (first + second + third + fourth)/4

print(f"Gemiddeld: {average}")
