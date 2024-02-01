# Write your solution here
def greatest_number(num1, num2, num3):
    greatest_num = None
    if num1 > num2:
        greatest_num = num1
    else:
        greatest_num = num2
    if greatest_num > num3:
        return greatest_num
    else:
        return num3

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(0, 0, 0)
    print(greatest)