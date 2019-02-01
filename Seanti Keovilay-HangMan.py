import string
import random
print("Let's play Hangman.")
word = ['cloud', 'sleep', 'daydream', "midnight", "nightmare", "star", "sun",
        "moon", "Winter", "Summer", "Spring", "Fall", "cherry bomb", "clock"]
letter_guesses = []
guesses_made = 8
random_word = random.choice(word)
playing = True
hidden = list(random_word)

for i in range(len(hidden)):
    if hidden[i] in string.ascii_letters:
        hidden.pop(i)
        hidden.insert(i, "*")

print(hidden)
while guesses_made > 0 and playing:
    letter = input("Guess a letter")
    if letter in letter_guesses:
        print("You guessed this already.")
    if letter in random_word and letter not in letter_guesses:
        print("you guess right")
        print("Guesses left: %d" % guesses_made)
    elif letter not in letter_guesses:
        print("Wrong letter")
        guesses_made -= 1
        print("Guesses left: %d" % guesses_made)
        letter_guesses.append(letter)
    else:
        print("You win")
        playing = False

if not playing:
    print("Winner")
else:
    print("Game Over")

print("Word: %s" % random_word)
