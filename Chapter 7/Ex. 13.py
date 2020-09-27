# Exercise 13

# Implement the calculator for the date of Easter.
# The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.
# Ask the user to enter a year. Compute the following:
#         a = year % 19
#         b = year % 4
#         c = year % 7
#         d = (19 * a + 24) % 30
#         e = (2 * b + 4 * c + 6 * d + 5) % 7
#         dateofeaster = 22 + d + e

# Special note: The algorithm can give a date in April. Also, if the year is one of four special years
# (1954, 1981, 2049, or 2076) then subtract 7 from the date.

# Your program should print an error message if the user provides a date that is out of range.


def date_of_easter(year):
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            date = date - 7
        if date > 31:
            return "April " + str(date - 31)
        else:
            return "March " + str(date)
    else:
        return "ERROR!"


print(date_of_easter(1899))
print(date_of_easter(2016))
print(date_of_easter(2049))
print(date_of_easter(2020))
