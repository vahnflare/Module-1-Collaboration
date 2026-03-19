import unittest
import my_sum

class TestSum(unittest.TestCase):

    def test_numbers(self):
        result = my_sum.sum([1, 2, 3])
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()