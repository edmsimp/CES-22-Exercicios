'''
3) Write a fruitful function sum_to(n) that returns the sum of all integer
numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which
would return the value 55.
'''

def sum_to(n):
    '''
    Returns the sum of all integer numbers up to a given number, including it.
    '''

    # Sum variable
    s = 0

    # Sum loop
    for i in range(1, n+1):
        s = s + i

    # Returning the result
    return s
