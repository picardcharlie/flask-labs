import datetime

def chinese_zodiac(date):
    """
    Find Chinese zodiac animal based off of birth year.
    Uses a datetime variable as input.
    returns a str of the animal.
    """

    zodiac_dic = {"Rat": 1948, "Ox": 1949, "Tiger": 1950, "Rabbit": 1951, "Dragon": 1952, "Snake": 1953, "Horse": 1954,
                  "Goat": 1955, "Monkey": 1956, "Rooster": 1957, "Dog": 1958, "Pig": 1959}

    find_zodiac = date.year

    while(True):
        if find_zodiac in zodiac_dic.values():
            for animal, date in zodiac_dic.items():
                if date == find_zodiac:
                    zodiac_sign = animal
            break
        else:
            find_zodiac -= 12

    return zodiac_sign