import unittest
from palindrome import palindrome

class PalindromeTest(unittest.TestCase):

    def test_type(self):
        self.assertEqual(type(palindrome('racecar')),bool)

    def test_1(self):
        self.assertEqual(palindrome('racecar'),True)

    def test_2(self):
        self.assertEqual(palindrome('Noon'),True)

    def test_3(self):
        self.assertEqual(palindrome('ciVic'),True)

    def test_4(self):
        self.assertEqual(palindrome('nice') ,False)
    
    def test_5(self):
        self.assertEqual(palindrome(434) ,True)

    def test_6(self):
        self.assertEqual(palindrome(123) ,False)

    def test_7(self):
        self.assertEqual(palindrome('bomb') ,False)

    def test_8(self):
        self.assertEqual(palindrome('Sore was I ere I saw Eros.') ,True)

    def test_9(self):
        self.assertEqual(palindrome('A man, a plan, a canal -- Panama') ,True)
    

if __name__ =='__main__':
    unittest.main()