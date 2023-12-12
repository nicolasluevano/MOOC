# Write your solution here
while True:
    response = input("Editor:")
    editor = response.lower()
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")