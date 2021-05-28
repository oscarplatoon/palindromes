// check input type of WORD
// if WORD is integer, convert to string
// Remove all non alpha-numeric chars from WORD and store in CLEANWORD
// reverse CLEANWORD and store in REVERSEWORD
// compare CLEANWORD and REVERSEWORD and return the result
exports.palindrome = function(inputWord) {
    
    let word = ""

    if (typeof(inputWord) === "number") {
      word = inputWord.toString();
    } else {
      word = inputWord.slice();
    }
   
    let cleanWord = word.replace(/\W/g, '')
    cleanWord = cleanWord.toLowerCase();

    let reverseWord = cleanWord.split("").reverse().join("");
 
    return reverseWord === cleanWord;

};

