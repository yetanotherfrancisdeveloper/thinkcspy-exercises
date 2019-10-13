
currentTimeInt = int(input("What time is it in hours (24 hours format)? "))
alarmTimeInt = int(input("How many hours from now do you have to wait for the alarm to go off? "))

dayHours = 24
timeAlarmOff = (alarmTimeInt + currentTimeInt) % dayHours
print("The time on your clock when the alarm will go off will be:", timeAlarmOff)
