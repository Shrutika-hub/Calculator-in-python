import math

def calculate():
    operation = input('''
        Press + for addition
        Press - for Subtraction
        Press * for Multiplication
        Press / for division
        Press ** for power
        Press % for modulus
        Press $ for cosine Trignometric operation
        Press c for sine Trignometric operation
        Press t for tangent Trignometric operation

Please Enter the above math operation which you want to execute:
''')

    number_1 = float(input('Please enter the First number: '))
    number_2 = float(input('Please enter the Second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2), end=" ")
        print(float(number_1 + number_2))

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2), end=" ")
        print(float(number_1 - number_2))

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2), end=" ")
        print(float(number_1 * number_2))

    elif operation == '/':
        if(number_2!= 0):
            print('{} / {} = '.format(number_1, number_2), end=" ")
            print(float(number_1 / number_2))
        else:
            print("\nZeroDivisionError: division by zero.",end=" ")
            print("Please enter valid number")

    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2), end=" ")
        print(number_1 ** number_2)

    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2), end=" ")
        print(float(number_1 % number_2))

    elif operation == '$':
        print('sin({}) = '.format(number_1), end=" ")
        print(float(math.sin(number_1)))

    elif operation == 'c':
        print('cos({}) = '.format(number_1), end=" ")
        print(float(math.cos(number_1)))

    elif operation == 't':
        print('tan({}) = '.format(number_1), end=" ")
        print(float(math.sin(number_1)))

    else:
        print('You have entered a wrong math operator!')
        print('Please try agin!')
    again()

def again():
    calculation_again = input('''
Do you want to Calculate again?
Please type YES to continue or NO to stop :
''')

    if calculation_again.upper() == 'YES':
        calculate()
    elif calculation_again.upper() == 'NO':
        print('see u next time, thank you to your interest here...')
    else:
        again()

calculate()