'''
Write a program that prints the numbers 
from 1 to 100 
and for multiples of ‘3’ print “Fizz”
instead of the number and for the multiples of ‘5’ print “Buzz”.
 
number divisible by 3 and 5 will
always be divisible by 15, print
'FizzBuzz' in place of the number
'''

from number_multiple_checker import checking_multiple as divide


def main_function(number_to_check: int, divisor_one: int, divisor_two: int, message1='Fizz', message2='Buzz'):
    """
    main function:
    Printing results of checking.
    Takes
    :param number_to_check: (integer)
    if it multiplies of
    :param divisor_one: (integer)
    then print
    :param message1: (string)
    if it multiplies of
    :param divisor_two: (integer)
    then print
    :param message2: (string)

    :return: 1
    """

    if divide(number_to_check, divisor_one) and divide(number_to_check, divisor_two):
        print(message1+message2)
    elif divide(number_to_check, divisor_one):
        print(message1)
    elif divide(number_to_check, divisor_two):
        print(message2)
    else:
        print(number_to_check)


if __name__ == '__main__':
    Fizz_num = 3
    Buzz_num = 5

    for i in range(100):
        main_function(i, Fizz_num, Buzz_num)
