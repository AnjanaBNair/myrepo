import random, sys

# Global varibles
wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True:
    print('\n %s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

    playerMove = input()

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    elif playerMove == 'q':
        sys.exit()
    else:
        print('Invalid input')
        continue

    computerMove = random.randint(1, 3)

    if computerMove == 1:
        computerMove = 'r'
        print('ROCK')
    elif computerMove == 2:
        computerMove = 'p'
        print('PAPER')
    elif computerMove == 3:
        computerMove = 's'
        print('SCISSORS')


    if playerMove == computerMove:
        ties = ties + 1
        print('It is a tie')

    elif playerMove == 'r' and computerMove == 's':
        wins = wins + 1
        print('You win!')
    elif playerMove == 'p' and computerMove == 'r':
        wins = wins + 1
        print('You win!')
    elif playerMove == 's' and computerMove == 'p':
        wins = wins + 1
        print('You win!')

    elif playerMove == 's' and computerMove == 'r':
        losses = losses + 1
        print('You lose!')
    elif playerMove == 'r' and computerMove == 'p':
        losses = losses + 1
        print('You lose!')
    elif playerMove == 'p' and computerMove == 's':
        losses = losses + 1
        print('You lose!')
