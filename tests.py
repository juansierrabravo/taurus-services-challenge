import unittest

from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    """The tests are based on various cases including different types 
    of characters and case insensitivity, sourced from: 
    https://becomeawritertoday.com/palindrome-words/
    
    Assumptions:
    1. Non-alphabetic characters are omitted.
    2. Checks are case-insensitive.
    3. Phrases or sentences are permitted.
    4. Strings of 0 or 1 character are considered palindromes.
    """

    def test_palindrome_word(self):
        self.assertTrue(is_palindrome("tattarrattat"))

    def test_palindrome_case_insensitivity(self):
        self.assertTrue(is_palindrome("Tenet"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("Mr. Owl ate my metal worm."))
        self.assertTrue(is_palindrome("Won't lovers revolt now?"))
        self.assertTrue(is_palindrome("Drab as a fool, aloof as a bard!"))

    def test_non_palindrome_word(self):
        self.assertFalse(is_palindrome("hello"))

    def test_non_palindrome_phrase(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome("Rotato1r"))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome("@#A#A@"))

    def test_incorrect_types(self):
        with self.assertRaises(TypeError):
            is_palindrome(["not", "a", "string"])
        
        with self.assertRaises(TypeError):
            is_palindrome(12345)
        
        with self.assertRaises(TypeError):
            is_palindrome({"key": "value"})
        
        with self.assertRaises(TypeError):
            is_palindrome(123.45)
        
        with self.assertRaises(TypeError):
            is_palindrome(None)


if __name__ == '__main__':
    unittest.main()