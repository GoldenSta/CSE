a = 5
b = 10
c = 100


def add(x, y):
    x = x + 5
    y = y - 15
    sum = x + y
    print(sum)


def subtract(w, v):
    w = w * 5
    v = v + 5
    if w > v:
        sub = w-v
    else:
        sub = v-w
    print(sub)


add(a, c)
subtract(a, c)


def add(x, y):
    sum = x+y
    print(sum)


add(2, 7)


def odd(x):
    if x % 2 == 0:
        return ("even")
    else:
        return ("odd")


def divisible_by_3(w):
    if w % 3 == 0:
        return ("multiple of three")
    else:
        return ("not a multiple of three")


print(odd(10))
print(divisible_by_3(10))


s = 2
t = 4
u = 6


def add(x, y):
    x = x + 9
    y = y - 3
    sum = x + y
    print(sum)


def multiple_by_2(d, g):
    d = d * 5
    g = g * 5
    if d > g:
        sub = d * g
    else:
        sub = g * d
    print(sub)


add(s, t)
multiple_by_2(u, s)


def add(x, y):
    sum = x+y
    return sum


add(2, 7)

productName = "The Hobbit"
print(productName)

footballTeam = "Dunfermline" + "Football" + "Club"
print(footballTeam)

dogBreed = "Labradoodle"
print(dogBreed + dogBreed)

firstName = "Walter"
surname = "White"
print(firstName[0:3] + surname[0:3])

filmRelease = "World War Z"
releaseDate = "31st OCT"
tempFilm = filmRelease.upper()
tempDate = releaseDate.lower()
print(tempFilm + "" + tempDate)

word1 = "central"
word2 = "processing"
word3 = "unit"
word4 = word1[0:1].upper()
word5 = word2[0:1].upper()
word6 = word3[0:1].upper()
print(word4 + " = " + word1)
print(word5 + " = " + word2)
print(word6 + " = " + word3)

password = "spider man"
passwordLength = len(password)
print(passwordLength)

statement = "When Mr. Bilbo Baggins of Bag End announced"
letter1position = statement.count("a")
letter2position = statement.count("e")
letter3position = statement.count("i")
letter4position = statement.count("o")
letter1 = statement[letter1position-1:letter1position]
letter2 = statement[letter2position-1:letter2position]
letter3 = statement[letter3position-1:letter3position]
letter4 = statement[letter4position-1:letter4position]
password = letter4 + letter2 + letter3 + letter1
print(password)
