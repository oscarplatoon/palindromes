
function palindrome(word) {
  //Placeholder for integer to string
  let numToString 
  let reversedNumToString
  //Check to see if word is an integer
  while (Number.isInteger(word)) {
    //Non reversal of integer to string/Persistent data of original integer
    numToString = word.toString()
    //Reversal of integer to string
    reversedNumToString = word.toString().split('').reverse().join('')
    //If non reversal int equals reversal int return true/else false
    if (numToString === reversedNumToString) {
      return true
    } else {
      return false
    }
  }

  //Check string for punctuation
  const regex = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g;;
  let punctuations = word.replace(regex, '')
  //Lowercase words/hold original word
  let loweredWord = punctuations.toLowerCase()
  //Reverse of original word
  let reversedWord = loweredWord.split("").reverse().join("")

  //Compare original to reversed word
  if (loweredWord === reversedWord) {
    return true
  } else {
    return false
  }

};

module.exports = palindrome