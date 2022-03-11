'''
4) Write a function, is_prime, which takes a single integer argument and returns True when
the argument is a prime number and False otherwise.
'''

# Importing libraries
from math import sqrt

def is_prime(n):
    '''
    Returns whether the given positive integer is prime or not.
    '''
    
    # Checking particular cases
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    # Checking general cases
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    
    # In case the number passes the other conditions, it's prime
    return True
