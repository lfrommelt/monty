import sys


def count_holidays(filename):
    """Returns the number of holidays listed inside
    the given csv file."""
    with open(filename) as f:
        return len(f.readlines()) - 1


if __name__ == '__main__':
    print(count_holidays(sys.argv[1]))
