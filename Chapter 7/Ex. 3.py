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
