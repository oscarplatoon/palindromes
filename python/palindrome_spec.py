from palindrome import palindrome
import unittest

class palindromeTestCase(unittest.TestCase):
    """ Tests for 'palindrome.py' """
    
    def test_returns_true(self):
        """ should return true """
        actual_output = palindrome("racecar")
        expected_output = "true"
        self.assertTrue(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return true """
        actual_output = palindrome(434)
        expected_output = "true"
        self.assertTrue(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return true """
        actual_output = palindrome("Noon")
        expected_output = "true"
        self.assertTrue(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return false """
        actual_output = palindrome(123)
        expected_output = "false"
        self.assertFalse(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return false """
        actual_output = palindrome("bomb")
        expected_output = "false"
        self.assertFalse(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return true """
        actual_output = palindrome("Sore was I ere I saw Eros.")
        expected_output = "true"
        self.assertTrue(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return true """
        actual_output = palindrome("A man, a plan, a canal -- Panama")
        expected_output = "true"
        self.assertTrue(actual_output, expected_output)
        
    def test_returns_true(self):
        """ should return true """
        actual_output = palindrome("21s-Race Cars!? 12%")
        expected_output = "true"
        self.assertTrue(actual_output, expected_output)
        
if __name__ == '__main__':
    unittest.main()