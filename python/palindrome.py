def palindrome(word):
  alpha_nums = 'abcdefghijklmnopqrstuvwxyz1234567890'
  caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  new_str = ""
  rev_new_str = ""
  string = str(word)

  for i in string:
    if i in alpha_nums:
      new_str += i
    elif i in caps:
      new_str += i.lower()
    else:
      continue

  for x in new_str[::-1]:
    rev_new_str += x
    
  return new_str == rev_new_str