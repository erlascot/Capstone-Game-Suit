# Create dictionary of words from text file, keys == length of word, values == words of that length; all upper case.
import urllib.request as url
dict = {}
lib = url.urlopen('https://raw.githubusercontent.com/erlascot/Capstone-Game-Suit/main/google-10000-english-usa.txt')
for word in lib:
    word = word.rstrip()
    l = str(len(word))
    if l not in dict:
        dict[l] = [word.upper()]
    dict[l].append(word.upper())
        
#Have user input desired length of word.
word_len = input('How long of a word do you want?\n')

#Check that user input a number.
while not word_len.isdigit():
    word_len = input('Please enter a number.\n')
    
#Check if the desired word length is in the dictionary.
while 1 > int(word_len) or int(word_len) > 16:
    word_len = input('Please enter a number between 1 and 16.\n')

#Build a bank of possible words based on the desiered length.
word_bank = dict[word_len]

#Convert word_len to integer for later comparisons.
word_len = int(word_len)

#Select a random word from the word bank.
import random
random_index = random.randint(0, len(word_bank))
word = word_bank[random_index]

#Convert word to a list of letters. Used to check user guesses.
word_list = list(word)
for i in range(word_len):
    word_list[i] = chr(word_list[i])
print(word_list)				#TODO: delete this, Temporary for testing.

#Create variables to track correct and incorrect guesses.
hanged_man = 0
correct_guess = 0

#Display blank spaces representing each letter in the word.
word_display = list('_' * word_len)
print(word_display)

#Check if the word has been correctly guessed.
while correct_guess != word_len:
    
    #Check if maximum number of incorrect guesses has been reached.
    if hanged_man == 6:
        print('GAME OVER\nTry Again?')
        break
    
    else:
        #Have user input a letter.
        guess = input('Guess a letter.\n')
        
        #Check that the input is an alphabetic letter.
        while not guess.isalpha():
            guess = input('Please choose a letter.\n')
            
        #Check that only one letter was entered.
        while len(guess) > 1:
            guess = input('Please enter only one letter.\n')
            
        #Convert input into upper case.
        guess = guess.upper()
        
        #Check if guessed letter is in the generated word.
        if guess in word_list:
            #Reveal the placement of the guessed letter in the word to the user.
            for i in range(len(word_list)):
                if word_list[i] in guess:
                    word_display[i] = guess
                    #Increment correct guess for game winning condition.
                    correct_guess += 1
            print(word_display)
        
        #Increment hanged_man for incorrect guesses and notify user of how many attmpts they have left.
        else:
            hanged_man += 1
            print(f'Your Hanged Man has', 6 - hanged_man, 'chances left')
            #TODO: add to hanged man graphic.

#Check for winning condition and notify user.
if correct_guess == word_len:
    print('YOU WIN!\nPlay Again?')
