"""These tests will be testing numeric utilities
"""

from loans.utilities.numeric import is_prime

def test_is_prime():
    """Testing prime numbers
    """
    assert is_prime(7)
    assert not is_prime(6)
    #assert not is_prime(0)
