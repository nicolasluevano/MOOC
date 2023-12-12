# Write your solution here
print('Person 1:')
name_one = input("Name:")
age_one = int(input("Age:"))
print('Person 2:')
name_two = input("Name:")
age_two = int(input("Age:"))
elder_msg = "The elder is "
same_msg = f'{name_one} and {name_two} are the same age'

if age_one > age_two:
    print(f'{elder_msg}{name_one}')
elif age_two > age_one:
    print(f'{elder_msg}{name_two}')
else:
    print(same_msg)