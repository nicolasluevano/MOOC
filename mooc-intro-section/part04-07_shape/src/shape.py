# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(length, char):
    if char == '':
        print(length * '*')
    else:
        first_char = char[0]
        print(length * first_char)

def triangle(length, char):
    # You should call function line here with proper parameters
    rows = 1
    while rows <= length:
        line(rows, char)
        rows += 1


def shape(a, b, c, d):
    triangle(a,b)
    rows = 1
    while rows <= c:
        line(a,d)
        rows +=1

if __name__ == "__main__":
    shape(5, "X", 3, "*")