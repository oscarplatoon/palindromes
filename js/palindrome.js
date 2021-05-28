// check input type of WORD
// if WORD is integer, convert to string
// Remove all non alpha-numeric chars from WORD and store in CLEANWORD
// reverse CLEANWORD and store in REVERSEWORD
// compare CLEANWORD and REVERSEWORD and return the result
// exports.

let palindrome = function(word) {
    if (typeof(word) === "number") {
      word = toString(word);
    }
   
    let cleanWord = word.replace(/\W/g, '')
    cleanWord = cleanWord.toLowerCase();

    let reverseWordArray = [];
    
    for (let i = 0; i < word.length; i++){
      reverseWordArray.push(cleanWord[i]);
    }

    let reverseWord = reverseWordArray.join("");

    return reverseWord === cleanWord;

};

console.log(palindrome("Noon"))
