from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: float


class ShoppingCart:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def delete_item(self, item: Item) -> None:
        self.items.remove(item)

    def total(self) -> Decimal:
        return sum(item.price for item in self.items)


# Stateless
def calculate_discount(cart: ShoppingCart, discount: Decimal):
    return cart.total() * (1 - discount / 100)


cart = ShoppingCart()
cart.add_item(Item("Apple", 1.5))
cart.add_item(Item("Banana", 0.75))

discounted_price = calculate_discount(cart, 20)
print(f"Discounted total: {discounted_price}")

print(f"Original total: {cart.total()}")
