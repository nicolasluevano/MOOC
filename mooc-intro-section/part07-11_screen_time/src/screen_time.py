# Write your solution here

# take in name of file to be saved as
# request starting date
# request how many days to record

# create a function that takes start date and prompts the user for input for how many days
# append to file after each entry

from datetime import datetime, timedelta

while False:
    start_date = input("Starting date:")
    date = datetime.strptime(start_date, "%d.%m.%Y")
else:
    date = datetime.strptime('24.6.2020', "%d.%m.%Y")
    days = 5
    filename = "late_june.txt"


def entry(date, days, filename):
    date = date
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    with open(f"{filename}", "w") as my_file:
        for i in range(days):
            entry = input(f'Screen time {date}:')
            print(entry.strftime("%M/"))
            date += timedelta(days=1)
    print(f"Data stored in {filename}")


entry(date, days, filename)
