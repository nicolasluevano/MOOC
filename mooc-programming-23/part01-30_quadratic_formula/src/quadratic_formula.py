# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt
import cmath
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(f'The roots are {sol1} and {sol2}')

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5