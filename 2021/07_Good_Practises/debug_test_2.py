def read_n_values(n):
    print("Please enter", n, "values.")
    values = []

    for i in range(n):
        values.append(input("Value {}: ".format(i + 1)))

    return values

def compute_average(values):
    # set sum to first value of list
    total_sum = values[0]

    # iterate over remaining values and add them up
    for value in values[1:]:
        total_sum += value

    return float(total_sum) / len(values)

values = read_n_values(3)
print("Average:", compute_average(values))
