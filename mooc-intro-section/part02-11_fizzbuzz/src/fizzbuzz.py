# Write your solution here
nummy = int(input("Number:"))

if nummy % 3 == 0 and nummy % 5 == 0:
    print("FizzBuzz")
elif nummy % 3 == 0:
    print("Fizz")
elif nummy % 5 == 0:
    print("Buzz")