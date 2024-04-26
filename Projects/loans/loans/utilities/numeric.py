"""This module will have numeric utilities
"""

def is_prime(number):
    """This function checks if the number is prime or not
    
    Args:
      number (int): 
    Returns:
      True if number is prime, False otherwise
    """
    if number < 2:
        return False
    for index in range(2, (number//2 + 1) ):
        if number % index == 0:
            return False
    return True
        