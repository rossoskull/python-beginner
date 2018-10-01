import random

found = False
secret_number = random.randint(1,101)

guess = int(input("Guess a number between 1 and 100: "))

while not found:

    if guess > secret_number:
        guess = int(input("Your guess was too high. Try again: "))
    elif guess < secret_number:
        guess = int(input("Your guess was too low. Try again: "))
    else:
        print("You guessed it right! Congratulations!")
        found = True
