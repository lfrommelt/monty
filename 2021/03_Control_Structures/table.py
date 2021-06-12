n = int(input("Please enter the size of the table: "))

# print the first row (header)
print("    ", end = "")

for i in range(1, n + 1):
    print("  ", i, end = "")

print() # new line

# print the actual table
for row in range(1, n + 1):

    # print row number at the beginning of each row
    print("  ", row, end = "")

    # print Xs if column number divides row number
    for col in range(1, n + 1):
        if col % row == 0:
            print("   X", end = "")
        else:
            print("    ", end = "")

    print() # new line at the end of each line
