
def read_distances(filename):
    """ reads in the distances from the file and converts them into meters

    Args:
        filename: the name of the file.

    Returns:
        list of the distance values from the file converted into meters
    """
    # initialize the list in which we save the distances
    distance_list = []

    # use with open in order to open (and close) the file
    with open(filename) as f:
        # read in the whole content of the file (str) and split at line breaks
        # and interate over each line
        for distance in f.read().splitlines():
            # separate into value and unit
            value, unit = distance.split()
            # convert the value into a float
            value = float(value)

            # convert the distance into meters and append it to the list
            if unit == 'm':
                distance_list.append(value)
            elif unit == 'cm':
                distance_list.append(value / 100)
            elif unit == 'mm':
                distance_list.append(value / 1000)
            else:
                raise ValueError('Invalid unit: ' + unit)

    return distance_list


def filter_greater_50m(distance_list):
    """ filters out all values that are > 50

    Args:
        distance_list: a list of distance values in meters.

    Returns:
        list of the distance values greater than 50 meters.
    """
    # init list of values greater than 50m
    greater_50 = []

    # iterate over each distance
    # and throw it into the greater_50 list if it is greater than 50
    # you could also use a list comprehension here
    for distance in distance_list:
        if distance > 50:
            greater_50.append(distance)

    return greater_50


def create_file(filename, distance_input):
    """ writes dinstances to a newly created file

    Args:
        filename: name of the file to be created.
        distance_input: list of distance values in meters.

    """
    # open (and close) the file in "write" mode
    with open(filename, "w") as outfile:
        # write each distance to the file
        for distance in distance_input:
            outfile.write(str(distance) + " m\n")


# get a list of distances from the file (unit is meters)
distance_list = read_distances('distances.txt')

# print total distance to the screen
total = sum(distance_list)
print('The total distance is', total, 'm.')

# print total distance to a new file
create_file("total_distance.txt", [total])

# print distances greater 50 m to a new file
create_file("greater_50.txt", filter_greater_50m(distance_list))
