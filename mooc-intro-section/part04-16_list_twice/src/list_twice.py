# Write your solution here
list_now = []
while True:
    item = int(input("New Item:"))
    if item == 0:
        print("Bye!")
        break
    list_now.append(item)
    print(f'The list now: {list_now}')
    in_order = sorted(list_now)
    print(f'The list in order: {in_order}')