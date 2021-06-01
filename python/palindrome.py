def palindrome(sequence):
    word = str(sequence)
    clean_word = ''
    for letter in word:
        if letter.isalpha():
            clean_word += letter
    if clean_word.lower() == clean_word[::-1].lower():
        return True
    else:
        return False
    
palindrome(121)