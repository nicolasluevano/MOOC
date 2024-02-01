# Write your solution here

a = input("1st letter:")
b = input("2nd letter:")
c = input("3rd letter:")

if a <= b <= c or c <= b <= a:
    print(f"The letter in the middle is {b}")
elif b <= a <= c or c <= a <= b:
    print(f"The letter in the middle is {a}")
else:
    print(f"The letter in the middle is {c}")