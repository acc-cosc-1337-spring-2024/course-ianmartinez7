#
import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die()

    def test_roll(self):
        self.die.roll() 
        roll_value = self.die.get_rolled_value()  # Get the rolled value
        self.assertIn(roll_value, [1, 2, 3, 4, 5, 6], "Roll should be between 1 and 6")

    def test_str(self):
        self.die.roll()  # Roll the die
        expected_str = f"The rolled value is {self.die.get_rolled_value()}"
        self.assertEqual(str(self.die), expected_str, "String representation should be accurate")

    def test_repeated_rolls(self):
        # Roll several times to ensure different values
        roll_values = []
        for _ in range(10):
            self.die.roll()
            roll_values.append(self.die.get_rolled_value())
        self.assertTrue(len(set(roll_values)) > 1, "Repeated rolls should produce varying results")

 
