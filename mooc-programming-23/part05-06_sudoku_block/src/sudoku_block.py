# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    which_row = row_no
    checker = []
    for row in sudoku[which_row]:
        while which_row < (row_no + 3):
            set = sudoku[which_row]
            which_row += 1
            result = set[column_no:(column_no + 3)]
            for i in result:
                checker.append(i)
    checked = []
    for i in checker:
        if i > 0 and i not in checked:
            checked.append(i)
        elif i in checked:
            return False
    return True








if __name__ == "__main__":

    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))