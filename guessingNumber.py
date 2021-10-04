import random
import math

# Getting inputs
lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

# Generating random number between the lower and the upper sing the random function
randomNum = random.randint(lower, upper)
print("\n\tYou have only ", round(math.log(upper - lower + 1, 2)),
" chances to guess the integer!\n")

# Initializng the number of guesses
count = 0

while count < math.log(upper - lower + 1, 2):
    count +=1

    guess = int(input("Guess a number: "))

    if randomNum == guess: 
        print("Congrats, you guessed the number right in ", count, "tries!")

        break
    elif randomNum > guess:
        print("You guessed too small.")
    elif randomNum < guess: 
        print("You guessed too high.")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % randomNum)
    print("\tBetter luck next time!")