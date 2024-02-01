# Write your solution here

word = input("Please type in a string")
count = len(word)

while count > 0:
    count -= 1
    if "a" in word:
        print('a found')
    else:
        print('a not found')
    if "e" in word:
        print('e found')
    else:
        print('e not found')
    if "o" in word:
        print('o found')
    else:
        print('o not found')
    break
