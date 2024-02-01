# Write your solution here

items = int(input("How many items:"))
item_count = 1
list = []

while items > 0:
    list.append(int(input(f'Item{item_count}:')))
    items -= 1
    item_count += 1
print(list)