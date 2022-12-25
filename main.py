'''
Write a program that prints the numbers 
from 1 to 100 
and for multiples of ‘3’ print “Fizz”
instead of the number and for the multiples of ‘5’ print “Buzz”.
 
number divisible by 3 and 5 will
always be divisible by 15, print
'FizzBuzz' in place of the number
'''

from number_multiple_checker import checking_multiple as checked


def fizz_buzz_returner(number_to_check: int, divisor_one: int, divisor_two: int, message1='Fizz', message2='Buzz'):
    """
    Return message or number depending on results of the checks.
    Function takes
    :param number_to_check: (integer).

    If it multiplies of
    :param divisor_one: (integer)
    then :return:
    :param message1: (string).

    If it multiplies of
    :param divisor_two: (integer)
    then :return:
    :param message2: (string).

    If it multiplies both, then :return:  concatenation of :param message1 one and :param message2.


    """

    if checked(number_to_check, divisor_one) and checked(number_to_check, divisor_two):
        return message1+message2
    elif checked(number_to_check, divisor_one):
        return message1
    elif checked(number_to_check, divisor_two):
        return message2
    else:
        return number_to_check


if __name__ == '__main__':
    fizz_num = 3
    buzz_num = 5

    for i in range(100):
        print(fizz_buzz_returner(i, fizz_num, buzz_num))