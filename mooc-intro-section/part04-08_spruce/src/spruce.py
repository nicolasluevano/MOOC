# Write your solution here
# You can test your function by calling it within the following block
def spruce(branch_rows):
    rows = 1
    branches = 1
    if branch_rows >= 5:
       blanks = 4
       trunk = f'{" "*4}*'
    else:
       blanks = 2
       trunk = f'{" "*2}*'
    
    print("a spruce!")
    while rows <= branch_rows:
        print(f'{" "*blanks}{"*"*branches}')
        rows += 1
        blanks -=1
        branches +=2
    print(trunk)
if __name__ == "__main__":
    spruce(3)

