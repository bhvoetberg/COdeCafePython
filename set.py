# Set: Geordend en veranderlijk, geen duplicaten
set1 = {2, 1, 4, 3}
set2 = {1, "rober", False}
set3 = {6, 5, 4, 7}
set3.add(9)
set3.add(8)
set3.
print('+++')
print(set3)
print('+++')

print(set2)

# use case: doublures voorkomen


print(set1.difference(set3))
print(set3.difference(set1))

print(set1.union(set3))

# verwijder een bestaand element
set1.remove(1)
print(set1)

# verwijder een bestaand element of doe niets
set1.discard(2)
set1.discard(10)
print(set1)
