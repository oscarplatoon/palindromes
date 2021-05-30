// Can you translate this driver code to unit tests?

const { expect } = require('@jest/globals');
const palindrome = require('./palindrome');
test('will return true if the word is plaindrome', () => {
  expect(palindrome("Sore was I ere I saw Eros.")).toBe(true);
  expect(palindrome("A man, a plan, a canal -- Panama")).toBe(true);
  expect(palindrome(1221)).toBe(true);
  expect(palindrome(1_2_2_2_1)).toBe(true);
})