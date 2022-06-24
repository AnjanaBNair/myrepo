# tic_tac_toe.py - Tic-tac-toe game between two players.
# Player 1 would be X; while player two would be O

import os                   # To clear screen.
import platform             # To check the operating system in use for clearing of the screen.

# theBoard is the dictionary of the board when it is empty.
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

# theNumBoard shows the players where to enter their input.
theNumBoard = {'1': '1', '2': '2', '3': '3',
               '4': '4', '5': '5', '6': '5',
               '7': '7', '8': '8', '9': '9'}


# Function to print out the board in an ordered form.
def ticTacToe(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# Score Variables
playerOneWins = 0
playerTwoWins = 0
draws = 0

repeat = 'y'    # For the main game loop
turn = 'X'      # First player is player 1 (X)
loop = True     # For game loop used to break out of loop from function when there is a win

# Players' Details
playerOne = input('Player 1 Name: ')
playerTwo = input('Player 2 Name: ')
print(playerOne + ': X')
print(playerTwo + ': O')

# Print board with numbers to indicate position.
ticTacToe(theNumBoard)


# Function to check if a player has won.
def win(value1, value2, value3):
    """win() checks the tic-tac-toe board values against the possible wins combination to know if a player has won"""
    if theBoard[value1] == theBoard[value2] == theBoard[value3] != ' ':
        print('\033[0;32;40m' + theBoard[value1] + ' is the winner' + '\033[0;0m')

        # global keyword allows the global variables to be changed in the function
        global playerOneWins
        global playerTwoWins
        global loop

        # Check which of the players won
        if theBoard[value1] == 'X':
            playerOneWins = playerOneWins + 1

            loop = False
            return loop
        else:
            playerTwoWins = playerTwoWins + 1

            loop = False
            return loop


# Main program loop
while repeat.lower() == 'y':

    loop = True
    # This used to determine the draw between the players. It is decreases with each player's input.
    # When the whole box is filled, spaceRemaining = 0 and no winner, the game is a draw.
    spaceRemaining = 9

    # Print an empty board
    ticTacToe(theBoard)

    while loop is True:
        # Ask players for input
        position = input('It is player ' + turn + ' turn: ')

        # This check if the position is empty and also handles key Error
        try:
            if theBoard[position] != ' ':
                # '\033[0;31;40m' - black background, red text.
                print('\033[0;31;40m' + 'Already filled. Choose an empty slot' + '\033[0;0m')
                continue
        except KeyError:
            # '\033[0;31;40m' - black background, red text.
            print('\033[0;31;40m' + 'Invalid! Choose between 1 to 9.' + '\033[0;0m')
            continue

        # Updates theBoard with player's input
        theBoard[position] = turn

        # CLEAR SCREEN
        # Clear screen for Windows
        if platform.system().lower() == "windows":
            os.system('cls')

        # Clear screen for other operating systems
        else:
            os.system('clear')

        # Print the new board.
        ticTacToe(theBoard)

        # Alternates player's turns
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # POSSIBLE WINS PATTERNS
        # Check if a player has won

        # First Row
        win('1', '2', '3')

        # Second Row
        win('4', '5', '6')

        # Third Row
        win('7', '8', '9')

        # First Column
        win('1', '4', '7')

        # Second Column
        win('2', '5', '8')

        # Third Column
        win('3', '6', '9')

        # / Forward Slash Diagonal
        win('3', '5', '7')

        # \ Backward Slash Diagonal
        win('1', '5', '9')

        # DRAW
        # Check if all the spaces are filled with no winner
        spaceRemaining = spaceRemaining - 1

        # Check if the board is filled up.
        if spaceRemaining == 0 and loop is True:
            # '\033[0;33;40m' - black background, yellow text.
            print('\033[0;33;40m' + 'It is a draw!' + '\033[0;0m')
            draws = draws + 1

            break

    # SCORE BOARD
    # Print the score board after a win or draw
    # '\033[7;32;40m' - Green background, black text.
    print('\033[7;32;40m' + '%s: %s; %s: %s; Draw: %s'
          % (playerOne.title(), playerOneWins, playerTwo.title(), playerTwoWins, draws) + '\033[0;0m')

    # Ask players if they want to continue the game
    # '\033[0;33;40m' - black background, yellow text.
    repeat = input('\033[0;33;40m' + 'Do you wish to continue? [y]es or [n]o: ' + '\033[0;0m')

    if repeat.lower() == 'y':

        # Empty the dictionary values of the game to start afresh
        for keys in theBoard:
            theBoard[keys] = ' '

        # If the players chooses to continue, the player who lost this round starts the next,
        # but if you want the winner to continue, uncomment the code below.

        # if turn == 'X':
            # turn = '0'
        # else:
            # turn = 'X'

        continue

    else:
        break
