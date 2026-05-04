import unittest
from lab5_oop import Toy, Car, Doll, Ball, Block, Playroom


class TestPlayroom(unittest.TestCase):

    def setUp(self):
        """Set up a fresh playroom and toys for each test."""
        self.room = Playroom(budget=100.0)
        self.car1 = Car("Small Car", 10.0, 2, 5, "small")
        self.car2 = Car("Large Car", 50.0, 6, 12, "large")
        self.doll = Doll("Rag Doll", 15.0, 1, 4, "Cloth")
        self.ball = Ball("Bouncy Ball", 5.0, 3, 10, 10.0)
        self.blocks = Block("Wood Blocks", 25.0, 1, 5, 50)

    def test_add_toy_success(self):
        """Test adding toys within the budget."""
        self.room.add_toy(self.car1)
        self.room.add_toy(self.doll)
        self.assertEqual(len(self.room.toys), 2)

    def test_add_toy_exceeds_budget(self):
        """Test adding a toy that exceeds the total budget."""
        self.room.add_toy(self.car2)  # 50
        self.room.add_toy(self.blocks)  # 25 (Total 75)

        # Adding a toy worth 30 should raise an error (75 + 30 > 100)
        expensive_toy = Car("Luxury RC", 30.0, 8, 15, "medium")
        with self.assertRaises(ValueError):
            self.room.add_toy(expensive_toy)

    def test_sort_toys_by_price(self):
        """Test if toys are sorted correctly by price."""
        self.room.add_toy(self.car2)   # 50.0
        self.room.add_toy(self.ball)   # 5.0
        self.room.add_toy(self.doll)   # 15.0

        self.room.sort_toys_by_price()

        self.assertEqual(self.room.toys[0].name, "Bouncy Ball")
        self.assertEqual(self.room.toys[1].name, "Rag Doll")
        self.assertEqual(self.room.toys[2].name, "Large Car")

    def test_find_toys_in_price_range(self):
        """Test searching for toys within a valid price range."""
        self.room.add_toy(self.car1)   # 10.0
        self.room.add_toy(self.doll)   # 15.0
        self.room.add_toy(self.blocks)  # 25.0

        # Search between 12.0 and 20.0
        found = self.room.find_toys_in_price_range(12.0, 20.0)

        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].name, "Rag Doll")

    def test_invalid_car_size(self):
        """Test validation of car size attribute."""
        with self.assertRaises(ValueError):
            Car("Bad Car", 10.0, 3, 5, "gigantic")


if __name__ == "__main__":
    unittest.main()
