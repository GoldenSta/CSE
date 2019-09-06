import string

string = input("Please a string: \n").lower()
reverse_str = ''.join(reversed(string))


if string == reverse_str[::-1]:
    print("{} is a Palindrome String".format(string))
else:
    print("{} isn't not a Palindrome String".format(string))
