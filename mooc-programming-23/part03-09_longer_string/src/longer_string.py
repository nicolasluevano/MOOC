# Write your solution here
first = input("Please type in a string 1:")
second = input("Please type in a string 2:")

if len(first) == len(second):
    print("The strings are equally long")
elif len(first) > len(second):
    print(f'{first} is longer')
else:
    print(f'{second} is longer')