from datetime import date
# datetime(YYYY,MM,DD)
# aries 3-21 to 4-19

# I'm sure there is a better way of doing this.  But... I don't want to think too hard so I did it like this.

aries_start = date(1, 3, 21)
aries_end = date(1, 4, 19)
taurus_start = date(1, 4, 20)
taurus_end = date(1, 5, 20)
gemini_start = date(1, 5, 21)
gemini_end = date(1, 6, 20)
cancer_start = date(1, 6, 21)
cancer_end = date(1, 7, 22)
leo_start = date(1, 7, 23)
leo_end = date(1, 8, 22)
virgo_start = date(1, 8, 23)
virgo_end = date(1, 9, 22)
libra_start = date(1, 9, 23)
libra_end = date(1, 10, 22)
scorpio_start = date(1, 10, 23)
scorpio_end = date(1, 11, 21)
sagittarius_start = date(1, 11, 22)
sagittarius_end = date(1, 12, 21)
capricorn_start = date(1, 12, 22)
capricorn_end = date(1, 1, 19)
aquarius_start = date(1, 1, 20)
aquarius_end = date(1, 2, 18)
pisces_start = date(1, 2, 19)
pisces_end = date(1, 3, 20)
#birthday = date(2001, 3, 29)

def astro(date):
    """
    Find astrology sign based off of import from user.
    takes in a datetime variable.
    returns a string of the sign.
    """

    birthday = date
    if birthday.month == aries_start.month:
        if birthday.day >= aries_start.day:
            return "aries"
    elif birthday.month == aries_end.month:
        if birthday.day <= aries_end.day:
            return "aries"

    if birthday.month == taurus_start.month:
        if birthday.day >= taurus_start.day:
            return "taurus"
    elif birthday.month == taurus_end.month:
        if birthday.day <= taurus_end.day:
            return "taurus"

    if birthday.month == gemini_start.month:
        if birthday.day >= gemini_start.day:
            return "gemini"
    elif birthday.month == gemini_end.month:
        if birthday.day <= gemini_end.day:
            return "gemini"

    if birthday.month == cancer_start.month:
        if birthday.day >= cancer_start.day:
            return "cancer"
    elif birthday.month == cancer_end.month:
        if birthday.day <= cancer_end.day:
            return "cancer"

    if birthday.month == leo_start.month:
        if birthday.day >= leo_start.day:
            return "leo"
    elif birthday.month == leo_end.month:
        if birthday.day <= leo_end.day:
            return "leo"

    if birthday.month == virgo_start.month:
        if birthday.day >= virgo_start.day:
            return "virgo"
    elif birthday.month == virgo_end.month:
        if birthday.day <= virgo_end.day:
            return "virgo"

    if birthday.month == libra_start.month:
        if birthday.day >= libra_start.day:
            return "libra"
    elif birthday.month == libra_end.month:
        if birthday.day <= libra_end.day:
            return "libra"

    if birthday.month == scorpio_start.month:
        if birthday.day >= scorpio_start.day:
            return "scorpio"
    elif birthday.month == scorpio_end.month:
        if birthday.day <= scorpio_end.day:
            return "scorpio"

    if birthday.month == sagittarius_start.month:
        if birthday.day >= sagittarius_start.day:
            return "sagittarius"
    elif birthday.month == sagittarius_end.month:
        if birthday.day <= sagittarius_end.day:
            return "sagittarius"

    if birthday.month == capricorn_start.month:
        if birthday.day >= capricorn_start.day:
            return "capricorn"
    elif birthday.month == capricorn_end.month:
        if birthday.day <= capricorn_end.day:
            return "capricorn"

    if birthday.month == aquarius_start.month:
        if birthday.day >= aquarius_start.day:
            return "aquarius"
    elif birthday.month == aquarius_end.month:
        if birthday.day <= aquarius_end.day:
            return "aquarius"

    if birthday.month == pisces_start.month:
        if birthday.day >= pisces_start.day:
            return "pisces"
    elif birthday.month == pisces_end.month:
        if birthday.day <= pisces_end.day:
            return "pisces"
