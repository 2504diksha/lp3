
def print_board(board, n):
    print("\nFinal N-Queens matrix:")#
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else "X", end=" ")
        print()

# Function to check if placing a queen is safe
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function to solve N-Queens
def solve_nqueens(board, row, n):
    if row == n:
        return True  # solution found
# Try placing queen in all columns of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack

    return False


# ---- Main Program ----
n = int(input("Enter the number of queens (N): "))

board = [[0 for _ in range(n)] for _ in range(n)]

# Place first queen manually
first_col = int(input("Enter column position (1 to N) to place the first Queen: ")) - 1
board[0][first_col] = 1

if solve_nqueens(board, 1, n):
    print_board(board, n)
else:
    print("No valid solution exists for this configuration.")