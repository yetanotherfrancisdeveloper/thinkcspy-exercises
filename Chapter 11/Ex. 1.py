# Exercise 1

# Using the text file studentdata.txt write a program that prints out the names of students that have more than six
# quiz scores. The file  contains one line for each student in an imaginary class. The student’s name is the first
# thing on each line, followed by some exam scores. The number of scores might be different for each student.


student_file = open("studentdata.txt", "r")

for line in student_file:
    student_line = line.split()
    if len(student_line[1:]) > 6:
        print("The student", student_line[0], "has more than 6 quiz scores.")

student_file.close()
