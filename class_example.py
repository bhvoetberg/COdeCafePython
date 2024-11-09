class MyQueue:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        self.items.append(item)
        return None

    def dequeue(self) -> None:
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.items[0]


bikes = MyQueue()
bikes.size()
# bikes.peek()
bikes.enqueue('Gazelle')
bikes.enqueue('Batavus')
bikes.enqueue('Union')
bikes.enqueue('Sparta')
print(bikes.size())
slice = bikes.items[::-1]
print(slice)

a, b, c, d = bikes.items
print('a: ' + a)

print('---')
print(bikes.__dir__())


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")

        return self.stack.pop(len(self.stack) - 1)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


print('+++')
stapel = MyStack()
print(stapel.size())
stapel.push("Volvo")
stapel.push("Toyota")
stapel.push("Volkswagen")

print(stapel.peek())
stapel.pop()
print(stapel.peek())

print('+++')
