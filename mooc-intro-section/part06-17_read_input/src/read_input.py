# Write your solution here
def read_input(prompt: str, num1: int, num2: int):
    while True:
        try:
            user_input = (input(f"{prompt}"))
            num = int(user_input)
            if num1 <= num <= num2:
                print(f"You typed in {num}")
                return num
        except ValueError:
            pass
        print(f"You must type in an integer between {num1} and {num2}")


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
