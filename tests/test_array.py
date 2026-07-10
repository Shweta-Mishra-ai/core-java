import unittest
from utils import array_utils

class TestArrayUtils(unittest.TestCase):

    def test_array_sum_avg(self):
        tot, avg = array_utils.array_sum_avg([1, 2, 3, 4, 5])
        self.assertEqual(tot, 15)
        self.assertEqual(avg, 3.0)
        self.assertEqual(array_utils.array_sum_avg([]), (0, 0.0))

    def test_get_even_odd_elements(self):
        res = array_utils.get_even_odd_elements([13, 7, 6, 91, 67])
        self.assertEqual(res["even"], [6])
        self.assertEqual(res["odd"], [13, 7, 91, 67])

    def test_array_length_primes_check(self):
        self.assertEqual(array_utils.array_length_primes_check([1, 2, 3, 4, 5, 6]), [2, 3, 5])
        self.assertEqual(array_utils.array_length_primes_check([]), [])

    def test_find_min_max(self):
        res = array_utils.find_min_max([5, 8, 2, 9, 1])
        self.assertEqual(res["max_val"], 9)
        self.assertEqual(res["max_pos"], 3)
        self.assertEqual(res["min_val"], 1)
        self.assertEqual(res["min_pos"], 4)
        
        res_empty = array_utils.find_min_max([])
        self.assertEqual(res_empty["max_pos"], -1)

    def test_is_palindrome_array(self):
        self.assertTrue(array_utils.is_palindrome_array([1, 2, 3, 2, 1]))
        self.assertTrue(array_utils.is_palindrome_array([]))
        self.assertFalse(array_utils.is_palindrome_array([1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()
