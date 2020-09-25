# Exercise 4

# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful
# holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a
# Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of
# your stay, and it will tell you the number of day of the week you will return on.

# Ask for the starting day of the holiday and its length. The answers need to be integers.
start_holiday = int(input("When do you plan to go on holiday (write a number from 0 to 6, where 0 corresponds to "
                          "Monday and 6 to Sunday)? "))
length_holiday = int(input("How many days are you planning to stay? "))

week_days = 7
# Compute the day of return by using the '%' operator as in 'Exercise 3'.
return_day = (start_holiday + length_holiday) % week_days
# Print the result.
print("The number of the day of the week you will return on is:", return_day)
