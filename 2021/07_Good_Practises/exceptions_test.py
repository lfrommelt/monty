user_number = None

while not user_number:
    try:
        user_input = input("Enter a number: ")
        user_number = float(user_input)

    except ValueError:
        print("That wasn't a number, try again.")
