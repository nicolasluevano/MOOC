# Write your solution here
name = input("Please tell me your name:")

msg = 'Next please!'


if name != 'Jerry':
    portions = int(input("How many portions of soup?"))
    total_cost = (5.90 * portions)
    print(f'The total cost is {total_cost}')
    print(msg)
print(msg)
    