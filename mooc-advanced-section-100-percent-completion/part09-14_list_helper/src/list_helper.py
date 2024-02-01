# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(self, my_list: list):

        counter = 0
        num = my_list[0]

        for i in my_list:
            current = my_list.count(i)
            if current > counter:
                counter = current
                num = i
        return num


    @classmethod
    def doubles(self, my_list: list):
        num_count = {}
        appears_twice = 0
        for i in my_list:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1

        for i in num_count:
            if num_count[i] >= 2:
                appears_twice += 1
        return appears_twice

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
