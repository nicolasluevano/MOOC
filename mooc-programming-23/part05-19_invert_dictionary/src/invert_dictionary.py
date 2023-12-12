# Write your solution here
def invert(dictionary: dict):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[value] = key

if __name__ == '__main__':
    s = {1: 10, 2: 20, 3: 30}
    s = invert(s)
    print(s)