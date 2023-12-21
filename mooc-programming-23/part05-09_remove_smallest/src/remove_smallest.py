# Write your solution here
def remove_smallest(numbers: list):

    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i

    numbers.remove(smallest)








if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)