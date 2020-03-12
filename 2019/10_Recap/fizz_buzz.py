def fizz(number):
    """ returns whether a number is divisible by 3"""
    return not number % 3


def buzz(number):
    """ returns whether a number is divisible by 5"""
    return not number % 5


def fizz_buzz(limit):
    """ play the fizz buzz game until the number limit"""
    for number in range(1, limit + 1):
        answer = ''
        if fizz(number):
            answer += 'fizz'
        if buzz(number):
            answer += 'buzz'

        if answer != '':
            print(answer)
        else:
            print(number)


fizz_buzz(20)  # Play to 20
