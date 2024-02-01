# Copy here code of line function from previous exercise
def line(length, char):
    if char == '':
        print(length * '*')
    else:
        first_char = char[0]
        print(length * first_char)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    rows = 0
    while rows < height:
        line(10, "#")
        rows += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
