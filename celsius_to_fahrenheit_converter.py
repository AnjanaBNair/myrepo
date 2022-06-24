# celsius_to_fahrenheit_converter.py - Converts Celsius to Fahrenheit and vice versa.
import sys

while True:         # Main program loop
    print('Temperature Conversion')
    print('Celsius to Fahrenheit, Click C \n'
          'Fahrenheit to Celsius, Click F')

    userChoice = input()  # This input the user choice between C and F

    # Celsius to Fahrenheit Conversion
    if userChoice == 'c' or userChoice == 'C':
        while True:           # If users inputs a non numeric value for the conversion, they are returned here
            print('Please, input the value of the temperature you want to convert to Fahrenheit')

            try:
                celsius = float(input())

                celsiusToFah = (9.0/5.0)*celsius + 32.0

                print('\033[0;31;40m' + str(celsius) + ' celsius is ' + str(celsiusToFah) + ' Fahrenheit' + '\033[0;0m')
                break
            except ValueError:          # This checks if the inputed a non numeric value
                print('\033[0;31;40m' + 'Please, input a numeric value.' + '\033[0;0m')
                continue
 
    # Fahrenheit to Celsius Conversion
    elif userChoice == 'f' or userChoice == 'F':
        print('Please, input the value of the temperature you want to convert to Celsius')
        
        while True:         # If users inputs a non numeric value for the conversion, they are returned here
            try:
                fahrenheit = float(input())

                fahToCelsius = (5.0 / 9.0) * (fahrenheit - 32.0)

                print('\033[0;31;40m' + str(fahrenheit) + ' Fahrenheit is ' + str(fahToCelsius) + ' Celsius' + '\033[0;0m')
                break
            except ValueError:           # This checks if the inputed a non numeric value
                print('Please, input a numeric value.')
                continue

    else:         # If the the user input any other letter aside 'F' or 'C', the program returns to the beginning
        print('Please, input the either F or C')
        continue
    
    # This asks the users if they want to perform another calculation
    print('Do you wish to do another conversion? (Y)es or (N)o.')
    repeatChoice = input()

    # The start the program for another conversion
    if repeatChoice == 'y' or repeatChoice == 'Y':          
        continue
  
    # This exits the program
    elif repeatChoice != 'y' or repeatChoice != 'Y':
        sys.exit()
