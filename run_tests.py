# Replace the import statement for the test module

import unittest

from tests.homework.e_functions import tests_functions

# Replace the suite variable initialization
suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
