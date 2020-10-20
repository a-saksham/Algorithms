# Qs 2nd - SUDOKU SOLVER


# Print Sudoku Board
def print_board(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end= ' ')
        print('')


# Finding empty location
def find_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


# Check row for same values
def row_check(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


# Check column for same values
def col_check(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# Check box conditions
def box_check(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False


# Call for all Checks
def check_location_is_safe(arr, row, col, num):
    return not row_check(arr, row, num) and \
           not col_check(arr, col, num) and \
           not box_check(arr, row - row % 3, col - col % 3, num)


# Main Function
def solve_sudoku(arr):
    l = [0, 0]

    if not find_location(arr, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if check_location_is_safe(arr, row, col, num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True

        # Backtrack count
        global bt_count
        bt_count+=1
        arr[row][col] = 0   # BACKTRACK

    return False


# DRIVER CODE
bt_count = 0
board = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
        [2, 8, 9, 0, 0, 4, 0, 0, 0],
        [3, 4, 6, 2, 0, 5, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 3, 8, 0, 0, 6, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 7, 8],
        [7, 0, 3, 4, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

print('\nProblem Sudoku Board:: ')
print_board(board)

print('\nSolved - Sudoku Board::')
if solve_sudoku(board):
    print_board(board)
else:
    print("Solution does not exist for the given problem")

print('\nTotal Backtrack Count =',bt_count)
