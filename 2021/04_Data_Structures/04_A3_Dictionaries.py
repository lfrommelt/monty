# importing the function randint from the random module
from random import randint

# dictionary with integer numbers as keys and the tranlated string number word as values
TRANSLATION = {9: "nine", 8: "eight", 7: "seven", 6: "six",
            5: "five", 4: "four", 3: "three", 2: "two", 1: "one", 0: "zero"}


def make_randint_list(start, stop, length=10):
    """ Makes a list of randomly generated integers

    Args:
        start: lowest integer to be generated randomly.
        stop: highest integer to be generated randomly.
        length: length of generated list.

    Returns:
        list of random numbers between start and stop of length length
    """
    return [randint(start, stop) for i in range(length)]


def translate(num_list, transl_dict):
    """ Translates integer list to number word list (no error handling!)

    Args:
        num_list: list with interger items.
        transl_dict: dictionary with integer keys and number word values.

    Returns:
        list of strings which are the translated numbers into words.
    """
    return [transl_dict[item] for item in num_list]


# Error handling
# handle the case if the key is not in the  dictionary

def translate_with_get(num_list, transl_dict):
    """ Translates integer list to number word list.
        If there is no translation available,
        "no translation" instead of the number word is added to the list.

    Args:
        num_list: list with interger items.
        transl_dict: dictionary with integer keys and number word values.

    Returns:
        list of strings which are the translated numbers into words.
    """
    translation = []

    for item in num_list:
        translation.append(transl_dict.get(item, "no translation"))

    return translation


def translate_except_error(num_list, transl_dict):
    """ Translates integer list to number word list.
        If there is no translation available,
        "unknown translation" instead of the number word is added to the list.

    Args:
        num_list: list with interger items.
        transl_dict: dictionary with integer keys and number word values.

    Returns:
        list of strings which are the translated numbers into words.
    """
    translation = []

    for item in num_list:
        try:
            translation.append(transl_dict[item])
        except KeyError:
            translation.append("unknown translation")

    return translation



# generating a list with 10 random numbers from 3 to 9
num_list_1 = make_randint_list(3, 9)

# print original number list
print(num_list_1)

# call function without error handling to translate number list
print(translate(num_list_1, TRANSLATION))


# generating a list with 5 random numbers from 7 to 10
num_list_2 = make_randint_list(7, 10, 5)

# print original number list
print(num_list_2)

# call function that uses the get() dictionary method to translate number list
print(translate_with_get(num_list_2, TRANSLATION))

# call function with try except error handling to translate number list
print(translate_except_error(num_list_2, TRANSLATION))
