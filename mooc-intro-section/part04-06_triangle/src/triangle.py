# Copy here code of line function from previous exercise
def line(length, char):
    if char == '':
        print(length * '*')
    else:
        first_char = char[0]
        print(length * first_char)

def triangle(size):
    # You should call function line here with proper parameters
    rows = 1
    while rows <= size:
        line(rows, "#")
        rows += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
