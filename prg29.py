min = int(input("Enter the time in munites"))
hours = min//60
if(hours == 0):
 minutes = min
else:
 minutes = min%60
print("hours:minutes",hours,minutes)
