import json


def write_to_file(info_dict, filename):
    """function that writes a dictionary to a file

    Arguments:
        info_dict -- dictionary containing information
        filename -- the name of the file that the content will be written to
    """
    with open(filename, "w") as fh:
        json.dump(info_dict, fh, indent=4)


if __name__ == "__main__":

    my_inf = {"name": "Katha", "fav_prog_lang": "Python",
              "fav_animals": ["Tigers", "Giraffes", "Dogs"]}

    # writing the info from the dict to file
    write_to_file(my_inf, "about_me.json")
