'''
Write a program that prints the numbers 
from 1 to 100 
and for multiples of ‘3’ print “Fizz”
instead of the number and for the multiples of ‘5’ print “Buzz”.
 
number divisible by 3 and 5 will
always be divisible by 15, print
'FizzBuzz' in place of the number

https://en.wikipedia.org/wiki/Fizz_buzz
'''


def perfect_oz_checker(num_for_check=60, dividers_array=[2,3,5], message_array=['Fizz', 'Buzz', 'Juzz']) -> str:
    """
    Check the number and if it multiplies one of dividers return message like “Fizz”

    Function takes:
    :param num_for_check: expected positive integer
    :param dividers_array: expected integer or array of integers
    :param message_array:  expected array of strings whose length is equal to the length
    of the array of divisors
    :return: string
    """

    result_of_checking = ''

    if not isinstance(dividers_array, (int, list)):
        raise TypeError('You must use integer or list of integers')

    if type(dividers_array) == int:
        dividers_array = [dividers_array]

    for i in range(len(dividers_array)):
        result_of_checking += message_array[i] * (not num_for_check % dividers_array[i])

    if result_of_checking == '':
        result_of_checking = str(num_for_check)

    return result_of_checking


if __name__ == '__main__':
    print(perfect_oz_checker())


    dividers = [3, 5, 4]
    result_list = []
    for int_num in range(100):
        result_list.append(perfect_oz_checker(int_num, dividers))
    print(result_list)
    print('**********\n')

    dividers = [3, 5, 4]
    messages = ['fizzz', 'buzzz', 'juzzz']
    result_list = []
    for int_num in range(100):
        result_list.append(perfect_oz_checker(int_num, dividers))
    print(result_list)
    print('**********\n')

    dividers = 3
    messages = ['fizzz', 'buzzz', 'juzzz']
    result_list = []
    for int_num in range(100):
        result_list.append(perfect_oz_checker(int_num, dividers))
    print(result_list)

'''

refactor to class
'''
