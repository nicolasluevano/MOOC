# Write your solution here

def get_sum(element: list):
    result = sum(element)
    return result

def row_sums(my_matrix: list):
    # add the values of the two elements in each list
    # append the sum to the end of each list
    # no return
    for element in my_matrix:
        summed = get_sum(element)
        element.append(summed)


if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
