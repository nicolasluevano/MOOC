# Copy here code of line function from previous exercise
def line(length, char):
    if char == '':
        print(length * '*')
    else:
        first_char = char[0]
        print(length * first_char)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    rows = 0
    while rows < size:
        line(size, "#")
        rows += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
