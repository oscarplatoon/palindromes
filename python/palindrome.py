import string

def palindrome(word):
  #check if word is an integer
  while isinstance(word, int):
    int_to_str = f'{word}'
    if int_to_str == int_to_str[::-1]:
      return True
    elif int_to_str != int_to_str[::-1]:
      return False
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
   