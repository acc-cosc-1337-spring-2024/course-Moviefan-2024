import unittest
from src.homework.d_repetition.decisions import sum_odd_numbers

class TestDecisions(unittest.TestCase):

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(5), 9)
        self.assertEqual(sum_odd_numbers(10), 25)
        self.assertEqual(sum_odd_numbers(15), 64)

if __name__ == '__main__':
    unittest.main()

