# Write your solution here
def times_ten(start_index: int, end_index: int):
    result = {}
    for i in range(start_index, end_index + 1):
        result[i] = i * 10
    return result

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)