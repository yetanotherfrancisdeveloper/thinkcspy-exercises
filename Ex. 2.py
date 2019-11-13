student_file = open("/studentdata.txt", "r")

for line in student_file:
    student_line = line.split()
    total_grades = 0
    for grade in student_line[1:]:
        total_grades += int(grade)
    average = total_grades / len(student_line[1:])
    print("The average of", student_line[0], "is", "{0:.{1}f}".format(average, 2), "m'kay?")

student_file.close()
