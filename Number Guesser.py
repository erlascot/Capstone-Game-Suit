#Have user input maximum range for possible numbers to guess.
max_range = input('Select the max range of possible numbers then press "ENTER"\n')

#Check that user input a number and obtain new input if necessary.
while not max_range.isdigit():
    max_range = input('Please enter a number\n')

#Use random module to generate a number between 1 and users max range input.
import random
number = random.randint(1, int(max_range))

#Define the guessing process and set a guesses counter to 1.
def guessing(guesses=1):
    
    #Ask user for a guess number.
    guess = input('Guess a number then press "ENTER"\n')
    
    #Confirm user entered a number and obtain a new guess if necessary.
    while not guess.isdigit():
        guess = input('Please guess a number\n')
    
    #Convert guess from a string to an integer
    guess_int = int(guess)

    #Check if guessed number is the same as generated number.
    if guess_int == number:
        print('Congratulations! It took you', guesses, 'attempts to guess the number!')
        
    #Provide feedback to user to guide them to the correct number and increase guess count.
    elif guess_int < number:
        print('My number is higher. Try again.\n')
        guessing(guesses+1)
    elif guess_int > number:
        print('My number is lower. Try again.\n')
        guessing(guesses+1)

guessing()