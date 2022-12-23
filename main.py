'''
Write a program that prints the numbers 
from 1 to 100 
and for multiples of ‘3’ print “Fizz”
instead of the number and for the multiples of ‘5’ print “Buzz”.
 
number divisible by 3 and 5 will
always be divisible by 15, print
'FizzBuzz' in place of the number
'''


def checking_multiple(number_for_checking: int, divider: int):
    """
    Check the condition:
    Is number_for_checking a multiple of the divider
    :param divider: no zero integer
    :param number_for_checking: integer
    :return: 1 if true else return 0
    """
    if number_for_checking % divider == 0:
        return 1
    else:
        return 0


def main_function(a: int, b: int, c: int, message1='fizz', message2='buzz'):
    """
    main function:
    printing results of checking
    takes
    :param a: integer
    if multiple of
    :param b: integer
    then print
    :param message1: string
    if multiple of
    :param c: integer
    then print
    :param message2: string

    :return: 1
    """
    ...
