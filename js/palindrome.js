const palindrome = (word) => {
  // create empty string named palindrome
  let palindromeStr = "";
  let alpahbets = "abcdefghijklmnopqrstuvwxyz";
  // if the input word is number make it to string so that for loop can be used
  if(typeof word === "number") {
    word = String(word);
  }
  // omit space
  // ignore case sensitive
  // filter out special chars
  word = word.split(' ').join('').toLowerCase();
  let filterOutSpecialWord = word.replace(/[^a-zA-Z]/gm,"")
  // loop through starting last index decrement 1
  // and save each index element to palindrome word
  for(let i = word.length - 1; i >= 0 ; i --) {
    // only alphabets to be added
    if(alpahbets.indexOf(word[i]) > -1) {
    palindromeStr += word[i];
    }
  }
  // compare palindrome and input word
  // return true if match 
  // else false.
  return (palindromeStr === filterOutSpecialWord ?  true : false);
}
palindrome("Sore was I ere I saw Eros.")
module.exports = palindrome;
