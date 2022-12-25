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


def perfect_ozz_checker(num_for_check, dividers_array, message_array) -> str:
    """
    Function takes:
    :param num_for_check: expected positive integer
    :param dividers_array: expected array of integers
    :param message_array:  expected array of strings whose length is equal to the length
    of the array of divisors
    :return: string
    """
    result_of_checking = ''
    for i in range(len(dividers_array)):
        result_of_checking += message_array[i] * (not num_for_check % dividers_array[i])
    if result_of_checking == '':
        result_of_checking = str(num_for_check)
    return result_of_checking


if __name__ == '__main__':

    dividers = [3, 5, 4]
    messages = ['fizz', 'buzz', 'juzz']
    for int_num in range(100):
        print(perfect_ozz_checker(int_num, dividers, messages))