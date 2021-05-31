# Can you translate this driver code to unit tests?
import unittest
from palindrome import palindrome

class PalindromeTestCase(unittest.TestCase):

    def test_bool(self):
        self.assertIsInstance(palindrome(''), bool)

    def test_racecar(self):
        self.assertEqual(palindrome('racecar'), True)
    
    def test_noon(self):
        self.assertEqual(palindrome('Noon'), True)

    def test_civic(self):
        self.assertEqual(palindrome('ciVic'), True)

    def test_nice(self):
        self.assertEqual(palindrome('nice'), False)

    def test_434(self):
        self.assertEqual(palindrome('434'), True)
    
    def test_123(self):
        self.assertEqual(palindrome('123'), False)

    def test_bomb(self):
        self.assertEqual(palindrome('bomb'), False)

    # print("The following should be True if you're trying to do the extra portion of this challenge")
    # print(palindrome('Sore was I ere I saw Eros.') == True)
    # print(palindrome('A man, a plan, a canal -- Panama') == True)
