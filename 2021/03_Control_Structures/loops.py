# for row in range(3):
#     for column in range(3):
#         number = row * 3 + column + 1
#         print("  ", number, end = "")
#
#     print("\n")

n = int(input("number pls "))

print("    ", end = "")

for i in range(n):
    print("  ", i + 1, end = "")

print()

for row in range(n):
    print("  ", row + 1, end = "")

    for col in range(n):
        if (col + 1) % (row + 1) == 0:
            print("   X", end = "")
        else:
            print("    ", end = "")

    print()
