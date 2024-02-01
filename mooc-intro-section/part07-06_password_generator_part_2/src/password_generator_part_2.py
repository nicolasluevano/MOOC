# Write your solution here
# Write your solution here
import string
import random

def generate_strong_password(length: int, arg1: bool, arg2: bool):
    # desired_length is length of password
    # all lowercase chars a-z
    # if arg1 is True, password should contain one or more numbers
    # if arg2 is True, password should contain on or more special chars !?=+-()#
    # password should always contain at least one lowercase alphabet

    password = ''
    while len(password) < length:
        print(len(password))
        random_letter = random.choice(string.ascii_letters).lower()
        password += random_letter
        if arg1 and len(password) < (length):
            random_number = random.randint(0, 9)
            password += str(random_number)
        if arg2 and len(password) < (length):
            chars = ['!', '?', '=', '+', '-', '(', ')', '#']
            random_char = random.choice(chars)
            password += random_char
    print(len(password))
    return password


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(16, False, True))

