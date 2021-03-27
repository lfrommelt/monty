from random import randint

LENGTH = 100

# start with an empty string
s = ""

for i in range(LENGTH):
    # pick random number between 1 and 10
    n = randint(1, 10)

    # the probability that n is <= 7 is 70%
    if n <= 7:
        s += "X"

    # which means the rest is 30%
    else:
        s += "O"

# finally print the built-up string
print(s)
