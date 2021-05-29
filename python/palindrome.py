


def palindrome(word):
    # lowercase the word and take out all spaces for both a varriable and the original words
    
    word_list = list(word.lower())
    # iterate through list and take out spaces
    for letter in word_list:
        if letter == ' ':
            word_list.remove(' ')
     
    # reverse the word list
    reversed_word_list = list(reversed(word_list))
    # return the comparrison 
    return word_list == reversed_word_list
    
# print(palindrome('racecar'))