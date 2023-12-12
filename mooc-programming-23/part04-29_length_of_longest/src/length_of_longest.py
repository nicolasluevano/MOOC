# Write your solution here
def length_of_longest(ls):
    longest = 0
    for i in ls:
        if len(i) > longest:
            longest = len(i)
    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    new_list = length_of_longest(my_list)
    print(new_list)
   