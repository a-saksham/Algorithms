# Qs 1st - N_QUEEN PROBLEM


# Printing the board
def printBoard(board):
    global k
    print('Case {}:'.format(k))
    k = k + 1
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("")
    print("")


# Checking whether place of queen is valid or not
def Check(board, row, col):

    # ROW-COL Check
    for i in range(col):
        if board[row][i] == 1:
            return False

    # DIAGONAL Check
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# N Queen Utility - places all queens, backtracks if needed
def nq_solve(board, col):
    if (col == N):
        printBoard(board)
        global bt_count
        bt_count += 1
        print(bt_count)
        return True

    res = False
    for i in range(N):
        if (Check(board, i, col)):
            board[i][col] = 1
            res = nq_solve(board, col + 1) or res

            # Backtrack count
            # global bt_count
            # bt_count += 1
            board[i][col] = 0   # BACKTRACK

    return res


# DRIVER CODE
print('')
N = int(input("Enter value of N:: "))
k = 1
bt_count = 0
board = [[0 for x in range(N)] for y in range(N)]

if nq_solve(board, 0) == False:
    print("Solution for the given problem does not exist")

print('Total Backtrack Count =',bt_count)
