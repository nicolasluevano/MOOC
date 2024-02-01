# Write your solution here
list = []
num = 1
print(f'The list is now {list}')
while True:
    decision = input("a(d)d, (r)emove or e(x)it:")
    if  decision != "x":
        if decision == "d":
            list.append(num)
            num +=1
        if decision == "r":
            list.pop(-1)
            num -=1
        print(f'The list is now {list}')
    else:
        print("Bye!")
        break
