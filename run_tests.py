# Replace the import statement for the test module

import unittest

from tests.homework.h_strings import test_strings


# Replace the suite variable initialization
suite = unittest.TestLoader().loadTestsFromModule(test_strings)

