
import requests
import json


def quote_of_the_day():
    """get the quote of the day from web api as nicely formatted string

    Returns:
        str -- nicely formatted quote
    """
    # request data from link
    link = "https://favqs.com/api/qotd"
    response_obj = requests.get(link)

    # get and check status code
    status = response_obj.status_code
    if status != 200:
        return "Could not retrieve a quote of the day."

    # get the data in json
    data = response_obj.json()

    # parse for information
    author = data['quote']['author']
    quote = data['quote']['body']

    return '{author} said: "{quote}"'.format(author=author, quote=quote)


if __name__ == "__main__":
    print(quote_of_the_day())
