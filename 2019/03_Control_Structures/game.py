from random import randint

n = randint(1, 100)

guess = int(input("Ok, I have thought of a number. First guess: "))
tries = 1

while guess != n:
    if n > guess:
        guess = int(input("My number is larger than that. Next guess: "))
    else:
        guess = int(input("My number is smaller than that. Next guess: "))

    tries += 1

print("Correct! It took you", tries, "guesses.")
