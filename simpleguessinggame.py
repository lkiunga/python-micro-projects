import random
from random import randrange
# Simple Guessing Game
# In this game the user guess a randomly generated number within a certain range.
# The game provides feedback to the user if their guess is too high or too low 
# Until they correctly guess the number right
#Get user input
#Give user 3 tries
userTries = 3


#Computer game function
#User while loop to give the player more tries
while userTries > 0:
    userTries -=1
    #Get user input
    userInput = int(input("Guess a Number between range 10 and 50 "))
    #Random computer Generated Number
    computerGeneratedNumber = randrange(10,50)
    print ("Computer Guess is ", computerGeneratedNumber)

    #Condition testing
    if userInput == computerGeneratedNumber:
        print("You won in ",userTries, "try")
        #if true - end game
        break
    # if not give feedback and play till end 
    elif userInput > computerGeneratedNumber:
        print ("User Guess too high")
    elif userInput < computerGeneratedNumber:
        print("Your guess is too low")
if userTries == 0:
    print("Your out of tries, Better luck next time")

