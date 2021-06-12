def input_numbers():
    """Reads in and returns a list of numbers.
    Does not do *any* incorrect input handling."""
    l = []

    while True:
        user_input = input("Please enter a number or type 'end': ")

        if user_input == "end":
            # exit loop if user types 'end'
            return l

        else:
            # try to convert entered number to int
            try:
                n = int(user_input)

                # check if n is in the right range
                if 0 < n <= 100:
                    l.append(n)
                else:
                    print("Please enter a number > 0 and <= 100!")

            except ValueError:
                # if it failed with a ValueError, the user did not enter a number
                print("Please enter a number!")


def pack_numbers(numbers):
    """Packs a list of numbers into bins with a maxmimum sum of 100"""
    bins = [[]]

    for n in numbers:
        # if current bin would be too full after adding n, create new bin first
        if sum(bins[-1]) + n > 100:
            bins.append([])

        # add n to current bin
        bins[-1].append(n)

    return bins

def pretty_print_bins(bins):
    """Prints a list of bins in a nice way"""
    print("===================================")

    for i in range(len(bins)):
        print("Bin " + str(i + 1), ": ",  end="")

        for j in range(len(bins[i])):
            print(bins[i][j], end="")

            # only write a , if we are not at the last number
            if j < len(bins[i]) - 1:
                print(",", end="")

            print(" ", end="")

        print("| Total weight:", sum(bins[i]))

    print("===================================")
    print("There are", len(bins), "bins with a total weight of", sum([sum(bin) for bin in bins]))


pretty_print_bins(pack_numbers(input_numbers()))
