import unittest

from palindrome import is_palindrome
from fraudulent_transactions import find_fraudulent_transactions


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


class TestFraudulentTransactions(unittest.TestCase):
    """Test the fraudulent transactions utility."""

    def test_high_amount_frauds(self):
        transactions = [
            [1, 1000, 10000.00, "Bogotá", 10],
            [2, 1001, 15000.00, "Bogotá", 10],
        ]
        self.assertEqual(find_fraudulent_transactions(transactions), [1, 2])

    def test_low_amount_non_frauds(self):
        transactions = [
            [1, 1000, 1000.00, "Bogotá", 10],
            [2, 1001, 9999.99, "Bogotá", 10],
        ]
        self.assertEqual(find_fraudulent_transactions(transactions), [])

    def test_same_card_different_city_within_30_minutes(self):
        transactions = [
            [1, 1000, 500.00, "Cartagena", 0],
            [2, 1000, 500.00, "Medellín", 20],
        ]
        self.assertEqual(find_fraudulent_transactions(transactions), [2])

    def test_same_card_different_city_after_30_minutes(self):
        transactions = [
            [1, 1000, 500.00, "Cartagena", 0],
            [2, 1000, 500.00, "Medellín", 31],
        ]
        self.assertEqual(find_fraudulent_transactions(transactions), [])

    def test_combined_fraud_cases(self):
        transactions = [
            [1, 1000, 500.00, "Vadodara", 0],
            [2, 1000, 500.00, "Mumbai", 5],
            [3, 1001, 500.00, "Mumbai", 10],
            [4, 1001, 10000.00, "Mumbai", 10],
        ]
        self.assertEqual(find_fraudulent_transactions(transactions), [2, 4])


if __name__ == "__main__":
    unittest.main()
