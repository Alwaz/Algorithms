## time input as String
## hours
## minutes
## seconds
time = input('Enter time in 12 hour formate: ')
hours = int(time[0:2])
minutes = int(time[3:5])
seconds = int(time[6:8])
AM_PM = time[8:]

if AM_PM == 'PM' and hours != 12:
    hours+=12
elif AM_PM == 'AM' and hours == 12:
    hours = 0

#     formate string
print('{:02}:{:02}:{:02}'.format(hours,minutes,seconds))




