'''
5) Write a function that recognizes palindromes.
'''

def is_palindrome(str):
    '''
    Recognizes palindromes.
    '''

    # Reversed string variable
    reversed_str = ""

    # Building the reversed word to compare
    for i in range(len(str)):
        reversed_str = str[i] + reversed_str

    # Checking if the word is palindrome
    if str == reversed_str:
        return True
    else:
        return False
