import unittest
from utils import string_utils

class TestStringUtils(unittest.TestCase):

    def test_ascii_val(self):
        self.assertEqual(string_utils.ascii_val("A"), 65)
        self.assertEqual(string_utils.ascii_val("a"), 97)
        with self.assertRaises(ValueError):
            string_utils.ascii_val("")

    def test_count_characters(self):
        res = string_utils.count_characters("Hello World 123!")
        self.assertEqual(res["vowels"], 3)       # e, o, o
        self.assertEqual(res["consonants"], 7)   # H, l, l, W, r, l, d
        self.assertEqual(res["digits"], 3)       # 1, 2, 3
        self.assertEqual(res["spaces"], 2)       # two spaces
        self.assertEqual(res["special"], 1)      # !

    def test_extract_substring(self):
        self.assertEqual(string_utils.extract_substring("abcdef", 1, 3), "bcd")
        self.assertEqual(string_utils.extract_substring("abcdef", 0, 5), "abcdef")
        with self.assertRaises(ValueError):
            string_utils.extract_substring("abcdef", -1, 3)
        with self.assertRaises(ValueError):
            string_utils.extract_substring("abcdef", 2, 8)
        with self.assertRaises(ValueError):
            string_utils.extract_substring("abcdef", 4, 2)

    def test_find_substring_index(self):
        self.assertEqual(string_utils.find_substring_index("hello", "ell"), 1)
        self.assertEqual(string_utils.find_substring_index("hello", "world"), -1)

    def test_is_substring(self):
        self.assertTrue(string_utils.is_substring("hello", "ell"))
        self.assertFalse(string_utils.is_substring("hello", "world"))

    def test_lower_to_upper_custom(self):
        self.assertEqual(string_utils.lower_to_upper_custom("aBc12!"), "AbC12!")

    def test_to_title_case(self):
        self.assertEqual(string_utils.to_title_case("hello world"), "Hello World")
        self.assertEqual(string_utils.to_title_case("HELLO WORLD"), "Hello World")
        self.assertEqual(string_utils.to_title_case("   "), "")

    def test_is_palindrome_string(self):
        self.assertTrue(string_utils.is_palindrome_string("A man, a plan, a canal: Panama"))
        self.assertTrue(string_utils.is_palindrome_string("racecar"))
        self.assertFalse(string_utils.is_palindrome_string("hello"))

    def test_is_palindrome_number(self):
        self.assertTrue(string_utils.is_palindrome_number(121))
        self.assertTrue(string_utils.is_palindrome_number(-121))
        self.assertFalse(string_utils.is_palindrome_number(123))

    def test_toggle_case(self):
        self.assertEqual(string_utils.toggle_case("aBc12!"), "AbC12!")

    def test_analyze_name(self):
        self.assertEqual(string_utils.analyze_name("Alicea"), "Name starts and ends with a")
        self.assertEqual(string_utils.analyze_name("Alice"), "Name starts with a")
        self.assertEqual(string_utils.analyze_name("Diana"), "Name ends with a")
        self.assertEqual(string_utils.analyze_name("Jane"), "Anywhere a")
        self.assertEqual(string_utils.analyze_name("Bob"), "No 'a' found in the name")
        self.assertEqual(string_utils.analyze_name("  "), "Empty name")

    def test_check_alphabets(self):
        self.assertEqual(string_utils.check_alphabets("123a45"), "123a45")
        self.assertEqual(string_utils.check_alphabets("12345"), "string not found")
        self.assertEqual(string_utils.check_alphabets(""), "string not found")

if __name__ == '__main__':
    unittest.main()
