class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender


    @property
    def Name(self):
        return self.__name

    # Python does not support method overloading, hence @Name.setter
    @Name.setter
    def Name(self, value):
        self.__name = value

    @staticmethod
    def mymethod():
        print("mymethod")
        print(self.__name)

    def __repr__(self):
        return f"{self.__name} {self.__age} {self.__gender}"


person = Person('Henk', 4, 'male')

print(person)
person.Name = 'Frits'
person.mymethod()
