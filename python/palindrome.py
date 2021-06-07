import re
def palindrome(word):
    word = re.sub('\W','',str(word).lower())
    if len(word) <= 1:
        return True
    else:
        if word[0]==word[-1]:
            return palindrome(word[1:-1])
        else:
            return False
