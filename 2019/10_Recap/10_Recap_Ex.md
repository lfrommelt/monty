---
title: BPP Exercise 10 -- Recap
date: 2019-06-16
...


\noindent
This week we will focus on practicing the concepts that you learned so far. To solve the exercises you do not only need to download this exercise sheet, but also all files that are referenced in the exercises (`hangman_game.py`, `hangman_words.txt`, `movies.py`, `bubblesort.py`).



# Warm-up

## There’s always more than one way to solve a problem! (16 points)

Can you write code which performs the following tasks by using

a) for loops,
b) list comprehensions?

Name your file `manyways.py`.

1. Convert the list `string.ascii_lowercase` into a list of its ascii values
   (use `ord(x)`).
   The desired output is: `[97, 98, 99, ...]`.
2. Create a list which contains all numbers starting at 1 except for those that contain a `3`, up to 47.
   The desired output is: `[1, 2, 4, 5, ..., 47]`.

*Note*: To use `string.ascii_lowercase`, you need to import `string`.  \vspace{1em}

::: solution
```{ .python .exec wd=10_Recap script=manyways.py linelength=90 }
```
:::



## Fizz Buzz (18 points)

Fizz Buzz is a simple children's game: Count up the numbers from 1 to N and whenever a number is divisible by 3 instead of saying the number say `fizz` (i.e. print `fizz` to the terminal). If a number is divisible by 5, say `buzz` instead. If the number is divisible by 3 and 5, say `fizzbuzz`. \vspace{0.5em}

\noindent Write a script `fizz_buzz.py`. Implement a function `fizz(number)` and a function `buzz(number)`. The function `fizz` should return `True` iff (= if and only if) `number` is divisible by 3. The function `buzz` should return `True` iff `number` is divisible by 5. \vspace{0.5em}

\noindent Next implement a function `fizz_buzz(limit)` which plays a game of Fizz Buzz from 1 up to number `limit` (inclusive). Use the functions `fizz` and `buzz` to test, if a number is divisible by 3 or 5.  \vspace{1em}

::: solution
```{ .python .exec wd=10_Recap script=fizz_buzz.py }
```
:::




# File I/O

## Hangman (34 points)

Let's implement a little game: In Hangman one person (in our case the computer) picks a random word and tells us how many letters there are, e.g. for `hello` it would tell us: `_____`.
Now your job is to guess the word, letter by letter.
So if you would guess `e`, the computer would reveal `_e___`.
If you then guessed `l`, the result would be `_ell_`.
Traditionally, for each wrong letter guessed, a player would get another stroke of the little hangman.
Eventually the stick figure will hang -- or you solve the word and win!
Since it's hard to visualize the stick figure on the terminal, you might want to just use a counter. \vspace{0.5em}


\noindent\textbf{Task}

\noindent Extend the script `hangman_game.py` which should implement a game of hangman. In the accompanying `*.zip` archive there is a file called `hangman_words.txt` which you should use (but you can change it as much as you like) to read the list of possible words. There are already function definitions in the script `hangman.py`. Write your code where it says `#TODO  Your code goes here`. Don't forget to comment your code. \vspace{0.5em}

\noindent\textbf{Example pseudocode}
```
Set number of misses
Read possible words
Pick one word
Prepare guess word with underscores
Present user with the "rules"
While not guessed and more than 0 misses left:
    Present current game state
    Get letter from user input
    If letter exists in chosen word:
        Update guess word
        If guessed:
            Win
    Else:
        Update list of failures and misses
        If no misses left:
            Lose
```
\vspace{0.5em}

\noindent\textbf{Hints}

\noindent Strings are immutable, so you **cannot** do something like this:

```python
a = 'hello'
a[3] = 'b'
```

\noindent Instead, try to represent the *guess word* as a list filled with underscores,
like this:

```python
word = 'hello'
guess_word = ['_', '_', '_', '_', '_']
```

\noindent Then, whenever a letter is guessed, check if it is inside the word, and if so,
update the `guess_word` accordingly (this code snippet is **not** really useful,
but remember the keyword `in`):

```python
if 'l' in word:
    guess_word[word.index('l')] = 'l'
```

\noindent Similarly, to check if the game is won, you just need to see if there are still `_`s inside the list. \vspace{0.5em}

\noindent By using the script `hangman_game.py` your code will be structured into several function which only do small bits, e.g.
a function which checks if you won, one which prints the current game state, one which reads in the file, etc. \vspace{0.5em}


\noindent Playing your game could look like this:

```output
Hello! Let's play a game of hangman!
I already picked a word, and you now have to guess letters.
But be warned, if you guess more than 5 times wrong, you lose!

Word: ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'] Wrong guesses: []
Next guess? a
Word: ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'] Wrong guesses: ['a']
Next guess? e
Word: ['_', '_', '_', '_', 'e', '_', '_', 'e', '_', '_'] Wrong guesses: ['a']
Next guess? i
Word: ['_', '_', '_', '_', 'e', '_', '_', 'e', '_', '_'] Wrong guesses: ['a', 'i']
Next guess? o
Word: ['_', '_', 'o', '_', 'e', '_', '_', 'e', '_', '_'] Wrong guesses: ['a', 'i']
Next guess? s
Word: ['_', '_', 'o', '_', 'e', '_', '_', 'e', '_', 's'] Wrong guesses: ['a', 'i']
Next guess? u
Word: ['_', '_', 'o', '_', 'e', '_', '_', 'e', 'u', 's'] Wrong guesses: ['a', 'i']
Next guess? r
Word: ['_', 'r', 'o', '_', 'e', '_', '_', 'e', 'u', 's'] Wrong guesses: ['a', 'i']
Next guess? h
Word: ['_', 'r', 'o', '_', 'e', '_', 'h', 'e', 'u', 's'] Wrong guesses: ['a', 'i']
Next guess? t
Word: ['_', 'r', 'o', '_', 'e', 't', 'h', 'e', 'u', 's'] Wrong guesses: ['a', 'i']
Next guess? p
Word: ['p', 'r', 'o', '_', 'e', 't', 'h', 'e', 'u', 's'] Wrong guesses: ['a', 'i']
Next guess? n
Word: ['p', 'r', 'o', '_', 'e', 't', 'h', 'e', 'u', 's'] Wrong guesses: ['a', 'i', 'n']
Next guess? s
Word: ['p', 'r', 'o', '_', 'e', 't', 'h', 'e', 'u', 's'] Wrong guesses: ['a', 'i', 'n']
Next guess? m
Word: ['p', 'r', 'o', 'm', 'e', 't', 'h', 'e', 'u', 's'] Wrong guesses: ['a', 'i', 'n']
You win! It was "prometheus".
```


::: solution
```{ .python wd=10_Recap script=hangman_game_solution.py }
```
:::


# Thinking Outside the Box

## Bubble sort (5 points)

Investigate how the sorting algorithm bubble sort works.
Create a file `bubble_sort_explained.txt` in which you write 1 sentence describing bubble sort.
Also add a link to a video that demonstrates or explains bubble sort.



## Sorting Bond movies (27 points)

For this exercise, make all your changes inside the `movies.py`.
Your task is to change bubble sort to sort some Bond movies. The code for the sorting algorithm is provided in the folder (see `bubblesort.py`).
You can find a `bond.csv` file inside the accompanying zip file.
It is a simplified list of [Wikipedia's List of James Bond films](https://en.wikipedia.org/wiki/List_of_James_Bond_films#Box_office_and_budget). \vspace{0.5em}

\noindent Create a class `Movie` which models a movie:

- A movie has a `title`.
- A movie has a release `year`.
- Implement the `__str__` method such that printing a film shows the title
  followed by the year in parentheses:
\noindent `From Russia with Love (1963)`  \vspace{0.5em}

\noindent Define the function `movie_sort` in the script `movies.py` that takes a list of movie objects as an argument and returns an ordered list of movie objects.
Inside the zip file for this homework you will find an implementation of bubble sort (in `bubblesort.py`).
Use this code to implement the function `movie_sort` to sort a list of movies by their release years.
For this, copy the code from `bubblesort.py` and adapt it so that it can sort the movies.
Comment the code (make sure you add inline comments for the function `movie_sort`! \vspace{0.5em}

\noindent The script `movies.py` is provided.
Conclude from it, which functions have to be implemented.
Make sure that you organize your code into functions and write docstrings.
When you execute the final script, the bond movies are supposed to be read from the csv file (you can use the `csv` library), get sorted, and printed nicely formated (one row per movie) to the terminal in the sorted order. \vspace{2em}

\noindent Overview:

- create a class `Movie`
- think about necessary attributes and dundor methods
- write a fuction that reads the provided csv file and returns a list of movies
- write a function that sorts the movies (copy the code from `bubblesort.py` and make necessary changes)
- write a function that prints a list of movies
- put all of them in the `movies.py`


::: solution
```{ .python .exec wd=10_Recap script=movies_solution.py }
```
:::