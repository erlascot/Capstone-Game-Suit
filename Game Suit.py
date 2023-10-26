# Get user input to direct the program.
game = input(
    "Please choose a game. Hangman, Number Guess, TicTacToe, or Rock Paper Sciccor"
)

# Convert input to upper case for later comparison.
game = game.upper()

# Check that user entered a valid input and get new input if necessary.
while (
    game != "HANGMAN"
    and game != "NUMBER GUESS"
    and game != "TICTACTOE"
    and game != "ROCK PAPER SCICCOR"
):
    game = input(
        "Please choose one of the available games. Hangman, Number Guess, TicTacToe, or Rock Paper Sciccor"
    )
    game = game.upper()

# Launch the appropriate file based on user input.
if game == "HANGMAN":
    import Hangman
if game == "NUMBER GUESS":
    import Number_Guesser
if game == "TICTACTOE":
    import TicTacToe
if game == "ROCK PAPER SCICCOR":
    import Rock_Paper_Sciccor
