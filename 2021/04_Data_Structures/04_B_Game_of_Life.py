from random import randint
from time import sleep

def main():
    """Executes the game as long as the script is not interrupted by the user."""
    field = init_field()
    field = rand_fill(field)
    display(field)

    while True:
        sleep(0.1)
        field = apply_rules(field)
        display(field)


def rand_fill(field, n=100):
    """Fills n randomly selected cells with value 1."""
    for i in range(n):
        field[randint(0, len(field) - 1)][randint(0, len(field[0]) - 1)] = 1
    return field
        

def apply_rules(field):
    """Applies the rules of Conway's Game of Life to each cell."""
    for y in range(len(field)):
        for x in range(len(field[0])): # for each cell
            neighbors = get_neighbors(y, x, field)
            if neighbors < 2 or neighbors > 3:
                field[y][x] = 0 # dies by over- or underpopulation
            elif neighbors == 3:
                field[y][x] = 1 # reproduces
    return field


def get_neighbors(y, x, field):
    """Counts how many living neighbors a given cell has."""
    if check_cell(y, x, field):
        neighbors = -1 # balance out own life if living
    else:
        neighbors = 0

    for y_diff in range(-1, 2):
        for x_diff in range(-1, 2): # for each neighbor position
            if check_cell(y + y_diff, x + x_diff, field):
                neighbors += 1
    return neighbors    


def check_cell(y, x, field):
    """Checks whether at a given position there is a living cell."""
    if -1 < x < len(field[0]) and -1 < y < len(field):
        return bool(field[y][x])
    else:
        return False    


def init_field(height=20, width=20):
    """Creates a field by filling a nested list with zeros."""
    field = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        field.append(row)
    return field    


def display(field):
    """Displays the field in nice formatting."""
    print("   " * (((len(field[0]) + 1) // 2) - 1) + "Game of Life")
    print("---" * (len(field[0]) + 1))
    print("   ", end="")
    for x in range(len(field[0])):
        col_num = str(x)
        if len(col_num) == 1:
            print(" " + col_num + " ", end="")
        elif len(col_num) == 2:
            print(col_num + " ", end="")
    print()
    
    for y in range(len(field)):
        row_num = str(y)
        if len(row_num) == 1:
            print(" " + row_num + " ", end="")
        elif len(row_num) == 2:
            print(row_num + " ", end="")
        for x in range(len(field[0])):
            if field[y][x] == 0:
                print("   ", end="")
            else:
                print(" * ", end="")
        print()
    print("---" * (len(field[0]) + 1))


if __name__ == "__main__":
    main()
