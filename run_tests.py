# Replace the import statement for the test module
from tests.homework.d_repetition import tests_repetition

# Replace the suite variable initialization
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
