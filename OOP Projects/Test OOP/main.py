#Item tracking software
import csv

class Item():

    pay_rate = 0.8 # The pay grade after 20% discount - CLASS ATTRIBUTE, APPLIES ACROSS ALL INSTANCES
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0 , f"Quantity {quantity} is not greater or equal to zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= .9

    @classmethod
    def instantiate_from_csv(clear):
        with open ("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item["name"],
                price = int(item["price"]),
                quantity = int(item["quantity"])
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"Item('{self.name},{self.price},{self.quantity}')"

print(Item.is_integer(4.0))