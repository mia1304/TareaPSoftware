import unittest
from sum import sum

class TestSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(5, 5), 10)

    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(-1, 1), 0)
        
    def test_sum_zero(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 5), 5)
        self.assertEqual(sum(5, 0), 5)

    def test_sum_floats(self):
        self.assertAlmostEqual(sum(1.5, 2.5), 4.0)
        self.assertAlmostEqual(sum(-1.1, 1.1), 0.0)


if __name__ == '__main__':
    unittest.main()