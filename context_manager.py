import contextlib

file = open("file.txt", "w")
try:
    file.write("hello")
finally:
    file.close()

# Is equal to:

with open("file.txt", "w") as file:
    file.write("hello")


# Make your own context manager

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("enter")
        return self.file

    def __exit__(self, type, value, trace):
        print("exit")
        self.file.close()


class Dog:
    def __init__(self, dogname):
        self.name = dogname

    def __enter__(self):
        print(f"This is dog {self.name}")

    def __exit__(self, type, value, trace):
        print(f"{self.name} says woof")
        return True


dog = Dog("Rufus")
print(dog.name)

with File("file.txt", "w") as file:
    print("middle")
    file.write("hello")


@contextlib.contextmanager
def file(filename, method):
    print("enter")
    file = open(filename, method)
    yield file
    file.close()
    print("exit")


with file("text.txt", "w") as file:
    print("middle")
    file.write("hello")
