const { expect } = require("@jest/globals");
let h = require("./palindrome.js");
let testPalindromes = ['racecar', 'Noon', 'ciVic', 434, "Sore was I ere I saw Eros.", "A man, a plan, a canal -- Panama"];
let testNotPalindromes = ["nice", 123];

test("testPalindromes are true", 
  () => {
    for (let palin of testPalindromes) {
      expect(h.palindrome(palin)).toBe(true);
    }
  }
)

test("testNotPalindromes are false", 
  () => {
    for (let notPalindrome of testNotPalindromes) {
      expect(h.palindrome(notPalindrome)).toBeFalsy();
    }
  }
)