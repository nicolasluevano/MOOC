# Write your solution here
from datetime import datetime

day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))
mil_eve = datetime(1999, 12, 31)
current = datetime(year, month, day)

if year > 1999:
    print("You weren\'t born yet on the eve of the new millennium.")
else:
    result = mil_eve - current
    print(f"You were {result.days} days old on the eve of the new millennium.")

