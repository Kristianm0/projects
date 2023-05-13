"""
Riddle Game

This program generates a random number between a specified range and allows the user to guess the number within a limited number of attempts.

"""

import random

# Initialize variables
guessTaken = 0
minNumber = 1
maxNumber = 20

# Get user's name
print("Hi! What is your name?")
print("Tell me: ")
username = input()

# Generate a random number within the specified range
number = random.randint(minNumber, maxNumber)
print("Great, " + str(username) + "! Let's play:")

# Provide instructions to the user
print("I am thinking of a number between " + str(minNumber) + " and " + str(maxNumber) + "🤓. Write a number and remember that you have 6 tries.")

# Main game loop
while guessTaken < 6:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    # Compare the user's guess with the generated number
    if guess < number:
        print("Your number is too low.")
    elif guess > number:
        print("Your number is too high.")
    else:
        break

# Display the result to the user
if guess == number:
    guessTaken = str(guessTaken)
    print("Good job, " + username + "! You guessed my number in " + guessTaken + " guesses.")
else:
    number = str(number)
    print("No, the number I was thinking of was " + number + ".")
