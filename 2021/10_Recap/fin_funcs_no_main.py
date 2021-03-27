def avg(num_1, num_2):
    """computes the average of two numbers"""
    return (num_1 + num_2) / 2


# testing the code at the end of the script
num_1, num_2 = 5, 10
answ = "The average of {} and {} is {}"
print(answ.format(num_1, num_2, avg(num_1, num_2)))
print("The __name__ of fin_funcs_no_main.py :", __name__)
