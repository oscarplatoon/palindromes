from palindrome import palindrome
import unittest

class palindromeTestCase(unittest.TestCase):
    """ Tests for 'palindrome.py' """
    
    def test_returns_true(self):
        """ should return true """
        self.assertTrue(palindrome("racecar"), "true")
        self.assertTrue(palindrome(434), "true")
        self.assertTrue(palindrome("Noon"), "true")
        self.assertTrue(palindrome("Sore was I ere I saw Eros."), "true")
        self.assertTrue(palindrome("A man, a plan, a canal -- Panama"), "true")
        self.assertTrue(palindrome("21s-Race Cars!? 12%"), "true")
        
    def test_returns_false(self):
        """ should return false """
        self.assertFalse(palindrome(123), "false")
        self.assertFalse(palindrome("bomb"), "false")
        
if __name__ == '__main__':
    unittest.main()