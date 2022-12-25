def checking_multiple(number_for_checking: int, divider: int) -> object:
    """
    Check the condition:
    Is number_for_checking a multiple of the divider?
    :param divider: no zero integer
    :param number_for_checking: integer
    :return: 1 if true else return 0
    """
    if number_for_checking % divider == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':

    print(checking_multiple(2, 2))
    print(checking_multiple(3,2))
