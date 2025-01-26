todolist = ['a', 'b', 'c', 'd']

for idx, desc in enumerate(todolist):
    print(idx, ' ', desc)

items = ['apple', 'banana', 'cherry', 'cheese']
amount = [10, 20, 30, 40]


for product, amount in zip(items, amount):
    print(f"{product} {amount}")