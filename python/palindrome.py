def palindrome(word):
    # Write code here
    if word == "":
        return True
    else:
        lowered_word = word.lower()
        return pal_helper(lowered_word,0,len(lowered_word)-1)

def pal_helper(word, left, right):
    if left > right:
        return True
    else:
        if word[left] != word[right]:
            return False
        return pal_helper(word, left+1, right-1)