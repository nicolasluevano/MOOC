# Write your solution here
#asks user for number
# if less than zero, print number muiltiple by -1
# else print as it

nummy = int(input("Please type in a number:"))

if nummy < 0:
    print(f'The absolute value of this number is {nummy * -1}')
else: 
    print(f'The absolute value of this number is {nummy}')