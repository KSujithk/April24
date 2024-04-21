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


# get arguments excluding file name
arguments = sys.argv[1::]
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
