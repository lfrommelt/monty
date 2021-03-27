import luhn


def test_nums(card_nums):
    """ test a given set of card numbers

    Arguments:
        card_nums -- list of card number strings
    """

    # iterate over cards and check validity
    for num in card_nums:
        if luhn.check_validity(num):
            print("The card number", num, "is valid.")
        else:
            print("The card number", num, "is NOT valid.")


if __name__ == "__main__":
    card_nums = ["4137894711755904", "6499802450273568",
                 "8504172191273888", "0043668783485480"]

    test_nums(card_nums)
