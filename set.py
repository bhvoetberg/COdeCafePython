#Set: Ongeordend en onveranderlijk, geen duplicaten
set1={1, 2, 3, 4}
set2={1, "rober", False}
set3={4, 5, 6, 7}

print(set2)

#usecase: doublures voorkomen


print(set1.difference(set3))
print(set3.difference(set1))

print(set1.union(set3))

#verwijder een bestaand element
set1.remove(1)
print(set1)

#verwijder een bestaand element of doe niets
set1.discard(2)
set1.discard(10)
print(set1)


