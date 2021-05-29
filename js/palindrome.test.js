// Can you translate this driver code to unit tests?

var pal = require("./palindrome");

test(pal.palindrome('racecar') === true);
test(pal.palindrome('Noon') === true);
test(pal.palindrome('ciVic') === true);
test(pal.palindrome('nice') === false);
test(pal.palindrome(434) === true);
test(pal.palindrome(123) === false);


//console.log(pal.palindrome("Sore was I ere I saw Eros.") === true);
//console.log(pal.palindrome("A man, a plan, a canal -- Panama") === true);
