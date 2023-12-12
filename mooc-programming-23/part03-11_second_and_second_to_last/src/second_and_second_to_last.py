# Write your solution here
wrd = input("Please type in a string:")

second_letter = wrd[1]
stl_letter = wrd[-2]

if second_letter != stl_letter:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {second_letter}")