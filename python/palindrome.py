def palindrome(word):
    # Write code here
    word = str(word).lower()
    banned = "!@#$%^&*()_+-=[]{};':,./<>? "
    
    # Remove punctuation through an overly complicated method I totally didn't look up online
    clean = ''.join(filter(lambda x: x not in list(banned), word))
    nealc = clean[::-1]  #Reverses the string
    if clean == nealc: return True
    return False
    
