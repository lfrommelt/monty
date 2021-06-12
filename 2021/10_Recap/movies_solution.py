import csv


class Movie:
    """A movie contains a title and a release year."""

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


def movie_sort(movies):
    """Sorts a list of movies by their release date using bubble sort.

    Args:
        movies: a list of movies.

    Returns:
        A sorted list of movies.
    """
    # make a copy of the list of movies
    organized = movies.copy()

    # initialize flag that tracks if there was a swap
    swapped = True

    # swap as long as you found something to swap
    while swapped:
        swapped = False
        # go through the list (start with the second element)
        for i in range(1, len(organized)):
            # always compare two consecutive movies in the list (in regard to their year)
            # check if the first movie is older than the second
            if organized[i - 1].year > organized[i].year:
                # if that is the case, swap the position of the movies
                organized[i], organized[i - 1] = organized[i - 1], organized[i]
                # save that you found something that you swapped
                swapped = True

    return organized


def read_movies(filename):
    """Reads a csv file and returns a list of movies.

    Args:
        filename: The file to read.

    Returns:
        A list of movies.
    """
    movies = []
    with open(filename, 'r') as movie_file:
        for movie_record in csv.DictReader(movie_file):
            movies.append(
                Movie(movie_record['Title'], int(movie_record['Year'])))
    return movies


def print_movies(movies):
    """Prints a list of movies.

    Args:
        A list of movies.
    """
    for movie in movies:
        print(movie)


def main():
    """Reads a list of movies from bond.csv and sorts it."""
    movies = read_movies('bond.csv')

    print('Original list:')
    print_movies(movies)

    sorted_movies = movie_sort(movies)
    print('\nSorted list by year:')
    print_movies(sorted_movies)


if __name__ == '__main__':
    main()
