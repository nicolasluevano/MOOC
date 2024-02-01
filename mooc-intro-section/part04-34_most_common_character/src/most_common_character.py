# Write your solution here
def most_common_character(str):
    count = 0
    most = ''
    for i in str:
        if str.count(i) > count:
            count = str.count(i)
            most = i
    return most


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))