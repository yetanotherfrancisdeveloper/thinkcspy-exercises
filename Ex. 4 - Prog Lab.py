
startHolidayInt = int(input("When do you plan to go on holiday "
                            "(write a number from 0 to 6, "
                            "where 0 corresponds to Monday and 6 to Sunday)? "))
lengthHolidayInt = int(input("How many days are you planning to stay? "))

weekDays = 7
returnDay = (startHolidayInt + lengthHolidayInt) % weekDays
print("The number of the day of the week you will return on is:", returnDay)
