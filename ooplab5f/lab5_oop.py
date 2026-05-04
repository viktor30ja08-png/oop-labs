

class Toy:

    def __init__(self, name: str, price: float, min_age: int, max_age: int):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if min_age < 0 or max_age < min_age:
            raise ValueError("Invalid age range.")

        self.name = name
        self.price = price
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return f"{self.__class__.__name__}: '{self.name}' | Price: ${self.price:.2f} | Ages: {self.min_age}-{self.max_age}"


class Car(Toy):

    def __init__(self, name: str, price: float, min_age: int, max_age: int, size: str):
        super().__init__(name, price, min_age, max_age)
        valid_sizes = ["small", "medium", "large"]
        if size.lower() not in valid_sizes:
            raise ValueError("Car size must be 'small', 'medium', or 'large'.")
        self.size = size.lower()

    def __str__(self):
        return super().__str__() + f" | Size: {self.size}"


class Doll(Toy):

    def __init__(self, name: str, price: float, min_age: int, max_age: int, material: str):
        super().__init__(name, price, min_age, max_age)
        self.material = material

    def __str__(self):
        return super().__str__() + f" | Material: {self.material}"


class Ball(Toy):

    def __init__(self, name: str, price: float, min_age: int, max_age: int, diameter_cm: float):
        super().__init__(name, price, min_age, max_age)
        self.diameter_cm = diameter_cm

    def __str__(self):
        return super().__str__() + f" | Diameter: {self.diameter_cm}cm"


class Block(Toy):

    def __init__(self, name: str, price: float, min_age: int, max_age: int, piece_count: int):
        super().__init__(name, price, min_age, max_age)
        self.piece_count = piece_count

    def __str__(self):
        return super().__str__() + f" | Pieces: {self.piece_count}"


class Playroom:

    def __init__(self, budget: float):
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
        self.budget = budget
        self.toys = []

    def add_toy(self, toy: Toy):

        current_total = sum(t.price for t in self.toys)
        if current_total + toy.price > self.budget:
            raise ValueError(
                f"Cannot add '{toy.name}': Exceeds playroom budget of ${self.budget:.2f}.")
        self.toys.append(toy)

    def sort_toys_by_price(self):

        self.toys.sort(key=lambda t: t.price)

    def find_toys_in_price_range(self, min_price: float, max_price: float):

        if min_price > max_price:
            raise ValueError(
                "Minimum price cannot be greater than maximum price.")

        found_toys = []
        for toy in self.toys:
            if min_price <= toy.price <= max_price:
                found_toys.append(toy)
        return found_toys

    def display_room(self):

        print(f"--- Playroom Status ---")
        print(f"Total Budget: ${self.budget:.2f}")
        current_spent = sum(t.price for t in self.toys)
        print(f"Total Spent:  ${current_spent:.2f}")
        print(f"Remaining:    ${self.budget - current_spent:.2f}\n")

        if not self.toys:
            print("The playroom is empty.")
        else:
            print("Toys in the room:")
            for toy in self.toys:
                print(f" - {toy}")
        print("-----------------------")


def main():
    try:

        room = Playroom(budget=100.00)

        small_car = Car("Hot Wheels Fast", 15.50, 3, 7, "small")
        large_car = Car("RC Monster Truck", 45.00, 8, 14, "large")
        barbie = Doll("Barbie Princess", 22.00, 4, 10, "Plastic")
        soccer_ball = Ball("Adidas Soccer Ball", 25.00, 5, 99, 22.0)
        lego = Block("Lego Classic", 35.00, 4, 99, 484)

        room.add_toy(small_car)
        room.add_toy(barbie)
        room.add_toy(soccer_ball)
        room.add_toy(large_car)

        print("Initial Playroom:")
        room.display_room()

        room.sort_toys_by_price()
        print("\nPlayroom after sorting by price:")
        room.display_room()

        min_p = 20.00
        max_p = 30.00
        print(f"\nSearching for toys between ${min_p:.2f} and ${max_p:.2f}:")
        found = room.find_toys_in_price_range(min_p, max_p)

        if found:
            for t in found:
                print(f" Found: {t}")
        else:
            print(" No toys found in this price range.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
