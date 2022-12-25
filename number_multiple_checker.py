def checking_multiple(number_for_checking: int, divider: int) -> object:
    """
    Check the condition:
    Is number_for_checking a multiple of the divider?
    :param divider: no zero integer
    :param number_for_checking: integer
    :return: 1 if true. 0 if false. 2 if zero division Error. 3 if type error.
    """

    try:
        if number_for_checking % divider == 0:
            return 1
        else:
            return 0

    except ZeroDivisionError:
        print('You try zero division. It is a bad practice')
        return 2
    except TypeError:
        print("We check only integer numbers, check your arguments please")
        return 3


if __name__ == '__main__':

    numbers_for_check = [-1, 0, 1, 2, 5, 7]

    divider1 = 1
    divider2 = 2
    divider3 = 0
    divider4 = -1
    divider5 = -2
    for x in numbers_for_check:
        print(checking_multiple(x, divider2))
    print('*********')
    for x in numbers_for_check:
        print(checking_multiple(x, divider3))
    for x in numbers_for_check:
        print(checking_multiple(x, divider4))
    for x in numbers_for_check:
        print(checking_multiple(x, divider5))

    print(checking_multiple('2dd', 2))
    print(checking_multiple(2, 'dd'))
