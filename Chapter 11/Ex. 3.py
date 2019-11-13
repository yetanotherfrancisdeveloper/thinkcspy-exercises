student_file = open("/studentdata.txt", "r")

for line in student_file:
    student_line = line.split()
    grades = []
    for grade in student_line[1:]:
        grades += [int(grade)]
    minimum = min(grades)
    maximum = max(grades)
    print("For the student", student_line[0], "the minimum is equal to", minimum,
          "while the maximum is equal to", maximum, "m'kay?")

student_file.close()
