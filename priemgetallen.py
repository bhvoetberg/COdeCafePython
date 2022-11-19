# zeef van erastothenes

lijst = []
for i in range(2, 30):
    lijst.append(i)
print(lijst)

i = 0
for t in range(2, 30):
    while i < len(lijst):
        if lijst[i] % t == 0:
            lijst.pop(i)
        i += 1
    print(lijst)
