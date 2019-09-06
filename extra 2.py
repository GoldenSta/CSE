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

password = "Olympus"
passwordLength = len(password)
print(passwordLength)

word = "Sydney"
middleLetter = len(word) / 2
middleLetter = int(middleLetter)
print(word[middleLetter-1:middleLetter])

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

my_string = "Monty Python"
print(my_string[1:3:4])
