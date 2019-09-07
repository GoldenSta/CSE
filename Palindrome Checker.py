import string
print(string.punctuation)

String = input("Please add a string: \n").lower()
reverse_str = ''
String = String.replace(" ", "")
reverse_str = reverse_str.replace(" ", "")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
str1 = ''


for char in String:
    if char not in punctuations:
        no_punct = no_punct + char


def isPalindrome(s):
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False


for i in String:
    str1 = i + str1
print("String in reverse Order :", str1)


if String == str1:
    print("%s is a Palindrome String" % no_punct)
else:
    print("%s isn't a Palindrome String" % no_punct)
