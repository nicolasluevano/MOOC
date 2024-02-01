# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers) > 0:
            return sum(self.numbers)
        else:
            return 0

    def average(self):
        if len(self.numbers) > 0:
            return self.get_sum() / self.count_numbers()
        else:
            return 0


def main():
    stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    while True:
        value = int(input("Enter a number:"))
        if value == -1:
            print("Sum of numbers:", stats.get_sum())
            print("Mean of numbers:", stats.average())
            print("Sum of even numbers:", even_stats.get_sum())
            print("Sum of odd numbers:", odd_stats.get_sum())
            break
        elif value % 2 == 0:
            stats.add_number(value)
            even_stats.add_number(value)
        else:
            stats.add_number(value)
            odd_stats.add_number(value)


main()





# stats = NumberStats()
# stats.add_number(1)
# stats.add_number(-1)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())