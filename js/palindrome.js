const palindrome = (word) => {
  
  let reversedWord = word.toString().split("").reverse().join().toLowerCase().replaceAll("!@#$^&%*()+=-[]\/{}|:<>?,. ", "");
  
  
  if (reversedWord === word) {
    return true
  } else {
    return false
  }
  
  

};


module.exports = palindrome