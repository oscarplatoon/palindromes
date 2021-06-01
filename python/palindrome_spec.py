# Can you translate this driver code to unit tests?

from palindrome import palindrome
import unittest


class TestPalindrome(unittest.TestCase):

    def test_for_easy(self):
        self.assertEqual(palindrome('racecar'), True)
    
    def test_for_int(self):
        self.assertEqual(palindrome(12321), True)

    def test_for_hard(self):
        self.assertEqual(palindrome('Ra c ecAr'), True)

    def test_for_false(self):
        self.assertEqual(palindrome('Ra c ecArx'), False)



if __name__ == '__main__':
    unittest.main()

