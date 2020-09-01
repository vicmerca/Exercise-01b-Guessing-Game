import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"
import random
number = random.randint(0,10)
approval = 0
while approval != 1:
    guess = input("Guess a number from 1 to 10: ")
    if int(guess) != number:
        print("Try again")
    elif int(guess) == number:
        approval = 1
        print("Great job! You got it!")
    else:
        print("That was not a number...")