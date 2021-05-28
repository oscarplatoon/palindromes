export.palindrome = function(str){
    
    let reg = /[A-Za-z0-9]/g; 
    let firstStr = str.toLowerCase().replace(reg, " ");
    let secondStr = firstStr.split(" ").reverse().join(" ");
    
    return secondStr === firstStr;
}
