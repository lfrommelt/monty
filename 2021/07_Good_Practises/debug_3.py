# why=None
# what=why
# while what is why:
#     try:
#         what=int (input ("what? " ) )
#     except ValueError :
#         print(   "no.")
# def abc(z):
#     if(z<=1):return False
#     for(x)in(range(2  ,int(z**.5)+1))  :
#         if z  %  x==0:
#             return False
#     return True
# for who   in range (1 ,what+   1):
#     how=abc (who)
#     if how :
#         print("{}???".format(who),":)")
#     else:
#         print ("{}???" . format(who) , ":(")

"""This program will check all integers up to a specified limit for primality"""
max_number = None

# letting user input a number up to which to check
while max_number is None:
    try:
        # try to convert user input to integer
        max_number = int(input("Up to which number would you like to check? "))
    except ValueError:
        # if input is invalid, let them try again
        print("Please enter an integer.")

def is_prime(n):
    """Checks if the argument n is a prime number. Returns True if it is, False otherwise."""
    # 1 is not prime by definition
    if n <= 1:
        return False

    # check up to sqrt(n) + 1 if there exists a number that divides n
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            # if divisor is found, n is not prime
            return False

    # if all checks up to here fail, n is prime
    return True

# check all numbers up to max_number and print result
for n in range(1, max_number + 1):
    if is_prime(n):
        print(n, "is a prime number!")
    else:
        print(n, "is NOT a prime number.")
