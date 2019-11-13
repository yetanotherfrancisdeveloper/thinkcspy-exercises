student_file = open("/studentdata.txt", "r")

for line in student_file:
    student_line = line.split()
    if len(student_line[1:]) > 6:
        print("The student", student_line[0], "has more than 6 quiz scores.")

student_file.close()
