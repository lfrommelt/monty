---
title: BPP Exercise 2 -- Variables, Assignments and If-statements
date: 2019-04-14
...

\noindent
Please create an individual file for the solution of each task.
If it is a program, please make sure you save it as `01_filename.py`.
Make sure that you use a descriptive filename that includes the tasknumber.
Then make a zip folder containing all files for all tasks.
Lastly, upload the folder to StudIP.

\noindent
We want to encourage you to come to the practice sessions.
They give you the oportunity to work on the tasks with your peers and ask us for tips for the exercises.
If you have any problems, ask questions to your fellow students, come to the practice session, or drop us a mail.
Have fun Programming!


# Warm-up Exercises

## Reasoning about variables (10 points)

1. What is the output if you run this code? Why?
   ```python
   cat = "Tom"
   dog = "Bruno"
   chase = dog + " chases " + cat
   print(chase)
   dog = "Bello"
   print(chase)
   print(dog, "chases", cat)
   ```

   :::solution
   ```{ .python .exec .hide}
   cat = "Tom"
   dog = "Bruno"
   chase = dog + " chases " + cat
   print(chase)
   dog = "Bello"
   print(chase)
   print(dog, "chases", cat)
   ```

   First print statement:
   The string `"Tom"` gets assigned to the variable `cat`. The string `"Bruno"` gets assigned to the variable `dog`. Then the two strings are concatenated with the `+` operator and assigned to the variable `chase`. Therefore, in line 3 `chase` contains the string `"Bruno chases Tom"` and this string will be printed on the terminal by calling the print function in line 4.

   Second print statement:
   After that in line 5, the string `"Bello"` gets assigned to the variable dog. In line 6 the variable `chase` gets printed again. The print function still outputs `"Bruno chases Tom"` as there was no reassignment to the variable `chase`.

   Third print statement:
   The print function in line 7 prints the assigned value of `dog` (which was lastly changed to `"Bello"`) followed by the string `"chases"` and followed by the assigned value of `cat`. This leads to the output: `"Bello chases Tom."`
   :::


# Variable Assignments and Common Operators (20 points)

## Analyzing code

1. Which of the following lines of code throws an error? Why?
2. Which lines make sense to use in a script?

   ```python
   2 + 2
   5 = 3 + 2
   5 == 3 + 2
   k = 5
   a = b
   ```

   :::solution

   1. `Line 1` does not throw an error. But as the result is not processed further or stored, e.g. in a variable, it does not make a lot of sense to use this line of code in a script.
   2. `Line 2` throws a SyntaxError. You can't assign values to numbers, only to variables.
   3. `Line 3` does not throw an error. As this statement is always true. As it is not part of an if-statement, it does not make a lot of sense to use this line of code in a script.
   4. `Line 4` does not throw an error. This is a way to store the value 5 in the variable `k` and reuse or modify it later in the script.
   5. `Line 5` throws a NameError. It is not possible to assign `b` to the variable `a` as `b` was not defined beforehand.

   :::


## Your first program: Calculating the prices of your grocery list

1. Complete the script: Print a sentence about the total price for cheese and the total price for the apples to the terminal. After that, add an additional sentence about the total price of the shopping list (the price of the cheese and the apples together).

   ```python
   # Your grocery list

   # items
   item_a = 'cheese'
   item_b = 'apple'

   # prices per unit
   price_a = 4.2
   price_b = 1.2

   # quantities
   quantity_a = 2
   quantity_b = 5
   ```

   :::solution
   ```{ .python .exec}
   # Your grocery list

   # items
   item_a = 'cheese'
   item_b = 'apple'

   # prices per unit
   price_a = 4.2
   price_b = 1.2

   # quantities
   quantity_a = 2
   quantity_b = 5

   # Calculating the total price for the cheese
   total_a = price_a * quantity_a
   print('The price for the', item_a, 'is', total_a, 'Euros.')

   # Calculating the total price for the apples
   total_b = price_b * quantity_b
   print('The price for the', item_b + 's', 'is', total_b, 'Euros.')

   # Calculating the total price for both
   total = total_a + total_b
   print('The total price is: ', total, 'Euros.')
   ```
   :::


# Understanding if-statements (30 points)

## Analyzing code
1. What does this program do? Explain briefly. What happens if you change the distances?

   ```python
     distance_university = 5
     distance_home = 4
     if distance_home < distance_university:
         print("Let's go home!")
     else:
         print("Since we are almost there...")
   ```

   :::solution
   This code either prints on the command line `"Lets go home!"` or `"Since we are almost there..."`.
   Which statement is displayed depends on whether the distance to home or the distance to the university is smaller. If the distance to home is strictly smaller than the distance to the university, the user will get the instruction to go home. In all other cases, i.e. if the distance to the university is smaller or equal to the distance to home, the user will see the encouraging words `"Since we are almost there..."`.
   :::


## Falsy and Truthy

1. What is going to be the output when you run this script?

   ```python
   if 'a':
       print('Learning')

   if '':
       print('to program')

   if 'false':
       print('Python')

   if bool('false'):
       print('is')

   if bool(False):
       print('Programming')

   if bool('False'):
       print('a lot')

   if False:
       print('some')

   if 0:
       print('plenty')

   if 1:
       print('of ')

   if 2:
       print('fun')

   if -3:
       print('.')

   if None:
       print('!')
   ```

   :::solution
   ```{ .python .exec .hide}
   if 'a':
       print('Learning')

   if '':
       print('to program')

   if 'false':
       print('Python')

   if bool('false'):
       print('is')

   if bool(False):
       print('Programming')

   if bool('False'):
       print('a lot')

   if False:
       print('some')

   if 0:
       print('plenty')

   if 1:
       print('of ')

   if 2:
       print('fun')

   if -3:
       print('.')

   if None:
       print('!')
   ```
   :::

2. Write down the cases that you learned from this exercise that are evaluated to `True`. Try out different if-statements on your own. Try to generalize your explanation for the different cases as much as possible and find general rules.

:::solution
You can look up the exact rules in the [**Python Docs**](https://docs.python.org/3/library/stdtypes.html#truth-value-testing). There are other cases, which we did not cover yet.

The following is a short (but not exhaustive) overview of cases that you should remember for the future:
All values are considered "Truthy" except for the following, which are "Falsy":

- `None`
- `False`   (this is case sensitive!)
- `0`
- `0.0`
- `""`      (an empty str)
:::


## Your second program: Positive or negative?

1. Write a program that determines whether a variable is a positive or negative number.

::: solution
```python
# setting a number
number = 3.2

if number > 0:
    print('The number is postive.')

elif number < 0:
    print('The number is negative.')

else:
    print('The number is 0.')
```
:::


# Errors and how to fix them (20 points)

Even the most experienced programmers make errors in their code. When running code, you will also receive error messages and need to debug (i.e. finding and fixing errors) your code. That is totally normal! Error messages are great as their names can often help us to spot the mistakes in the code more easily and give hints where to start debugging. There are many different kind of error messages. The following exercise picks up three kinds of common mistakes and wants to encourage you to read the error messages carefully.

1. Which errors occurred when you ran the lines of code? Fix them.

   ```python
   # First error
   variable_1 = variable_2
   variable_2 = 5
   print(variable_2)
   ```

   ```python
   # Second error
   print('Please fix this.)
   ```

   ```python
   # Third error
   age = 21
   print('You will turn 100 years in ' + (100 - age) + ' years.')
   ```

   ```python
   # Fourth error
   savings = 100
   debts = 'ten'

   account_balance = savings - float(debts)
   print('The account balance is:', account_balance, 'dollars.')
   ```

   :::solution

   <!-- 1 -->
   ```{ .python .exec}
   # First error
   variable_1 = variable_2
   variable_2 = 5
   print(variable_2)
   ```

   The first error was a NameError. A NameError occurs when you use a variable that did not exist before. Therefore we have to change the order of the variable assignments in the code.

   ```{ .python .exec}
   # Fixed code:
   variable_2 = 5
   variable_1 = variable_2
   print(variable_2)
   ```

   <!-- 2 -->
   ```{ .python .exec}
   # Second error
   print('Please fix this.)
   ```

   The second error was a SyntaxError. A SyntaxError occurs when Python cannot parse the code.
   In the provided code the closing quotation mark was missing.

   ```{ .python .exec}
   # Fixed code:
   print('Please fix this.')
   ```


   <!-- 3 -->
   ```{ .python .exec}
   # Third error
   age = 21
   print('You will turn 100 years in ' + (100 - age) + ' years.')
   ```

   The third error was a TypeError. A TypeError occurs when a operation is used with inappropriate variable types.
   ```{ .python .exec}
   # Fixed code:
   age = 21
   print('You will turn 100 years in ' + str(100 - age) + ' years.')
   ```

   <!-- 4 -->
   ```{ .python .exec}
   # Fourth error
   savings = 100
   debts = 'ten'

   account_balance = savings - float(debts)
   print('The account balance is: ', account_balance, 'dollars.')
   ```

   The fourth error was a ValueError. A ValueError occurs when a function (more about this in the next lecture) is given an inappropriate value. Numbers that are written out as a string cannot be casted into a floating point number with a `float()` call. To do arithmetic, we need to provide a number type.

   ```{ .python .exec}
   # Fixed code:
   savings = 100
   debts = 10.0

   account_balance = savings - debts
   print('The account balance is: ', account_balance, 'dollars.')
   ```
   :::


# Thinking Outside the Box (20 points)

In the _Thinking Outside the Box_ exercises, we want to encourage you to play around with code, to try out creative solutions, and investigate about concepts that have not been explicitly mentioned in the lecture. To get to a solution, you can run the code, change things and run the code again, search the internet, ask a fellow student for tips or whatever helps you to solve the exercise.

1. What does this program do?
2. What are the two 'things' that we did not cover in the lecture yet? What do they do and how can you use them?

   ```python
   a = int(input('Please enter a number: '))
   b = int(input('Please enter a number: '))

   if a % b == 0:
       print('Yes')
   else:
       print('No')
       print('The remainder is', a % b)
   ```

   :::solution

   1. The program checks wether the first number (entered by the user) is divisible by the second number without leaving a remainder. In case there is a remainder, the remainender gets printed to the terminal.

   2. Sometimes you want to work with user input e.g. numbers or words the user types to the keyboard in reaction to a prompt that is displayed on the screen. The function `input()` can be used to work with the user input that stems from the keyboard. The string that you can write into the paranthesis (the prompt) will be written in the terminal. The user then enters her or his input. The input to the terminal is terminated by hitting the return key. If the user input was assigned to a variable, this variable can now be used in the subsequent script. To see another example, you can have a look at the
   [**Documentation**](https://docs.python.org/3/library/functions.html#input).

   The `%` operator is called modulo operator and returns the remainder of integer division.
   :::
