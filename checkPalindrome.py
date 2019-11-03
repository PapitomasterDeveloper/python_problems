# Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.

# Note: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc.

def check_palindrome(word):
    return word[::-1] == word
    #Remove pass and write your logic here

status=check_palindrome("malayalam")
# status=check_palindrome("malayalam	")
# status=check_palindrome("mango")
# status=check_palindrome("laptop")
# status=check_palindrome("MADAM")

if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
