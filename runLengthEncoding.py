# Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

# Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

# Provide different String values and test your program

# Sample Input
# AAAABBBBCCCCCCCC

# Expected Output
# 4A4B8C

# Sample Input
# AABCCA

# Expected Output
# 2A1B2C1A

def encode(message):
  s = set(message)
  d = dict.fromkeys(s, 0)
  for i in range(0, len(message)):
    if(message[i] in s):
      d.update({message[i]:d.get(message[i]) + 1})
    #Remove pass and write your logic here

  return("".join((str(a) + str(b)) for a,b in d.items()))

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
