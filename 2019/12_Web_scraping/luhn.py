import sys


def check_validity(card_number):
    """checks the validity of a credit card number with the Luhn Algorithm

    Arguments:
        card_number {str} -- the number of the card to be cheked as a string

    Returns:
        Boolean -- True if the card number is valid
    """

    # make a list of integer numbers from the string
    num_list = [int(num) for num in card_number]

    # double every second digit
    doubled_2nd = [2*num if not index % 2
                   else num for index, num in enumerate(num_list)]

    # if number is greater than 9, build the cross sum
    cross_sum_gr_9 = [num % 10 + 1 if num > 9 else num for num in doubled_2nd]

    # sum all digits up
    check_sum = sum(cross_sum_gr_9)

    # check if the result is divisible by 0
    return check_sum % 10 == 0


if __name__ == "__main__":
    # take the command line argument
    card_num = sys.argv[1]
    print(check_validity(card_num))
