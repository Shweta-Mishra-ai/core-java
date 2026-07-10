import unittest
import math
from utils import math_utils

class TestMathUtils(unittest.TestCase):
    
    def test_is_disarium(self):
        self.assertTrue(math_utils.is_disarium(89))  # 8^1 + 9^2 = 8 + 81 = 89
        self.assertTrue(math_utils.is_disarium(175)) # 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175
        self.assertFalse(math_utils.is_disarium(90))
        self.assertFalse(math_utils.is_disarium(-89))
        self.assertTrue(math_utils.is_disarium(0))  # 0^1 = 0

    def test_is_duck(self):
        self.assertTrue(math_utils.is_duck("102"))
        self.assertTrue(math_utils.is_duck(" 702 "))
        self.assertFalse(math_utils.is_duck("012"))
        self.assertFalse(math_utils.is_duck("123"))
        self.assertFalse(math_utils.is_duck(""))
        self.assertTrue(math_utils.is_duck("-102"))

    def test_is_happy(self):
        self.assertTrue(math_utils.is_happy(19)) # 1^2+9^2=82 -> 8^2+2^2=68 -> 6^2+8^2=100 -> 1^2+0^2+0^2=1
        self.assertFalse(math_utils.is_happy(4))
        self.assertFalse(math_utils.is_happy(0))
        self.assertFalse(math_utils.is_happy(-19))

    def test_is_neon(self):
        self.assertTrue(math_utils.is_neon(9))  # 9*9=81 -> 8+1=9
        self.assertTrue(math_utils.is_neon(0))  # 0*0=0 -> 0=0
        self.assertFalse(math_utils.is_neon(12))
        self.assertFalse(math_utils.is_neon(-9))

    def test_is_niven(self):
        self.assertTrue(math_utils.is_niven(18)) # 18 % (1+8) == 0
        self.assertTrue(math_utils.is_niven(10)) # 10 % (1+0) == 0
        self.assertFalse(math_utils.is_niven(11))
        self.assertFalse(math_utils.is_niven(0))
        self.assertFalse(math_utils.is_niven(-18))

    def test_is_prime(self):
        self.assertTrue(math_utils.is_prime(2))
        self.assertTrue(math_utils.is_prime(17))
        self.assertFalse(math_utils.is_prime(1))
        self.assertFalse(math_utils.is_prime(0))
        self.assertFalse(math_utils.is_prime(-5))
        self.assertFalse(math_utils.is_prime(9))

    def test_primes_in_range(self):
        self.assertEqual(math_utils.primes_in_range(1, 10), [2, 3, 5, 7])
        self.assertEqual(math_utils.primes_in_range(10, 20), [11, 13, 17, 19])
        self.assertEqual(math_utils.primes_in_range(20, 10), [])

    def test_is_spy(self):
        self.assertTrue(math_utils.is_spy(1124)) # sum: 1+1+2+4=8 | prod: 1*1*2*4=8
        self.assertTrue(math_utils.is_spy(123))  # sum: 6 | prod: 6
        self.assertFalse(math_utils.is_spy(124))
        self.assertFalse(math_utils.is_spy(0))

    def test_is_magic(self):
        self.assertTrue(math_utils.is_magic(19)) # 1+9=10 -> 1+0=1
        self.assertTrue(math_utils.is_magic(1234)) # 1+2+3+4=10 -> 1+0=1
        self.assertTrue(math_utils.is_magic(55))  # 5+5=10 -> 1+0=1 is magic
        self.assertFalse(math_utils.is_magic(25))  # 2+5=7 (not 1)

    def test_is_pronic(self):
        self.assertTrue(math_utils.is_pronic(6))  # 2 * 3 = 6
        self.assertTrue(math_utils.is_pronic(12)) # 3 * 4 = 12
        self.assertFalse(math_utils.is_pronic(10))
        self.assertFalse(math_utils.is_pronic(-6))

    def test_is_special(self):
        self.assertTrue(math_utils.is_special(145)) # 1! + 4! + 5! = 1 + 24 + 120 = 145
        self.assertFalse(math_utils.is_special(100))

    def test_get_factors(self):
        self.assertEqual(math_utils.get_factors(6), [1, 2, 3, 6])
        self.assertEqual(math_utils.get_factors(1), [1])
        self.assertEqual(math_utils.get_factors(0), [])

    def test_factorial(self):
        self.assertEqual(math_utils.factorial(0), 1)
        self.assertEqual(math_utils.factorial(5), 120)
        with self.assertRaises(ValueError):
            math_utils.factorial(-1)

    def test_gcd(self):
        self.assertEqual(math_utils.gcd(12, 18), 6)
        self.assertEqual(math_utils.gcd(-12, 18), 6)
        self.assertEqual(math_utils.gcd(0, 5), 5)

    def test_power(self):
        self.assertEqual(math_utils.power(2, 3), 8)
        self.assertEqual(math_utils.power(5, 0), 1)
        with self.assertRaises(ValueError):
            math_utils.power(2, -3)

    def test_square(self):
        self.assertEqual(math_utils.square(4), 16)
        self.assertEqual(math_utils.square(-4), 16)

    def test_sum_digits(self):
        self.assertEqual(math_utils.sum_digits(123), 6)
        self.assertEqual(math_utils.sum_digits(-123), 6)
        self.assertEqual(math_utils.sum_digits(0), 0)

    def test_absolute_val(self):
        self.assertEqual(math_utils.absolute_val(-5), 5)
        self.assertEqual(math_utils.absolute_val(5), 5)

    def test_marks_total_avg(self):
        self.assertEqual(math_utils.marks_total_avg([80, 90, 100]), (270, 90.0))
        self.assertEqual(math_utils.marks_total_avg([]), (0, 0.0))

if __name__ == '__main__':
    unittest.main()
