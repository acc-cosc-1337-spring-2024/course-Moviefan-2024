# In test_dictionaries_and_sets.py

import unittest
from src.homework.i_dictionaries_sets import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}
        
        # Assert that adding Widget1 with quantity of 10 inserts the correct value
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        # Assert that adding Widget1 with quantity of 25 updates the existing quantity correctly
        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        # Assert that adding Widget1 with quantity of -10 updates the existing quantity correctly
        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {"Widget1": 10, "Widget2": 20}

        # Remove widget1 and test length of dictionary and existence of widget2
        remove_inventory_widget(inventory_dictionary, "Widget1")
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertIn("Widget2", inventory_dictionary)
