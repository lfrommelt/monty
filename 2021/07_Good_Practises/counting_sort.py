def counting_sort(values, max_value):
    """Sorts integers using the Counting Sort algorithm.

    Args:
        values:     iterable, contains the integers to sort
                    should be between 0 and max_value
        max_value:  maximum value the numbers can take

    Returns:
        a sorted list of the numbers
    """

    counting_list = [0] * (max_value + 1)
    values_sorted = []

    for number in values:
        counting_list[number] += 1

    for number, amount in enumerate(counting_list):
        for _ in range(amount):
            values_sorted.append(number)

    return values_sorted


print(counting_sort([4, 2, 5, 7, 3, 1, 1, 4, 1, 2, 2], 7))
