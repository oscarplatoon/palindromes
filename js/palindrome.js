// check input type of WORD
// if WORD is integer, convert to string
// Remove all non alpha-numeric chars from WORD
// reverse WORD and store in REVERSEWORD
// compare WORD and REVERSEWORD and return the result
// exports.

let palindrome = function(word) {
    if (typeof(word) === "number") {
      word = toString(word);
    }
   
    let cleanWord = word.replace(/\W/g, '')

    return cleanWord;
};

console.log(palindrome("ra7c-e car"))
