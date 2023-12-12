# Write your solution here
def hash_square(length):
    amt = length
    while amt > 0:
        print("#" * length)
        amt -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)