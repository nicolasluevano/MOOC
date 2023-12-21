# Write your solution here
import string

def separate_characters(my_string: str):
    characters = list(my_string)
    chars = ''
    punct = ''
    rest = ''
    for char in characters:
        if char in string.ascii_letters:
            chars += char
        if char in string.punctuation:
            punct += char
        if char.isascii() == False or char in string.whitespace:
            rest += char

    return chars, punct, rest



if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
