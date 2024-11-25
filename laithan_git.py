print("Hello World!")

import random
import os

guess = "Random number: ", random.randint(1, 10)
inpt = input("Enter a number between 1 and 10: ")

if int(inpt) == guess:
    print("You got it!")
else:
    print("You didn't get it! Try again.")