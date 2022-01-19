# THIS IS A "ROCK PAPER SCISSORS" GAME
# COMPUTER VERSUS HUMAN
# ROCK > SCISSORS
# PAPER > ROCK
# SCISSORS > PAPER

import random       # To generate a random output.

def game():

    # VARIABLES
    # Variables for the score record.
    wins = 0
    losses = 0
    draws = 0

    # MAIN LOOP
    while True:
        # Using fstring to print out the score of players.
        # Used ANSI escape codes for the colours.

        # \033[7;32;40m gives a green background, and black text.
        print('\033[7;32;40m' + f'Wins: {wins}; Losses: {losses}; Draws: {draws}' + '\033[0;0m')


        # LIST OF CHOICES
        # This is a list of choices the player and the computer are allowed can make.
        gameChoices = ['r', 'p', 's', 'e']      # r-rock, p-paper, s-scissors, e-exit
        computerGameChoices = ['r', 'p', 's']

        # RANDOM CHOICE FOR THE COMPUTER
        computerChoice = random.choice(computerGameChoices)

        # PLAYER'S CHOICE
        print('r-rock, p-paper, s-scissors, e-exit')
        userChoice = input('Choose between r, s, p, and e \n')

        # PLAYERS WINS
        if userChoice.lower() == 'r' and computerChoice == 's':
            print('ROCK VS SCISSORS')
            print('You win! \n')
            wins = wins + 1
        elif userChoice.lower() == 's' and computerChoice == 'p':
            print('SCISSORS VS PAPER')
            print('You win! \n')
            wins = wins + 1
        elif userChoice.lower() == 'p' and computerChoice == 'r':
            print('PAPER VS ROCK')
            print('You win! \n')
            wins = wins + 1

        # PLAYER LOSES
        elif userChoice.lower() == 's' and computerChoice == 'r':
            print('SCISSORS VS ROCK')
            print('You lose \n')
            losses = losses + 1
        elif userChoice.lower() == 'p' and computerChoice == 's':
            print('PAPER VS SCISSORS')
            print('You lose \n')
            losses = losses + 1
        elif userChoice.lower() == 'r' and computerChoice == 'p':
            print('ROCK VS PAPER')
            print('You lose \n')
            losses = losses + 1

        # DRAW
        elif userChoice.lower() == 's' and computerChoice == 's':
            print('SCISSORS VS SCISSORS')
            print('It is a draw \n')
            draws = draws + 1
        elif userChoice.lower() == 'p' and computerChoice == 'p':
            print('PAPER VS PAPER')
            print('It is a draw \n')
            draws = draws + 1
        elif userChoice.lower() == 'r' and computerChoice == 'r':
            print('ROCK VS ROCK')
            print('It is a draw \n')
            draws = draws + 1

        # T0 EXIT THE GAME
        if userChoice.lower() == 'e':
            if wins > losses:
                print('\033[7;34;40m' + 'Well done, you beat me.' + '\033[0;0m')
                # \033[7;34;40m gives a black text on a blue background
                break
            elif losses > wins:
                print('\033[7;34;40m' + 'So sorry, I beat you. Try next time.' + '\033[0;0m')
                break
            elif losses == wins and draws != 0:
                print('\033[7;34;40m' + 'It is a draw. Try beating me next time.' + '\033[0;0m')
                break
            elif losses == wins and wins != 0:
                print('\033[7;34;40m' + 'It is a draw. Try beating me next time.' + '\033[0;0m')
                break
            else:
                break

        # INVALID INPUT
        # If the user inputs an invalid letter, there are taken back to the start of the loop
        if userChoice.lower() not in gameChoices:
            print('\033[0;31;40m' + 'Please, choose between r, s, and p' + '\033[0;0m \n')
            # \033[0;31;40m gives a red text on a black background
            continue

# Vaiable for restarting the program
repeat = 'y'

while repeat.lower() == 'y':
    game()      # Calling the game function

    repeat = input('Do you which to restart the game? y - yes, n - no \n')

    if repeat.lower() == 'y':
        continue
    else:
        break
