# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date

def list_years(dates: list):
    years_list = []
    for dte in dates:
        years_list.append(dte.year)
    years_list.sort()
    return years_list


if __name__ == "__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)