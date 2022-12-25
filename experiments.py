# print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')


def perfect_ozz_checker(num_for_check, dividers_array, message_array) -> str:
    """
    Function takes:
    :param num_for_check: expected positive integer
    :param dividers_array:
    :param message_array:
    excepted that length of arrays is equal
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