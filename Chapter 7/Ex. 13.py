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
