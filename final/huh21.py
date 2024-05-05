def acceptableChars(str):
   validation = set(str)
   if validation.issubset(acceptable_chars):
      return True
   else:
      return False 
      
acceptable_chars = set('0123456789')
str1 = "1234654185"
print(acceptableChars(str1))