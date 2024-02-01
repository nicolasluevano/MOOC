# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(numbers: list, limit: int):
    return [number for number in numbers if number >= limit]

if __name__ == "__main__":
    print(remove_smaller_than([-4, 7, 8, -100], 0))
