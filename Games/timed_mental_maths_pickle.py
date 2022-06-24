# Timed Mental Maths

import random           # For randint
import pickle           # For storing the high score
import time

# Dummy variable when the game has not been played at all
high_score_dict = {'Player Name': 'Anonymous', 'Score': 0}

# Read into the high score file to print high score and high scorer's name
try:
    filename = 'high_score'
    infile = open(filename, 'rb')
    high_score = pickle.load(infile)

    # try ... except used when the game is yet to be played and the high score has not been created
    # The dummy variable is printed.
except FileNotFoundError:
    high_score = high_score_dict
    pass

# Print High Score
print('\033[7;32;40m' + 'High score' '\033[0;0m\n' + high_score['Player Name'] + ': ' + str(high_score['Score']) + '\n')

player_name = input("Name: ")

# List of operators used in the game
operators = ['*', '/', '+', '-']
random_operator = operators[random.randint(0, 3)]

player_lives = 3
player_score = 0

print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')


def operation(random_op1, random_op2, game_seconds):
    # To be able to change the global variable, the 'global' keyword is used

    global player_lives
    global player_score
    start_time = time.time()
    player_answer = ""

    print('You have ' + str(game_seconds) + ' seconds')

    while player_answer == "":
        # try ... except to catch ValueError
        try:
            # This prints out the algebraic operation to the screen
            print(str(random_op1) + str(random_operator) + str(random_op2))
            player_answer = int(input("Answer: "))
        except ValueError:
            print('\033[0;31;40m' + 'Invalid input! Input an integer.' + '\033[0;0m')
            continue

        if player_answer != "":
            break

    # Check if question was answered before the time elapsed
    time_used = int(time.time() - start_time)
    remaining_sec = game_seconds - time_used

    if remaining_sec <= 0:
        print('Time up!')
        player_lives = player_lives - 1
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # MULTIPLICATION
    elif random_operator == operators[0]:
        if player_answer == random_op1 * random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score)

        else:
            print('Wrong! The answer is ' + str(random_op1 * random_op2))
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # DIVISION
    elif random_operator == operators[1]:
        if player_answer == random_op1 / random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score)

        else:
            print('Wrong! The answer is ' + str(int(random_op1 / random_op2)))
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # ADDITION
    elif random_operator == operators[2]:
        if player_answer == random_op1 + random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score)

        else:
            print('Wrong! The answer is ' + str(random_op1 + random_op2))
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    # SUBTRACTION
    elif random_operator == operators[3]:
        if player_answer == random_op1 - random_op2:
            player_score = player_score + (remaining_sec * 10)
            print('Player score:', player_score)

        else:
            print('Wrong! The answer is ' + str(random_op1 - random_op2))
            player_lives = player_lives - 1
            print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')


# The game continues so long the player life goes not depletes to 0.
while player_lives > 0:

    # LEVEL: Very Easy
    game_sec1 = 10

    while player_score < 1500 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand1 = random.randint(0, 9)
        random_operand2 = random.randint(1, 9)  # This starts from 1 to avoid ZeroDivisionError

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers)
        if (random_operator == operators[1]) and (random_operand1 % random_operand2 != 0):
            continue

        # Calling the operation function
        operation(random_operand1, random_operand2, game_sec1)

    # LEVEL: Easy
    if player_score > 1500:
        player_lives = player_lives + 2
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score >= 1500 and player_score < 3500 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand3 = random.randint(0, 99)
        random_operand4 = random.randint(1, 20)  # This starts from 1 to avoid ZeroDivisionError

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers)
        if (random_operator == operators[1]) and (random_operand3 % random_operand4 != 0):
            continue

        # Calling the operation function
        operation(random_operand3, random_operand4, game_sec1)

    # LEVEL: Medium
    if player_score > 3500:
        player_lives = player_lives + 2
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score >= 3500 and player_score < 10000 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand5 = random.randint(0, 99)
        random_operand6 = random.randint(1, 50)  # This starts from 1 to avoid ZeroDivisionError
        game_sec2 = 15

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers)
        if (random_operator == operators[1]) and (random_operand5 % random_operand6 != 0):
            continue

        # Calling the operation function
        operation(random_operand5, random_operand6, game_sec2)

    # LEVEL: Hard
    if player_score > 10000:
        player_lives = player_lives + 3
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score >= 10000 and player_score < 25000 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand7 = random.randint(0, 999)
        random_operand8 = random.randint(1, 100)  # This starts from 1 to avoid ZeroDivisionError
        game_sec3 = 20

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers)
        if (random_operator == operators[1]) and (random_operand7 % random_operand8 != 0):
            continue

        # Calling the operation function
        operation(random_operand7, random_operand8, game_sec3)

    # LEVEL: Very Hard
    if player_score > 25000:
        player_lives = player_lives + 5
        print('\033[0;31;40m' + 'Life: ' + str(player_lives) + '\033[0;0m')

    while player_score > 25000 and player_lives != 0:
        random_operator = operators[random.randint(0, 3)]
        random_operand9 = random.randint(0, 999)
        random_operand10 = random.randint(1, 400)  # This starts from 1 to avoid ZeroDivisionError
        game_sec4 = 25

        # This ensures that the generated numbers are always divisible (that is, they don't give decimal numbers)
        if (random_operator == operators[1]) and (random_operand9 % random_operand10 != 0):
            continue

        # Calling the operation function
        operation(random_operand9, random_operand10, game_sec4)

if player_lives == 0:
    print('Game Over!')
    print('\033[0;33;40m' + 'Your score: ' + str(player_score) + '\033[0;0m')

# Check if player score is higher than high score

if player_score > high_score_dict['Score']:
    high_score_dict['Score'] = player_score
    high_score_dict['Player Name'] = player_name.title()

    filename = 'high_score'
    outfile = open(filename, 'wb')
    pickle.dump(high_score_dict, outfile)

    print('\033[30;32;40m' + 'New High Score!' + '\033[0;0m')

# TODO: Break out of question if the time elapse before the player enters an answer
