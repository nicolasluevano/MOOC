# Write your solution here

#prompt user for inputs
def diary_entry():
    funct = 1
    while funct > 0:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        funct = int(input("Function:"))
        if funct == 1:
            entry = input("Diary entry:")
            with open("diary.txt", "a") as my_file:
                my_file.write(f"{entry}\n")
                print("Diary saved")
        if funct == 2:
            with open("diary.txt") as my_file:
                for line in my_file:
                    print(line)
        if funct == 0:
            print("Bye now!")
            break

diary_entry()




