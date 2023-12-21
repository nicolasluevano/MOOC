# Write your solution here
def row_correct(sudoku: list):
    for row in sudoku:
        result = True
        checker = []
        for num in row:
            if num not in checker:
                checker.append(num)
                result = True
            elif num != 0 and num in checker:
                result = False
                return result
    return result

def column_correct(sudoku: list, column_no: int):
    column_check = []
    for column in sudoku:
        if column[column_no] > 0 and column[column_no] not in column_check:
            column_check.append(column[column_no])
        elif column[column_no] in column_check:
            return False
    print(column_check)
    return True

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


def sudoku_grid_correct(sudoku:list):
    row_no = len(sudoku)
    column_no = len(sudoku[0])

    for i in sudoku:
        row_correct(sudoku, i)



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

sudoku_grid_correct(sudoku)