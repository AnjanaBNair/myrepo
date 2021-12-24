# Conversion of Temperature
import sys

while True:
    print('Temperature Conversion')
    print('Celsius to Fahrenheit, Click C \n'
          'Fahrenheit to Celsius, Click F')

    userChoice = input()  # This input the user choice between C and F

    if userChoice == 'c' or userChoice == 'C':
        while True:
            print('Please, input the value of the temperature you want to convert to Fahrenheit')

            try:
                celsius = float(input())

                celsiusToFah = (9.0/5.0)*celsius + 32.0

                print('\033[0;31;40m' + str(celsius) + ' celsius is ' + str(celsiusToFah) + ' Fahrenheit' + '\033[0;0m')
                break
            except ValueError:
                print('\033[0;31;40m' + 'Please, input a numeric value.' + '\033[0;0m')
                continue

            # If the user input a non numeric value, the user is taken back to the beginning
            # This needs a solution
            # How to return to the beginning of an if function

    elif userChoice == 'f' or userChoice == 'F':
        print('Please, input the value of the temperature you want to convert to Celsius')
        while True:
            try:
                fahrenheit = float(input())

                fahToCelsius = (5.0 / 9.0) * (fahrenheit - 32.0)

                print('\033[0;31;40m' + str(fahrenheit) + ' Fahrenheit is ' + str(fahToCelsius) + ' Celsius' + '\033[0;0m')
                break
            except ValueError:
                print('Please, input a numeric value.')
                continue

            # If the user input a non numeric value, the user is taken back to the beginning
            # This needs a solution

    else:
        print('Please, input the either F or C')
        continue

    print('Do you wish to do another conversion? (Y)es or (N)o.')
    repeatChoice = input()

    if repeatChoice == 'y' or repeatChoice == 'Y':
        continue

    elif repeatChoice != 'y' or repeatChoice != 'Y':
        sys.exit()