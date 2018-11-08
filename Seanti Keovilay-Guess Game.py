import random
a = random.randint(1, 10)
guess = 5
playing = True
print("I am thinking of a number between 1 and 10.")

while guess > 0 and playing:
    number_guessed = int(input("Guess a number."))
    if number_guessed > a:
        print("Guess lower.")
        guess -= 1
    elif number_guessed < a:
        print("Guess higher.")
        guess -= 1
    else:
        print("You win.")
        playing = False

if not playing:
    print("Winner")
else:
    print("You lose.")
