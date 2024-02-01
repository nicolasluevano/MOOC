# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    fractions = []
    result = Fraction(1, amount)
    for x in range(amount):
        fractions.append(result)
    return fractions


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))
