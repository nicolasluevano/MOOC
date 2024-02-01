# write your solution here
def read_fruits():
    dict = {}
    with open("src/fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            dict[parts[0]] = float(parts[-1])
    return dict

if __name__ == "__main__":
    print(read_fruits())

