import contextlib
import sqlite3
import time

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



@contextlib.contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

with timer():
    total = sum(range(10_000_000))
    print("Total: {total} seconds elapsed")


with sqlite3.connect("context_manager_example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    cursor.execute("INSERT INTO people (name) VALUES (?)", ("Alice",))
    cursor.execute("INSERT INTO people (name) VALUES (?)", ("Bob",))
    conn.commit()
    cursor.execute("SELECT * FROM people")
    print(cursor.fetchall())
    # conn.close() is not necessary in ' with '  context manager!!
    print("Connection closed automatically at end of block")

