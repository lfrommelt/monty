bubblelist = [3, 0, 1, 8,  7, 2, 5, 4, 6, 9, 2]

swapped = True
while swapped:
    swapped = False
    for index in range(1, len(bubblelist)):
        if bubblelist[index - 1] > bubblelist[index]:
            temp = bubblelist[index]
            bubblelist[index] = bubblelist[index - 1]
            bubblelist[index - 1] = temp
            swapped = True

print(bubblelist)
