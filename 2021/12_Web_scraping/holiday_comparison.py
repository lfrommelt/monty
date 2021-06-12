import requests


def compare_holiday_counts(country_code1, country_code2, year=2019):
    """Returns the difference between the holiday counts of country 1 and country 2.

    Args:
        country_code1: The ISO 3166-1 alpha-2 country code for country 1.
        country_code2: The ISO 3166-1 alpha-2 country code for country 2.
        year: The year to use for the comparison.

    Returns:
        The number of holidays of country 1 minus the number of holidays of country 2.
    """
    # build the link depending on the country that you are looking for
    link = 'https://date.nager.at/api/v2/publicholidays/{year}/{country_code}'
    link1 = link.format(year=year, country_code=country_code1)
    link2 = link.format(year=year, country_code=country_code2)

    # request information as json
    holidays1 = requests.get(link1).json()
    holidays2 = requests.get(link2).json()

    # calculate the difference
    return len(holidays1) - len(holidays2)


if __name__ == '__main__':
    country_code1 = "DE"
    country_code2 = "NI"

    print("{} has {} more days of holidays than {}.".format(country_code1,
                                                            compare_holiday_counts(country_code1, country_code2), country_code2))
