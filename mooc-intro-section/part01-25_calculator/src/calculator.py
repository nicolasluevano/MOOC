# Write your solution here
one = int(input("Number 1:"))
two = int(input("Number 2:"))
operation = input("Operation:")

add = one + two
multiply = one * two
subtract = one - two

if operation is 'add':
    print(f'{one} + {two} = {add}')
if operation is 'subtract':
    print(f'{one} - {two} = {subtract}')
if operation is 'multiply':
    print(f'{one} * {two} = {multiply}')