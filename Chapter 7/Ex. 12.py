def leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return "This is a leap year!"
    elif year % 100 == 0 and year % 400 != 0:
        return "This is NOT a leap year!"
    else:
        if year % 4 == 0:
            return "This is also a leap year"
        else:
            return "This is NOT a leap year ..."


print(leap_year(2021))
