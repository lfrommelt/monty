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
	#
	# Your code:
	# Change n random cells in the field from 0 to 1
	#
	return field
		

def apply_rules(field):
	#
	# Your code:
	# Apply the rules of Conway's Game of life here to each cell
	#
	return field	


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
