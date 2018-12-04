def challenge1(firstname, lastname):
    return "%s %s" % (lastname, firstname)


print(challenge1("John", "Doe"))


def challenge3(b, h):
    return .5 * b * h


print(challenge3(3, 6))


def challenge5(r):
    return 3.14 * r ** 2


print(challenge5(6))


def challenge6(r):
    return 4/3 * 3.14 * r ** 3


print(challenge6(7))


vowel = ["a", "e", "i", "o", "u"]


def challenge9(letter):
    if letter in vowel:
        return "This is a vowel"
    else:
        return "This isn\'t a vowel"

print(challenge9("a"))

