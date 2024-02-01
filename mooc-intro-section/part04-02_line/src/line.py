# Write your solution here
# You can test your function by calling it within the following block
def line(length, char):
    if char == '':
        print(length * '*')
    else:
        first_char = char[0]
        print(length * first_char)

if __name__ == "__main__":
    line(5, "")