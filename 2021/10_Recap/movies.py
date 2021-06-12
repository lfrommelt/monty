import csv

# TODO: add your functions and class definition here


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
