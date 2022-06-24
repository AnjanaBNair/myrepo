# strong_password_detection_regex.py
# PAGE 186 Automate the Boring Stuff With Python Chapter 7 Practice Project
import re           # For search()


# Function to check for strong password
def strong_password_check(user_inputs):
    """Check if there is uppercase, lowercase, and numbers in the password
    with a minimum of 8 characters and maximum of 15 characters."""
    
    # Patterns
    upcase = re.search(r'[A-Z]', user_inputs)
    lowcase = re.search(r'[a-z]', user_inputs)
    digit = re.search(r'[0-9]', user_inputs)

    if len(user_inputs) < 8:
        print('Password should more than 8 characters.')
        return False
    elif len(user_inputs) > 15:
        print('Password should be less than 15 characters.')
        return False
    elif upcase is None:
        print('Enter an uppercase.')
        return False
    elif lowcase is None:
        print('Enter a lowercase.')
        return False
    elif digit is None:
        print('Enter a digit')
        return False
    else:
        print('Strong password.')
        return True


print(' Strong Password Checker '.center(40, '*'))
user_input = input('Enter your password: ')
strong_password_check(user_input)
