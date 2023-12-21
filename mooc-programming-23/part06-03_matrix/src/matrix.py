# write your solution here
def matrix_data():
    with open("src/matrix.txt") as new_file:
        data = []
        for line in new_file:
            line = line.replace("\n", "").split(",")
            int_line = []
            for item in line:
                int_line.append(int(item))
            data.append(int_line)
    return data


def matrix_sum():
    data = matrix_data()
    line_sum = 0
    for line in data:
        for i in line:
            line_sum += i
    return line_sum

def matrix_max():
    data = matrix_data()
    highest_num = 0
    for line in data:
        for i in line:
            if i > highest_num:
                highest_num = i
    return highest_num

def row_sums():
    data = matrix_data()
    sums = []
    for line in data:
        total = 0
        for i in line:
            total += i
        sums.append(total)
    return sums




