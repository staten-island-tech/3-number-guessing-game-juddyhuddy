# You will be creating a program that creates a random number and then
# have the user guess the number. The code must contain all of the following
# -Generate a random number between 1 and 10 (you can do more if you
# want)
# -Use a while loop that breaks only when the user correctly guesses the
# number
# -create a guess variable based on user input. There will be a global guess
# variable equal to 0 and then another guess variable inside the while loop
# based on user input
# -using conditional statements, inform the user if their guess is less than or
# greater than the random number
# -push the users incorrect guess into a guess_history list. Print the used
# letters at every wrong guess
# -When the user guesses correctly inform them and show them their guess
# history using a for loop

import random
number = int(input("what is the number between 1 and 10"))

random_integer = random.randint(1,10)
guess_history = [] 
while True:
    if number == random_integer:
        print("correct")
        print(guess_history)
        break

    else:
        guess_history.append(number)
        print("incorrect")
        print(guess_history)
        if number < random_integer:
            print("too low")
        elif number > random_integer:
            print("too high")
        number = int(input("what is the number between 1 and 10"))
        
        
