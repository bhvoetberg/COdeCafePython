class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender


    @property
    def name(self):
        return self.__name

    # Python does not support method overloading, hence @name.setter
    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def mymethod(self: object) -> object:
        print("mymethod")
        print(self.__name)

    def __repr__(self):
        return f"{self.__name} {self.__age} {self.__gender}"


person = Person('Henk', 4, 'male')

print(person)
person.name = 'Frits'
person.mymethod()
