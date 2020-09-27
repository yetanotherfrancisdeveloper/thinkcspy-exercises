# Exercise 3

# Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to
# this scheme (check it on the book)

# The square and round brackets denote closed and open intervals. A closed interval includes the number, and open
# interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.
# Test your function by printing the mark and the grade for a number of different marks.


def grade_mark(grade):
    """Given an exam mark, returns the grade for that mark"""
    if grade >= 90:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    else:
        return "F"


print(grade_mark(65))
