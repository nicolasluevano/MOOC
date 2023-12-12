# Write your solution here
how_many = int(input('How many times a week do you eat at the student cafeteria? '))
price = float(input('The price of a typical student lunch?'))
spend = float(input('How much money do you spend on groceries in a week?'))

spend_one = price * how_many
weekly = spend_one + spend
daily = weekly / 7

print(f'Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros ')