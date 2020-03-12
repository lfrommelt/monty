---
title: BPP Exercise 12 -- Getting data from the web
date: 2019-07-07
...

# Warm-up


## Is my credit card valid?  (20 points)

Let's check if your credit card is valid.
Every time you make a transaction with your credit card, it will be validated with a pretty simple algorithm. If this first test passes, more costly tests will be performed before the transaction takes place. The first and simple algorithm is called Luhn Algorithm and works as described by the following picture [@luhn_2018]:\newline
![Luhn Algorithm.](Luhn-Algorithm.png){ width=50% height=50% }

1. Write a script that takes a 16-digit card number as a command line argument (!) and prints to the terminal whether it belongs to a valid credit card. To see how to work with command line arguments, please review Lecture 08 (more specifically sheet 08 exercise 2 hint 1). \vspace{1em}

\noindent \textbf{Requirements:}

- Your script should have the name `luhn.py`
- Your script should have a function called `check_validity` that takes a credit card number as an argument and returns `True` if the card number is valid and `False` otherwise.
- The answer should be printed nicely to the terminal.
- The answer should  only be printed to the terminal if the script is run as the main program.
- Write another script that is called `test_luhn.py`. Import your `check_validity` function. If the test script is run as the main program, it should check whether the following list of credit card numbers are valid: `["4137894711755904", "6499802450273568", "8504172191273888", "0043668783485480"]`


::: solution

\noindent Thanks to https://www.101computing.net/is-my-credit-card-valid/

```{ .python wd=12_Web_scraping script=luhn.py }
```

```{ .python wd=12_Web_scraping script=test_luhn.py }
```
:::



## JSON repetition (10 points)

Create an `about_me.json` file with the following information:

- your name
- your favorite programming language
- a list of your three favorite animals \vspace{1em}


\noindent Create this file by first creating a script called `about_me.py`.
The script should have a variable  `my_inf` (a dictionary) and a function `write_to_file` that takes the dictionary and a filename as arguments.
Use `json.dump(info_dict, fh, indent=4)` to dump the string into a json file with an indentation of 4. 
You do not need to open the file with your script again. \vspace{1em}

\noindent So your script should create a json file that looks something like this:
```{ wd=12_Web_scraping script=about_me.json }
```

\noindent \textbf{Requirements:}

- your script should have a `main()`
- your script should not create any output if it is imported

::: solution
```{ .python wd=12_Web_scraping script=about_me.py }
```
:::


# Web APIs

## Installing *requests* (5 points)

The package *requests* is the first package that you need to install manually.
There is a whole chapter about how to install Python packages in the [Python Documentation](https://docs.python.org/3/installing/index.html). \vspace{1em}


\noindent \textbf{Short excerpt from the Python Documentation:}

> Installing Python Modules
>
> As a popular open source development project, Python has an active supporting community of contributors and users that also make their software available for other Python developers to use under open source license terms.
> 
> This allows Python users to share and collaborate effectively, benefiting from the solutions others have already created to common (and sometimes even rare!) problems, as well as potentially contributing their own solutions to the common pool.
> 
> This guide covers the installation part of the process.
> 
> `pip` is the preferred installer program. Starting with Python 3.4, it is included by default with the Python binary installers.


\noindent Go ahead and read the documentation above to learn more about installing packages. To install *requests*, type `pip3 install requests` or `pip install requests` into your command line.


## Summarize the purpose of Web APIs and querying them (10 points)

In the lecture you learned about Web APIs and how to query them for information. Summarize the main points of the lecture by answering the following questions:

- What is the advantage of using Python over a browser to do web requests?
- How can we limit the number of website requests our scripts do and why should we do it?
- Name a common data format used for Web APIs.

::: solution
We are using Web APIs to gather information from websites for further customized processing. For example, we could get a list of actors and their dates of birth and calculate their age. 
Doing this processing with a browser is tedious and involves many steps, from clicking on links to copying the data into a program. Using Python (or other programming languages) we are in control and can modify the data as we like.
Many publicly available Web APIs serve their data as JSON, XML or CSV files, all of which are common data formats used on the web.
To avoid overloading a server with requests, what could be seen as a cyber attack, there are a few methods to do ethic web crawling. For example, we could rate limit our requests, i.e. only send a request every second or so. Or, we could store information as a file and only retrieve a new one if the file is outdated or destroyed.
:::

## Simple API query: Quote of the day (25 points)

Look at this link: [https://favqs.com/api](https://favqs.com/api) \vspace{0.5em}

\noindent The website FavQs has several Web APIs. Most of them need some kind of authorization, but the quote of the day works without authentication. Find out how to query the quote of the day. (It is not actually a quote of the *day*, each time you request it again, it will be something different.)  \vspace{0.5em}

\noindent For example, you might get a quote like the following:

```output
{"qotd_date":"2019-06-24T00:00:00.000+00:00","quote":{"id":27339,"dialogue":false,"priva
te":false,"tags":["nature","life","good"],"url":"https://favqs.com/quotes/william-shakes
peare/27339-and-this-our--","favorites_count":0,"upvotes_count":1,"downvotes_count":0,"a
uthor":"William Shakespeare","author_permalink":"william-shakespeare","body":"And this, 
our life, exempt from public haunt, finds tongues in trees, books in the running brooks,
 sermons in stones, and good in everything."}}
```

\noindent Write a Python script which requests the quote of the day and prints it alongside its author, similar to the following output:

```output
William Shakespeare said: "And this, our life, exempt from public haunt, finds tongues i
n trees, books in the running brooks, sermons in stones, and good in everything."
```

\noindent Make sure that the script outputs an error message if the HTTP status code of the request is not `200` (`OK`).\vspace{1em}

::: solution
```{ .python .exec wd=12_Web_scraping script=quote_of_the_day.py }
```
:::



# National holidays  (30 points)

Visit [nager.date](https://date.nager.at/) a web service to query for national holidays. \vspace{0.5em}

\noindent Type *Nicaragua* into the search bar on the left to get more information about the national holidays in Nicaragua.
Download the csv file of the national holidays for 2019 of Nicaragua and save them to your homework folder.

1. Write a script that determines how many holiday days there are in Nicaragua in 2019.
Your program should take the name of the csv file as a command line argument and display the answer on the terminal.

2. Next, visit the API documentation of nager.date at https://date.nager.at/Api.
Try out the example and explain, how we have to use the API.
In the example, what does `AT` stand for? In your words, how is the API response structured?

3. Provide the link to get the national holidays for Germany in 2019. \vspace{0.5em}

\noindent \textbf{Your choice:} Do it with scripts and programming if you feel comfortable, otherwise do it manually by inspecting your results and writing down what you did:

4. Find out how many holidays more there are in Germany than in Nicaragua in 2019. Consider all listed holidays (they do not have to be observed in the whole country).


::: solution

\noindent 1.

```{ .python wd=12_Web_scraping script=holiday_count.py }
```
\vspace{1em}

\noindent 2.

\noindent The example, https://date.nager.at/api/v2/PublicHolidays/2017/AT, queries for the public holidays in Austria in 2017. `AT` is Austria's country code.
The response is a JSON containing a list of the public holidays represented by their names, dates, localized names and some meta information, i.e. whether the day is always on the same date every year or if it is "global", that is whether the holiday is observed across the whole country. \vspace{1em}


\noindent 3.

\noindent https://date.nager.at/api/v2/publicholidays/2019/DE
\vspace{1em}


\noindent 4.

```{ .python .exec wd=12_Web_scraping script=holiday_comparison.py }
```
:::


# References