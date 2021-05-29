import unittest
from palindrome import palindrome

class TestingOfPalindrome(unittest.TestCase):
  def test_of_single_word(self):
    print(palindrome('racecar') == True)
    print(palindrome('Noon') == True)
    print(palindrome('ciVic') == True)
    print(palindrome('nice') == False)
    print(palindrome(434) == True)
    print(palindrome(123) == False)
    print(palindrome('bomb') == False)

if __name__ == '__main__':
  unittest.main()

#print("The following should be True if you're trying to do the extra portion of this challenge")
#print(palindrome('Sore was I ere I saw Eros.') == True)
#print(palindrome('A man, a plan, a canal -- Panama') == True)
