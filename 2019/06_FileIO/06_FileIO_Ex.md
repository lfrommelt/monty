---
title: BPP Exercise 6 -- File Input/Output
date: 2019-05-19
...


\noindent
This week you will practice how to read data from a file into your Python program and how to save data to a file.
Therefore you do not only need to download this exercise sheet, but also all files that are referenced in the exercises (`Code_Ex_1.py`, `distances.txt`, `my_questions_answers.csv`, `my_shadox.txt`, `random_user.json`).


\noindent
Furthermore, you can find the cheat sheet, that was used in the lecture, [**here**](https://perso.limsi.fr/pointal/python:memento).
Have a look at the different boxes and feel proud of how much you learned already!


# Warm-up

## String recap (3 points)

1. What is the output of the code?
2. Describe in your own words what the methods `strip()`, `split()` and `splitlines()` do.

```python
fun_fact = "This string uses words\nand lines\n"

# the string variable fun_fact
print(fun_fact)
print(type(fun_fact))

# using strip
print(fun_fact.strip())
print(type(fun_fact.strip()))

# using split
print(fun_fact.split())
print(type(fun_fact.split()))

# using splitlines
print(fun_fact.splitlines())
print(type(fun_fact.splitlines()))
```


:::solution

1. What is the output of the code?

```{ .python .exec .hide}
fun_fact = "This string uses words\nand lines\n"

# the string variable fun_fact
print(fun_fact)
print(type(fun_fact))

# using strip
print(fun_fact.strip())
print(type(fun_fact.strip()))

# using split
print(fun_fact.split())
print(type(fun_fact.split()))

# using splitlines
print(fun_fact.splitlines())
print(type(fun_fact.splitlines()))
```

2. Describe in your own words what the methods `strip()`, `split()` and `splitlines()` do.

`strip()`: removes the whitespace characters at the beginning and the end of a string.

`split()`: splits a string into a list of strings (by default it splits at whitespace).

`splitlines()`: splits a string at each line break into a list of strings.
:::


## Read in file (2 points)

1. Print the poem _My Shadow_ to the terminal. Pay attention to not print empty lines where there are none in the original `.txt` file.

:::solution
```{ .python .exec wd=06_FileIO linelength=100 }
# prints the poem to the terminal
with open('my_shadow.txt') as poem:
    print(poem.read())
```
:::



# Read in and work with files (30 points)

1. Write a program that prints the last `n` lines of a file to the screen. Write a function that is given a filename and `n` as arguments and prints the result to the terminal. You can use the _My Shadow_ poem to test your code. Do not use user input for this. Just call the function with two appropriate arguments. Again make sure to not print additional empty lines!

:::solution
```{ .python .exec wd=06_FileIO linelength=100 }
def last_n_lines(filename, n):
    """ writes the last n lines of a file to the terminal

    Args:
        filename: the name of the file.
        n: how many (last) lines are printed
    """
    with open(filename, "r") as poem:
        lines = poem.read().splitlines()

        for line in lines[-n:]:
            print(line)

last_n_lines("my_shadow.txt", 4)
```
:::


2. Read in the file `distances.txt`. It contains numbers with units meters (m), centimeters (cm) and millimeters (mm). Calculate the total distance in m and print your result to the terminal i.e. convert all numbers into the same unit, cast them and calculate the sum of all numbers.

3. Write the result to a **new** file called `total_distance.txt`.

4. Write the distances > 50 m to another **new** file called `greater_50.txt`.

\noindent
\textbf{Caution:} Think of a suitable structure to solve 2.2, 2.3, 2.4 . For that you should define functions that can be reused for several of the subtasks.
Nevertheless, make sure that each task (2.2, 2.3, 2.4) is solved. Also make sure that it does not matter whether you run your program for the first time or if you ran it multiple times before, it will have the intended output.


::: solution
```{ .python .exec script=distances.py wd=06_FileIO linelength=100 }
```
:::



# Working with csv files: Your own quiz (50 points)

Make a quiz that asks the user at least 5 different questions.
The questions are supposed to have one correct answer (i.e. do not ask something like "what is your opinion on xyz?").
There should always be exactly 3 possible answers to choose from.
Store the questions in a file `questions_answers.csv` together with their answers.
Your file should look like the example `questions_answers.csv` uploaded on StudIP.


## The quiz

 - say hello to the user
 - ask the user how many questions she wants to answer
 - the user is asked one question at a time
 - the user gives her answer as keyboard input
 - the user is told if she is right or wrong
 - then the next question is presented.
 - the user's score is presented at the end of the quiz
 - save the user's score to a file called `result.csv`


\noindent \textbf{Required:} Implement the quiz according to the requirements from above.
Save the user's name and the user's score (achieved and total possible score) in a csv file called `result.csv`.
When the quiz is played multiple times, the result file should have stored the records of all users that ever took the quiz.
Tip: you do not have to write a header for the `result.csv` file. \vspace{0.5em}

\noindent \textbf{Optional:} 1) Write down how you want to structure your code. Make a flowchart that visualizes the flow of data in your program. 2) Make the order of the questions random. \vspace{0.5em}

\noindent \textbf{Hints:} Use the csv library to read in from `questions_answers.csv`. You can use the `csv.DictReader`. \vspace{0.5em}

\noindent \textbf{Caution:} You do not have to catch all possible silly user inputs, but the case that the user asks for an inappropriate number of questions (e.g. for more questions than you can provide) should be handled.  \vspace{0.5em}


::: solution
\noindent Look at the sample solution `my_quiz.py`.
:::



# Thinking outside the box (15 points)

There are many different file formats. You already worked with `.txt` files and `.csv` files. Now you happen to browse the web and find the [**randomuser**]( https://randomuser.me) website. On the website you can find [**randomly generated user profiles**]( https://randomuser.me/api/). One random profile is saved in the file `random_user.json` and uploaded to StudIP.

\noindent
Look at the documentation for the [**Python JSON library**](https://docs.python.org/3/library/json.html) or other helpful sources.

1. What does `json.loads()` do to a string? Of what type is the output in our case?

2. Parse the `random_user.json` file into a dictionary.

3. Take the random user information from `random_user.json` and change the name into Max Mustermann (leave the other information as is).

4. What does `json.dumps()` do to a dictionary? Of what type is the output?

5. Save the random Max Mustermann user to the file `max_mustermann.json`.

6. Optional: What would have been faster than using loads and dumps?



::: solution

`json.loads()` takes the JSON file as a string and converts it (in our case) into a dictionary.

`json.dumps()` converts the dictionary to a string that is formatted like JSON.

```{ .python .exec script=generate_max_mustermann.py wd=06_FileIO linelength=100}
```
:::