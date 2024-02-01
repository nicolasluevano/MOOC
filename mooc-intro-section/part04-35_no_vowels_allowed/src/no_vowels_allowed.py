# Write your solution here

def no_vowels(my_string):
    new_string = ''
    vowels = 'aeiou'
    for i in my_string:
        if i not in vowels:
            new_string += i

    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))