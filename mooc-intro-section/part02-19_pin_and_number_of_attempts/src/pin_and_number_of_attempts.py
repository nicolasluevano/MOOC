# Write your solution here

attemps = 0

while True:
    pin = int(input("PIN:"))
    attemps += 1

    if pin == 4321 and attemps == 1:
        print("Correct! It only took you one single attempt!")
        success = True
        break
    if pin == 4321:
        print(f'Correct! It took you {attemps} attempts')
        break
    print("Wrong")
    


    