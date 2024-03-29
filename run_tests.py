# Import the test module for dictionaries and sets
import unittest

from tests.homework.i_dictionaries_and_sets import test_dictionaries_and_sets

# Adjust the suite creation
suite = unittest.TestLoader().loadTestsFromModule(test_dictionaries_and_sets)