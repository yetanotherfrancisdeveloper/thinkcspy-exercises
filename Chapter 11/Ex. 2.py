# Exercise 2

# Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for each
# student, and print out the student’s name along with their average grade.


student_file = open("studentdata.txt", "r")

for line in student_file:
    student_line = line.split()
    total_grades = 0
    for grade in student_line[1:]:
        total_grades += int(grade)
    average = total_grades / len(student_line[1:])
    print(f"The average of {student_line[0]} is {round(average, 2)}, m'kay?")

student_file.close()
