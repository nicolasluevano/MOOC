# Write your solution here
def create_tuple(x: int, y: int, z: int):
    numbers = [x, y, z]
    smallest = sorted(numbers)[0]
    greatest = sorted(numbers)[-1]
    sum = x + y + z
    return smallest, greatest, sum


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))