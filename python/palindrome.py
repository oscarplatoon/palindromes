def palindrome(word):
    
    # Import ascii_letters to check for special characters
    from string import ascii_letters

    # Check if word is an integer
    if (isinstance(word, int)) :
        # Convert the int to a string and compare to original
        if str(word) [::-1] == str(word) :
            return True
        else :
            return False
   
    # Check if word has any special characters
    elif set(word).difference(ascii_letters) :
        # Create empty string to push our reversed string
        alpha_numeric_0 = ""
        alpha_numeric_1 = ""
        
        # Reverse the string and assign to variable
        reversed = word [::-1]
        
        # Filter through special characters in the reversed string
        for character_0 in reversed :
            if character_0.isalnum() :
                alpha_numeric_0 += character_0
        
        # Filter through special characters in the original string
        for character_1 in word :
            if character_1.isalnum() :
                alpha_numeric_1 += character_1
        
        # Compare the strings
        if alpha_numeric_0.lower() == alpha_numeric_1.lower() :
            return True
        else :
            return False

    # Reverse and compare the word
    else :
        # Reverse the Word 
        reversed = word [::-1]
        
        # Check if the reversed word equals the original
        if reversed.lower() == word.lower() :
            return True
        else :
            return False