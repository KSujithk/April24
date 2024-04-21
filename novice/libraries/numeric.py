"""
This module will have reusable numeric functions
encountered during my learning on python
"""

def is_even(number):
    """This function determines if the number is even or odd

    Args: 
      number: number to be checked

    Returns:
        True if even, False otherwise
    """
    if number <= 0:
        return False
    return number % 2 == 0

def factors(number):
    """This function returns a list of factors of the given number

    Args:
      number: factors to be found out for this number

    Returns:
      a list of factors
    """
    factor_list = []
    half_of_number = number // 2 + 1 # to pass for range function 
    for index in range(2, half_of_number):
        if number% index == 0:
            factor_list.append(index)
    return factor_list
