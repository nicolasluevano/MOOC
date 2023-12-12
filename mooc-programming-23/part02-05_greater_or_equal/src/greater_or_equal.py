# Write your solution here
num_one = int(input("Please type in the first number: "))
num_two = int(input("Please type in another number: "))
msg = "The greater number was: "

if num_one > num_two:
    print(f'{msg}{num_one}')
elif num_one < num_two:
    print(f'{msg}{num_two}')
else:
    print('The numbers are equal!')