# Inspiration code from https://www.geeksforgeeks.org/implementation-of-tic-tac-toe-game/#


# Set up the game board as a list.
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def print_board():
    """Prints the board so the players can track the game."""
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--" + "|" + "---" + "|" + "--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--" + "|" + "---" + "|" + "--")
    print(board[6] + " | " + board[7] + " | " + board[8])


def take_turn(player):
    """Handles the player input for turn flow."""
    
    # Notifies which players turn it is.
    print(player + "'s turn.")
    
    # Player picks a square.
    position = input("Choose a position from 1-9: ")
    
    # Checks that player input a valid option.
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")
        
    # Converts player input to index number for assignment to board list.
    position = int(position) - 1
    
    # Checks that input index is available and get a new input if necessary.
    while board[position] == "X" or board[position] == "O":
        position = input("Position already taken. Choose a different position: ")
        
        # Chekcs that player input a valid option.
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
            
        # Converts player input to index number for assignment to board list.
        position = int(position) - 1
    
    # Assigns current player character to selected square.
    board[position] = player
    
    # Print the updated board.
    print_board()

def check_game_over():
    """Checks the condition of the board to determ in game is over or should continue."""

    # Check for a win
    if (
        (board[0] == board[1] == board[2])
        or (board[3] == board[4] == board[5])
        or (board[6] == board[7] == board[8])
        or (board[0] == board[3] == board[6])
        or (board[1] == board[4] == board[7])
        or (board[2] == board[5] == board[8])
        or (board[0] == board[4] == board[8])
        or (board[2] == board[4] == board[6])
    ):
        return "win"

    # Check for a tie
    elif (
        (board[0] == "X" or board[0] == "O")
        and (board[1] == "X" or board[1] == "O")
        and (board[2] == "X" or board[2] == "O")
        and (board[3] == "X" or board[3] == "O")
        and (board[4] == "X" or board[4] == "O")
        and (board[5] == "X" or board[5] == "O")
        and (board[6] == "X" or board[6] == "O")
        and (board[7] == "X" or board[7] == "O")
        and (board[8] == "X" or board[8] == "O")
    ):
        return "tie"

    # Play continues
    else:
        return "play"


# The main game loop
print_board()
current_player = "X"
game_over = False
while not game_over:
    take_turn(current_player)
    game_result = check_game_over()
    if game_result == "win":
        print(current_player + " wins!\nPlay Again?")
        game_over = True
    elif game_result == "tie":
        print("It's a tie!\nPlay Again?")
        game_over = True
    else:
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"
