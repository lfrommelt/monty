def is_prime(n):
    """Returns True if n is prime and False otherwise"""
    if n == 1:
        return False

    # check for all numbers up to sqrt(n) whether they divide n
    for divider in range(2, int(n ** 0.5) + 1):
        if n % divider == 0:
            # if a divider is found, immediately return False
            return False

    # we only get here if no divider has been found --> n is prime
    return True

n = int(input("Please input a number: "))

for i in range(1, n + 1):
    if is_prime(i):
        print(i, "is prime.")
    else:
        print(i, "is not prime.")
