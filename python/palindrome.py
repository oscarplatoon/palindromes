def palindrome(word):
    # Write code here
    if word == "":
        return True
    else:
        lowered_word = word.lower()
        
        left = 0
        right = len(lowered_word)-1

        while(left < right):
            if lowered_word[left] != lowered_word[right]:
                return False
            left += 1
            right -= 1
        return True
