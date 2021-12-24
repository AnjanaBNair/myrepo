theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
# theBoard is the dictionary of the the board when it is empty

theNumBoard = {'1': '1', '2': '2', '3': '3',
               '4': '4', '5': '5', '6': '6',
               '7': '7', '8': '8', '9': '9'}
# theNumBoard show the players the position to enter their input


def ticTacToe(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


ticTacToe(theNumBoard)
# ticTacToe(theBoard)

turn = 'X'
repeat = 'y'
xWins = 0   # This is the variable for the wins of player X
oWins = 0   # This is the variable for the wins of player 0
draws = 0   # This is the variable for no winner

spaceRemaining = 9  # This to check the amount of spaces remaining

while repeat == 'y' or repeat == 'Y':   # The main game loop
    ticTacToe(theBoard)  # This prints the board
    for i in range(20):
        # The range ought to be range(9), but this used because when the user makes an invalid moves, it also counts,
        # thus this gives room for the players to make mistake up to 10 times

        try:  # This handles errors when a value that is not an integer is inputted
            print('It is player ' + turn + ' turn. Choose a space')
            position = int(input())
        except ValueError:
            print('\033[0;31;40m' + 'Invalid Entry' + '\033[0;0m')
            continue

        try:  # This check if the position input is one of the KEY values of theBoard dictionary.
            # That is, we ensure that the values inputted are from 1 to 9,
            if theBoard[str(position)] != ' ':
                # This notifies the players when a previously selected cell is selected again

                print('\033[0;31;40m' + 'Space filled. Try another.' + '\033[0;0m')

                # \033[0;31;40m add a red color (31), and a black background (40m). O means *normal* font
                # \033[0;0m ensure that this color formatting does not go to the next line

                continue
        except KeyError:  # if it is not one of the KEYS, this is displayed and player asked to try another entry
            print('\033[0;31;40m' + 'Wrong index. Input between spaces 1 to 9' + '\033[0;0m')
            continue

        theBoard[str(position)] = turn  # This enter either X or O based on the position chosen

        ticTacToe(theBoard)  # This displays the board after each entry by the users

        # To determine who plays next
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        # To check if there is a winner
        if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # First row
            print('\033[0;32;40m' + theBoard['1'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # Second row
            print('\033[0;32;40m' + theBoard['4'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # Third row
            print('\033[0;32;40m' + theBoard['7'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # First column
            print('\033[0;32;40m' + theBoard['1'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # Second column
            print('\033[0;32;40m' + theBoard['2'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # Third column
            print('\033[0;32;40m' + theBoard['3'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # Backward slash diagonal
            print('\033[0;32;40m' + theBoard['1'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))

            break

        elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':  # Forward slash diagonal
            print('\033[0;32;40m' + theBoard['3'] + ' is the winner' + '\033[0;0m')

            # This checks who wins and inputs their score
            if theBoard['1'] == 'X':
                xWins = xWins + 1
            else:
                oWins = oWins + 1

            # print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws)) # string interpolation
            print(f'X: {xWins}, O: {oWins}, Draw: {draws}')  #f-strings
            # f-strings and string interpolation serves the same purpose

            break
        spaceRemaining = spaceRemaining - 1

        # This tells after nine rounds and there is no winner that it is a draw
        if spaceRemaining == 0:  # if the spaces remains 0, we alert the players that the game is a draw.
            print('\033[0;32;40m' + 'It is a draw' + '\033[0;0m')
            draws = draws + 1
            print('X: %s, O: %s, Draw: %s' % (xWins, oWins, draws))
            break

    # We ask the players if they wish to continue
    print('\033[0;33;40m' + 'Do you wish to continue? (y)es or (n)o' + '\033[0;0m')
    repeat = input()

    if repeat == 'y' or repeat == 'Y':  # This loop is used to empty the values of the keys before the game continues
        for key in theBoard:
            theBoard[key] = ' '
    # From this the player who starts is the one who lost the game