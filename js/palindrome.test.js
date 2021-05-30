// Can you translate this driver code to unit tests?

const { expect } = require('@jest/globals');
const { test } = require('jest-circus');
const palindrome = require('./palindrome');
test('will return true if the word is plaindrome', () => {
  expect(palindrome('abc')).tobe('abc');
})