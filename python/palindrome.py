import string

def palindrome(word):
  #Removes any punctuations in a possible string
  punct_check = word.translate(str.maketrans('', '', string.punctuation))
  #Lowercase String prior to comparison/persisent copy of word
  word_lowered = punct_check.lower()
  #Reverse of word prior to comparison
  word_reversed = word_lowered[::-1]
  if word_reversed == word_lowered:
    return True
  else:
    return False
   



print(palindrome("Sore was I ere I saw Eros."))
