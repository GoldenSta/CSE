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
