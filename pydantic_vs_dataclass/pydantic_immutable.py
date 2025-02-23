from pydantic import BaseModel

# See pydantic warnings below!


class User(BaseModel):
    name: str
    age: int

    class Config:
        frozen = True  # Makes the model immutable

user = User(name="Alice", age=25)
print(user.name)  # Alice

user.age = 30  # ❌ Raises an error: "User" is immutable


class User2(BaseModel):
    name: str
    _age: int  # Private field

    @property
    def age(self):
        return self._age

    class Config:
        allow_mutation = False  # Prevents changes after creation


user2 = User2(name="Alice", _age=25)
print(user2.age)
user2.age = 22
user2._age = 30  # ❌ Raises error