const palindrome = require("./palindrome");

test("racecar", () => {
  expect(palindrome("racecar"))===(true);
});

test("Noon", () => {
  expect(palindrome("Noon")===(true));
});

test("ciVic", () => {
  expect(palindrome("ciVic"))===(true);
});

test("434", () => {
  expect(palindrome(434)===(true));
});

test("123", () => {
  expect(palindrome(123))===(false);
});

test("SentenceOne", () => {
  expect(palindrome("Sore was I ere I saw Eros."))===(true);
});

test("SentenceTwo", () => {
  expect(palindrome("A man, a plan, a canal -- Panama")===(true));
});

