# Write your solution here
import string
import random

def generate_password(length: int):
    # desired_length is length of password
    # all lowercase chars a-z

    password = ''
    for x in range(length):
        random_letter = random.choice(string.ascii_letters).lower()
        password += random_letter
    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))

