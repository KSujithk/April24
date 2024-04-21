"""This projects aims at building a command line calculator
* As of now this project supports 
    * addition
    * subtraction
    * division
    * multiplication
    * modulus

Author: shaikkhajaibrahim
CreatedOn: 21/April/2024
"""

import sys

def add(number1, number2):
    """Function to add two numbers
    
    Args:
      number1
      number2

    Returns:
      sum of number1 and number2
    """
    return number1 + number2

def sub(number1, number2):
    """Function to sub two numbers
    
    Args:
      number1
      number2

    Returns:
      sub of number1 and number2
    """
    return number1 - number2

def mul(number1, number2):
    """Function to multiply two numbers
    
    Args:
      number1
      number2

    Returns:
      product of number1 and number2
    """
    return number1 * number2

def div(number1, number2):
    """Function to div two numbers
    
    Args:
      number1
      number2

    Returns:
      division of number1 and number2
    """
    return number1 / number2

def mod(number1, number2):
    """Function to modulus two numbers
    
    Args:
      number1
      number2

    Returns:
      remainder of number1 and number2
    """
    return number1 % number2

def print_usage():
    """This program prints usage
    """
    print("""Usage: python calc.py <action> <number1>  <number2>
          action:  add | sub | mul | div | mod
          number1 is integer
          number2 is integer
          """)

def is_int(value):
    try:
        int(value)
    except ValueError:
        print()
        return False
    return True

def validate_arguments(arguments):
    """This function validates arguments and displays error 
    message to the user

    Arguments: arguments

    Returns:
      True if the arguments are valid False otherwise
    """
    if len(arguments) != 3:
        print_usage()
        return False
    valid_actions = ('add', 'sub', 'mul', 'div', 'mod')
    if arguments[0].lower() not in valid_actions:
        print("Invalid action")
        print_usage()
        return False    
    #todo: We still need to validate if the values are 
    # integers or not
    if not is_int(arguments[1]) or  not is_int(arguments[2]):
        print("pass integers only")
        print_usage()
        return False
    return True


def main(arguments):
    """This function executes when the file is called directly

    Arguments:
       arguments
    """
    if not validate_arguments(arguments):
        sys.exit(1)
    # get action
    action = arguments[0]
    # get number 1
    number1 = int(arguments[1])
    # get number 2
    number2 = int(arguments[2])

    if action.lower() == 'add':
        result = add(number1, number2)
    elif action.lower() == 'sub':
        result = sub(number1, number2)
    elif action.lower() == 'mul':
        result = mul(number1, number2)
    elif action.lower() == 'div':
        result = div(number1, number2)
    elif action.lower() == 'mod':
        result = mod(number1, number2)
    else:
        print("wrong operation provided")
        sys.exit(1)
    print(result)

if __name__ == "__main__":
    main(sys.argv[1::])
