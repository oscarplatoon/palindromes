import unittest

from palindrome import palindrome

class TestPalindrome(unittest.TestCase) :
      
    def test_palindrome_0(self) :
        self.assertEqual(palindrome("racecar"), True)
    
    def test_palindrome_1(self) :
        self.assertEqual(palindrome("Noon"), True)
    
    def test_palindrome_2(self) :
        self.assertEqual(palindrome(434), True)
    
    def test_palindrome_3(self) :
        self.assertEqual(palindrome(123), False)

    def test_palindrome_4(self) :
        self.assertEqual(palindrome('Sore was I ere I saw Eros.'), True)
    
    def test_palindrome_5(self) :
        self.assertEqual(palindrome('A man, a plan, a canal -- Panama'), True)

if __name__ == '__main__':
    unittest.main()

