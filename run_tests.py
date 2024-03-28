# Replace the import statement for the test module

import unittest

from tests.homework.i_dictionaries_and_sets import tests_dictionaries_and_sets


# Replace the suite variable initialization
suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)