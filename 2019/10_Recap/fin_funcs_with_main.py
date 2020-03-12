def avg(num_1, num_2):
    """computes the average of two numbers"""
    return (num_1 + num_2) / 2


def main():
    num_1, num_2 = 5, 10
    answ = "The average of {} and {} is {}"
    print(answ.format(num_1, num_2, avg(num_1, num_2)))


if __name__ == "__main__":
    main()
