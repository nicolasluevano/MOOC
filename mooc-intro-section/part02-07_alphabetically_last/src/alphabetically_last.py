# Write your solution here
first = input("Please type in the 1st word:")
second = input("Please type in the 2nd word:")

msg = " comes alphabetically last"

if first == second:
    print("You gave the same word twice")
elif first > second:
    print(f"{first}{msg}")
elif first < second:
    print(f"{second}{msg}")
