# Write your solution here
points = int(input("How many points [0-100]:"))

if points < 0 or points > 100:
    print("Grade: impossible!")
if 0 <= points <= 49:
    print("Grade: fail")
if 50 <= points <= 59:
    print("Grade: 1")
if 60 <= points <= 69:
    print("Grade: 2")
if 70 <= points <= 79:
    print("Grade: 3")
if 80 <= points <= 89:
    print("Grade: 4")
if 90 <= points <= 100:
    print("Grade: 5")
