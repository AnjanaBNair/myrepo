# quadratic_equation_solver.py - Solves a quadratic equation.
import cmath


def quad():
    print('Quadratic Equation')
    print(f'ax\N{SUPERSCRIPT TWO} + bx + c = 0')
    # Using fstring and the \N{SUPERSCRIPT TWO} allows the output to display a superscript of 2 (Python 3.6+)
    print('Please enter the values of a, b, and c.')

    a_value = int(input('a: '))
    b_value = int(input('b: '))
    c_value = int(input('c: '))

    try:
        first_quad_calc = (-b_value + cmath.sqrt(pow(b_value, 2) - (4 * a_value * c_value))) / (2 * a_value)
        second_quad_calc = (-b_value - cmath.sqrt(pow(b_value, 2) - (4 * a_value * c_value))) / (2 * a_value)
        # The pow() function is used for exponential, while the sqrt() is used for square root

        print('\nThe roots are:')
        print(f'x\N{SUBSCRIPT ONE} = ' + str(first_quad_calc) + '\n' + f'x\N{SUBSCRIPT TWO} = ' + str(second_quad_calc))
        # Using fstring and the \N{SUPERSCRIPT ONE} allows the output to display a subscript

    except ZeroDivisionError:
        print('Invalid Input')


quad()
