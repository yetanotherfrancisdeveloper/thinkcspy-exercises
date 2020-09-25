# Exercise 3

# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you
# set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the
# above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on the clock when the alarm goes off.

# Ask for the current time and the hours to wait for the alarm to go off using 'input'.
# The answer needs to be an integer, that's why 'int' is used.
current_time = int(input("What time is it in hours (24 hours format)? "))
alarm_wait_hours = int(input("How many hours from now do you have to wait for the alarm to go off? "))

day_hours = 24
# '%' returns the remainder of the division between the sum on the left and the 'day_hours' on the right.
alarm_off_time = (current_time + alarm_wait_hours) % day_hours
# Prints the result obtained above.
print("The time on your clock when the alarm will go off will be:", alarm_off_time)
