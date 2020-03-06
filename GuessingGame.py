import random

random_number = random.randint(1,10)
guess = None

while guess != random_number:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!")

print(guess)

# handle user guesses
# if they guess corrrect, tell them they won
# otherwise tell them if they are too high or too low

# Bonus - let player play again if they want!