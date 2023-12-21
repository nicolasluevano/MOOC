# Write your solution here
# def row_correct(sudoku: list):
#     for row in sudoku:
#         result = True
#         checker = []
#         for num in row:
#             if num not in checker:
#                 checker.append(num)
#                 result = True
#             elif num != 0 and num in checker:
#                 result = False
#                 return result
#     return result

def column_correct(sudoku: list):
    # get the first element from each list
    columns = len(sudoku[0])

    for col in range(columns):
        column_values = []
        for row in sudoku:
            column_values.append(row[col])
        





if __name__ == "__main__":
    # sudoku = [
    #   [9, 0, 0, 0, 8, 0, 3, 0, 0],
    #   [2, 0, 0, 2, 5, 0, 7, 0, 0],
    #   [0, 2, 0, 3, 0, 0, 0, 0, 4],
    #   [2, 9, 4, 0, 0, 0, 0, 0, 0],
    #   [0, 0, 0, 7, 3, 0, 5, 6, 0],
    #   [7, 0, 5, 0, 6, 0, 4, 0, 0],
    #   [0, 0, 7, 8, 0, 3, 9, 0, 0],
    #   [0, 0, 1, 0, 0, 0, 0, 0, 3],
    #   [3, 0, 0, 0, 0, 0, 0, 0, 2]
    # ]

    sudoku = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 7, 0, 0, 3, 9, 0, 1]
    ]

    print(column_correct(sudoku))