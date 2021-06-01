function palindrome(str) {
  if (str.toLowerCase().toString().replace(/[\W]/, '') === str.toLowerCase().toString().replace(/[\W]/, '').split('').reverse().join('')) {
    return true
  } else {
    return false
  }
}

module.exports = palindrome
