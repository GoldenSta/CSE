import string
import random
print("Let's play Hangman.")
word = ['cloud', 'sleep', 'daydream', "midnight", "nightmare", "star",
        "sun", "moon", "Winter", "Summer", "Spring", "Fall", "cherry bomb"]
letter_guesses = 0
guesses_made = {}
letter_guessed_right = {}
random_word = random.choice(word)
playing = True

while guesses_made < 0 and playing:
        letter = input("Guess a letter")
        if letter in random_word and letter not in letter_guesses:
                print("you guess right")
                guesses_made += 1
                print("Number of guesses %d" % guesses_made)
