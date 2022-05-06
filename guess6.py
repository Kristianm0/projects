## Riddle

import random

guessTaken = 0
minNumber = 1
maxNumber = 20

print("Hi What is your name?")
print("Tell me: ")
username = input()

number = random.randint(minNumber, maxNumber)
print("Great " + str(username) +" Let's go to play:")

print ("i am thinking in a number between " + str(minNumber) + " and " + str(maxNumber) + "🤓. Write a number and remenber that you have 6 time")

while guessTaken < 8:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < number:
        print("Your number is too low.")
    if guess > number:
        print("Your number is too high.")
    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken)
    print("Good Job " + username + "! you gussed my number in " + guessTaken + " guesses")
if guess != number:
    number = str(number)
    print("No the number i was thinking of was " + number)


## Task you have to result the bug