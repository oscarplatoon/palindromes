def palindrome(word):
    
    my_str = " "
    first_str = my_str.lower()
    second_str = reversed(first_str)
    
    if list(first_str) == list(second_str):
        return second_str == first_str

