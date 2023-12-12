# Write your solution here
def shortest(ls):
    shortest = ls[0]
    for i in ls:
        if len(i) < len(shortest):
            shortest = i
    return shortest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)