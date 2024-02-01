# Write your solution here
def get_lottery_data():
    # read lottery numbers
    lottery_data = []
    with open("src/lottery_numbers.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            lottery_data.append(parts)
    return lottery_data


def filter_days(lottery_data: list):
    correct_days = []
    for data in lottery_data:
        week_info = []
        day_info = []
        week_info.append(data[0].split())
        day_info.append(week_info[0][1])
        for i in day_info:
            try:
                int(i)
                correct_days.append(data)
            except ValueError:
                print('week number is incorrect')
    return correct_days

def filter_numbers(correct_days):
    # one or more numbers not correct
    lottery_numbers = []
    correct_numbers = []
    for numbers in correct_days:
        lottery_numbers.append(numbers[1].split(','))
    for num in lottery_numbers:
        valid = True
        if len(num) == 7:
            for number in num:
                if not number.isdigit() and 1 <= int(number) >= 39:
                    valid = False 
            if valid:
                correct_numbers.append(num)
    print(correct_numbers)







filter_numbers(filter_days(get_lottery_data()))

