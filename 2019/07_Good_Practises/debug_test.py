fruit_list = ["apple", "banana", "orange"]

# let user add their own fruit
user_fruit = input("Please name a fruit: ")
fruit_list.append(user_fruit)

# print each fruit in a line
for fruit in fruit_list:
    print("This is a cool fruit: " + fruit)

# print explicitly the fruit that was entered by the user
last_fruit_index = len(fruit_list) - 1
print("You especially like: {}".format(fruit_list[last_fruit_index]))
