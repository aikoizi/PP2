def palindrome(text):
    return text == ''.join(reversed(text))

string = "nolemonnomelon"

if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
