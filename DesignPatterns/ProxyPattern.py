from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def person_method(self):
        pass


class Person(IPerson):
    def person_method(self):
        print("person_method")


class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("proxy functionality")
        self.person.person_method()


p1 = Person()
p1.person_method()
p2 = ProxyPerson()
p2.person_method()
