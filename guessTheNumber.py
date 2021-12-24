import random

realNum = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')


for guessTaken in range(1, 7):
    print('Take a guess. You have 6 chances')
    guessNum = int(input())

    if guessNum > realNum:
        print('Your guess is too high')
    elif guessNum < realNum:
        print('Your guess is too low')
    else:
        break

if guessNum == realNum:
    print('Good job')
    print('You were able to guess my number in ' + str(guessTaken) + ' guesses')

else:
    print('Nope. The number I was thinking of is ' + str(realNum))