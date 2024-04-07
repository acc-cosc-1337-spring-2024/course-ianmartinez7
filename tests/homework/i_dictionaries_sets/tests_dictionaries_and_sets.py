
import unittest
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog2_not_prog1
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget
class TestInventoryManagement(unittest.TestCase):

# for homework assignment 6
    def test_add_inventory(self):
        
        inventory = {}
        add_inventory(inventory, 'Widget1', 10)
        self.assertEqual(inventory.get('Widget1'), 10, "Failed to add a new widget.")

        add_inventory(inventory, 'Widget1', 25)
        self.assertEqual(inventory.get('Widget1'), 35, "Failed to update an existing widget.")

        add_inventory(inventory, 'Widget1', -10)
        self.assertEqual(inventory.get('Widget1'), 25, "Failed to update an existing widget with negative quantity.")

    def test_remove_inventory_widget(self):
        inventory = {'Widget1': 25, 'Widget2': 40}

        result = remove_inventory_widget(inventory, 'Widget1')
        self.assertNotIn('Widget1', inventory, "Failed to remove an existing widget.")
        self.assertEqual(result, "Record deleted", "Failed to return the correct message after deletion.")
        
        self.assertEqual(len(inventory), 1, "The inventory should have only one item after deletion.")
        self.assertIn('Widget2', inventory, "Widget2 should still exist in the inventory.")

        result = remove_inventory_widget(inventory, 'Widget3')
        self.assertEqual(result, "Item not found", "Failed to return the correct message when item not found.")


# test cases for homework assignment 7



def test_get_students_who_took_prog1_and_prog2(self):
        expected = {'Student3'}
        result = get_students_who_took_prog1_and_prog2(self.prog1, self.prog2)
        self.assertEqual(result, expected)

def test_get_students_who_took_prog1_or_prog2(self):
        expected = {'Student1', 'Student2', 'Student3', 'Student4', 'Student5'}
        result = get_students_who_took_prog1_or_prog2(self.prog1, self.prog2)
        self.assertEqual(result, expected)

def test_get_students_who_took_prog1_not_prog2(self):
        expected = {'Student1', 'Student2'}
        result = get_students_who_took_prog1_not_prog2(self.prog1, self.prog2)
        self.assertEqual(result, expected)

def test_get_students_who_took_prog2_not_prog1(self):
        expected = {'Student4', 'Student5'}
        result = get_students_who_took_prog2_not_prog1(self.prog1, self.prog2)
        self.assertEqual(result, expected)