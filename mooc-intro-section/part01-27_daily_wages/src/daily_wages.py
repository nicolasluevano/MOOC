# Write your solution here
hourly = float(input("Hourly wage:"))
worked = int(input("Hours worked:"))
day = input("Day of the week")
wages = float(hourly * worked)
sunday_wages = (hourly * 2) * worked

if day != "Sunday":
    print(f'Daily wages: {wages} euros')
else: print(f'Daily wages: {sunday_wages} euros')