#List: geordend en veranderlijk
x = [1, 2, 2, 2, 3, 4]
tweedelijst = [5, 6, 7]

print(len(x))

#Laatste element
print(x[-1])

#Voorlaatste element
print(x[-2])

x[2]=6
print(x)

x[0] = tweedelijst

print(x[0][0])

x.append("Rober")
print(x)
x.insert(3,"Mirjam")
print(x)

x.pop()
print(x)

#haalt 1 waarde weg, herhalen indien nodig
x.remove(2)
print(x)

x.extend(tweedelijst)
print(x)

#print van tot in lijst
print(x[2:4])
print(x[2:-1])

