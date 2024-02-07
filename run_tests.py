# File: tests/homework/c_decisions/run_tests.py

import unittest
from tests.homework.c_decisions import test_decisions


    # Load the test cases from the test_decisions module
suite = unittest.TestLoader().loadTestsFromModule(test_decisions)

    # Run the tests
unittest.TextTestRunner(verbosity=2).run(suite)