# Can you translate this driver code to unit tests? um yes
import unittest
from palindrome import palindrome
class PalTestCase(unittest.TestCase):
    """Tests for palindrome.py."""
    """.yp.emordnilap rof stseT""" #I'm a smartass
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
    def test_phrase1(self):
        self.assertEqual(palindrome('Sore was I ere I saw Eros.'), True)
    def test_phrase2(self):
        self.assertEqual(palindrome('A man, a plan, a canal -- Panama'), True)


if __name__ == '__main__':
    unittest.main()
