import string

string = input("Please a string: \n")
reverse_str = string[::-1]


if string == reverse_str[::-1]:
    print("This is a Palindrome String")
else:
    print("This is not a Palindrome String")
