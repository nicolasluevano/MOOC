# Write your solution here
name = input("Please type in your name:")

mm = "I think you might be one of Mickey Mouse's nephews."
dd = "I think you might be one of Donald Duck's nephews."
no = "You're not a nephew of any character I know of."

if name == "Huey" or name == "Dewey" or name == "Louie":
    print(dd)
elif name == "Morty" or name == "Ferdie":
    print(mm)
else:
    print("You're not a nephew of any character I know of.")

