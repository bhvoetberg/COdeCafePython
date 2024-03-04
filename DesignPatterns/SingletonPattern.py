from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def print(self):
        pass


class PersonSingleton(IPerson):
    def print(self):
        pass

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("PersonSingleton cannot be initialized")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name} age: {PersonSingleton.__instance.age}")


p = PersonSingleton("Mike", 30)
p.print_data()
p2 = PersonSingleton("Jeff", 45)
p.print_data()