import string
import random
print("Let's play Hangman.")
word = ['clock', 'sleep', 'daydream', "midnight", "nightmare", "star",
        "sun", "moon", "Winter", "Summer", "Spring", "Fall", "cherry bomb"]
letter_guesses = 0
guesses_made = {}
letter_guessed_right = {}
print(list(string.ascii_letters))
playing = True

while guesses_made