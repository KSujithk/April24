"""
This python module will have reusable numerical functions
   is_even
   is_prime
"""
import snoop

def is_even(number: int):
    """Finds if the number is even or odd

    Args:
      number: Number passed

    Returns:
      True if even, False otherwise

    Usage:
       is_even(6)
       Return True
    """
    if number <= 0:
        return False
    result = number%2 == 0
    return result

@snoop
def is_prime(number: int):
    """Determines if the number is prime or not

    Args:
      number: the value to be passed 

    Returns: 
      True if prime False otherwise
    """
    if number<=0:
        return False
    for index in range(2,number):
        if number % index == 0:
            return False
    return True

if __name__ == "__main__":
    for value in range(5,10):
        if is_prime(value):
            print(value)
