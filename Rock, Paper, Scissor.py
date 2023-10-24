#Define Rock Paper Scissor 1 Player. Used for later recusion.
def RPS_1P():
    
    #Obtain players choice.
    player = input('Choose Rock, Paper, or Scissor\n')

    #Covert players choice to upper case for later checks.
    player = player.upper()

    #Check that player entered a viable choice and obtain new choice if necessary.
    while player != 'ROCK' and player != 'PAPER' and player != 'SCISSOR':
        player = input('Please select Rock, Paper, or Scissor\n')
        player = player.upper()

    #Use Random module to select CPU choice.
    import random
    throw = random.randint(1, 3)
    if throw == 1:
        opponent = 'ROCK'
    if throw == 2:
        opponent = 'PAPER'
    if throw == 3:
        opponent = 'SCISSOR'
    print(f'Computer plays', opponent)
        
    #Check CPU choice agaist players choice and determine winner. If tie, play again automatically.
    if opponent == 'ROCK' and player == 'PAPER':
        replay = input('YOU WIN!\nPlay Again?\n')
    elif opponent == 'PAPER' and player == 'SCISSOR':
        replay = input('YOU WIN!\nPlay Again?\n')
    elif opponent == 'SCISSOR' and player == 'ROCK':
        replay = input('YOU WIN!\nPlay Again?\n')
    elif opponent == player:
        print('TIE! Go again!')
        RPS_1P()
    else:
        replay = input('YOU LOSE\nTry Again?\n')
    if replay.upper() == 'YES':
        print('')
        RPS_1P()
    else:
        print('Thank you for playing')

#Define Rock Paper Scissor 2 Player. Used for later recusion.
def RPS_2P():
    
    print('HONOR RULES!\nNO PEAKING!\n')
    
    #Obtain first players choice.
    player = input('Player 1, Choose Rock, Paper, or Scissor\n')

    #Covert players choice to upper case for later checks.
    player = player.upper()

    #Check that player entered a viable choice and obtain new choice if necessary.
    while player != 'ROCK' and player != 'PAPER' and player != 'SCISSOR':
        player = input('Please select Rock, Paper, or Scissor\n')
        player = player.upper()

    #Obtain second players choice.
    opponent = input('Player 2, Choose Rock, Paper, or Scissor\n')

    #Covert players choice to upper case for later checks.
    opponent = opponent.upper()

    #Check that player entered a viable choice and obtain new choice if necessary.
    while opponent != 'ROCK' and opponent != 'PAPER' and opponent != 'SCISSOR':
        opponent = input('Please select Rock, Paper, or Scissor')
        opponent = opponent.upper()
        
    #Check Player 1 choice agaist Player 2 choice and determine winner. If tie, play again automatically.
    if opponent == 'ROCK' and player == 'PAPER':
        replay = input('Player 1 WINS!\nPlay Again?\n')
    elif opponent == 'PAPER' and player == 'SCISSOR':
        replay = input('Player 1 WINS!\nPlay Again?\n')
    elif opponent == 'SCISSOR' and player == 'ROCK':
        replay = input('Player 1 WINS!\nPlay Again?\n')
    elif opponent == player:
        print('TIE! Go again!\n')
        RPS_2P()
    else:
        replay = input('Player 2 WINS!\nPlay Again?\n')
    if replay.upper() =='YES':
        print('')
        RPS_2P()
    else:
        print('Thank you for playing!')

#Ask how many players will be playing the game.
players = ''
#Check that the user entered a valid response.
while players != 'ONE' and players != 'TWO':
    players = input('Please select one or two players\n')

    #Convert input to upper case for later checks.
    players = players.upper()

#Check number of players and direct program appropriately.
if players == 'ONE':
    RPS_1P()

elif players == 'TWO':
    RPS_2P()