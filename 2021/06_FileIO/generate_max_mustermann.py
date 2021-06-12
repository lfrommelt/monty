import json


def generate_max():
    """ generates a Max Mustermann with random information based on a random user
    """
    # read in the content of the random user file
    with open("random_user.json") as file:
        file_string = file.read()

    print('After reading in the file with read(), it is of the type:',
          type(file_string))

    # convert into dictionary
    user_dict = json.loads(file_string)

    # change information
    user_dict["results"][0]["name"]["first"] = 'Max'
    user_dict["results"][0]["name"]["last"] = 'Mustermann'

    # make a string (in JSON format) out of the dictionary
    max_json = json.dumps(user_dict, indent=4)
    print('After dumping the dictionary, we have the type:', type(max_json))

    # write max's info to a new file
    with open("max_mustermann.json", "w") as max_file:
        max_file.write(max_json)


def short_cut_max():
    """ generates a Max Mustermann with random information based on a random user
    """
    # get the random user information
    with open("random_user.json") as file:
        # convert into dictionary
        user_dict = json.load(file)

    # change information
    user_dict["results"][0]["name"]["first"] = 'Max'
    user_dict["results"][0]["name"]["last"] = 'Mustermann'

    # write max user info to a new file
    with open("max_mustermann.json", "w") as max_file:
        json.dump(user_dict, max_file, indent=4)


generate_max()
