from dataclasses import dataclass, field
from encodings.base64_codec import Codec
from typing import ClassVar

@dataclass
# @dataclass can contain optional arguments: @dataclasses.dataclass(order=True)
class User:
    name: str
    email: str
    account_id: int

    sizes: list[str] = field(default_factory=list)

    # a class can contain a class variable - to be used in the class only
    class_var = ClassVar = 100

user: User = User('Rober', 'admin@example.com', '99')
print(user.class_var)


# help(user)

