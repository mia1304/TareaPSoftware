import unittest
from sum import sum

class TestSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(5, 5), 10)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()