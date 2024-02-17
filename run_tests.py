# File: tests/homework/c_decisions/run_tests.py

import unittest
from tests.homework.d_repetition import tests_repetition


    # Load the test cases from the test_decisions module
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

    # Run the tests
unittest.TextTestRunner(verbosity=2).run(suite)