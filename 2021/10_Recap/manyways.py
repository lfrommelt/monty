import string


def loops():
    """ solve the tasks with loops"""
    list_a = []
    for letter in string.ascii_lowercase:
        list_a.append(ord(letter))

    list_b = []
    for number in range(1, 48):
        if '3' not in str(number):
            list_b.append(number)

    return list_a, list_b


def list_comprehensions():
    """ solve the tasks with list comprehensions"""
    list_a = [ord(letter) for letter in string.ascii_lowercase]

    list_b = [number for number in range(1, 48) if '3' not in str(number)]

    return list_a, list_b


def main():
    print('Loops:')
    print(*loops(), sep='\n', end='\n'*2)
    print('List comprehensions:')
    print(*list_comprehensions(), sep='\n', end='\n')


if __name__ == '__main__':
    main()
