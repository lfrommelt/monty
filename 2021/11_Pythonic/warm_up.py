import csv

# read in list of names, discard the header
with open("names.csv") as names_file:
    names = []
    reader = csv.reader(names_file)

    for i, name in enumerate(reader):
        if i != 0:
            names.append(name)

# convert to ages to int
for i in range(len(names)):
    names[i][2] = int(names[i][2])

# sort by first age
def bubblesort_names(names):
    done = False

    while not done:
        done = True

        for i, name in enumerate(names[:-1]):
            if names[i][2] > names[i+1][2]:
                names[i], names[i+1] = names[i+1], names[i]
                done = False

bubblesort_names(names)

# print names in a nice way:
for name in names:
    first_name = name[1]
    last_name = name[0]
    age = name[2]

    print(first_name + " " + last_name + " is " + str(age) + " years old.")
