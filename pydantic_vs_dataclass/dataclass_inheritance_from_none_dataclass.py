# When a dataclass inherits from a class that is not a dataclass, you must init the class

from dataclasses import dataclass

class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width


@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)

