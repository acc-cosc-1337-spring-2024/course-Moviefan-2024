import unittest
from src.homework.i_dictionaries_and_sets import add_inventory, remove_inventory_widget

class TestConfig(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}
        
        # Test adding Widget1 with quantity of 10
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        # Test updating existing item quantity to 35
        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        # Test updating existing item quantity to 25
        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {"Widget1": 10, "Widget2": 20}

        # Remove Widget1
        remove_inventory_widget(inventory_dictionary, "Widget1", 10)

        # Test length of dictionary is 1
        self.assertEqual(len(inventory_dictionary), 1)

        # Test that Widget2 still exists
        self.assertIn("Widget2", inventory_dictionary)