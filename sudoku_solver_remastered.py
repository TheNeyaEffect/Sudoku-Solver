# This program implements a Sudoku solver using a backtracking algorithm.
# Portions of the logic were inspired by the following tutorial:
# https://www.youtube.com/watch?v=jM80SmTQT1k
# Adapted and commented by Aneya Ward to demonstrate understanding of each section



NUMBERS = 9  # Constant for a standard 9x9 Sudoku board

# Initial Sudoku board (0 represents an empty space)
sudoku = [
    [8,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0],
    [6,0,0,0,0,0,0,0,0],
    [7,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0]
]

def valid_placement(board: list, num: int, pos: tuple):
    """
    Checks whether a number can be legally placed in a given position
    based on Sudoku rules (row, column, and 3x3 subgrid).
    """
    row_pos, col_pos = pos

    # Check that the number does not already exist in the row
    for col in range(NUMBERS):
        if board[row_pos][col] == num:
            return False

    # Check that the number does not already exist in the column
    for row in range(NUMBERS):
        if board[row][col_pos] == num:
            return False

    # Determine the top-left corner of the 3x3 subgrid
    box_x = (row_pos // 3) * 3
    box_y = (col_pos // 3) * 3

    # Check that the number does not already exist in the 3x3 subgrid
    for row in range(box_x, box_x + 3):
        for col in range(box_y, box_y + 3):
            if board[row][col] == num:
                return False

    # If all checks pass, the placement is valid
    return True

def next_empty_space(board: list):
    """
    Finds the next empty cell (represented by 0) on the board.
    Returns the row and column index of that cell, or None if the board is full.
    """
    for row in range(NUMBERS):
        for col in range(NUMBERS):
            if board[row][col] == 0:
                return row, col
    return None

def solve(sudoku: list):
    """
    Solves the Sudoku puzzle using a recursive backtracking algorithm.
    """
    # Find the next empty space to fill
    find = next_empty_space(sudoku)

    # If no empty space is found, the board is solved
    if not find:
        return True

    row, col = find

    # Try numbers 1 through 9 in the empty space
    for num in range(1, 10):
        if valid_placement(sudoku, num, (row, col)):
            sudoku[row][col] = num  # Place the number temporarily

            # Recursively attempt to solve the rest of the board
            if solve(sudoku):
                return True

            # If the placement leads to no solution, reset the cell (backtrack)
            sudoku[row][col] = 0

    # Trigger backtracking if no valid number can be placed
    return False

def print_board(board: list):
    """
    Prints the Sudoku board in a readable 9x9 grid format,
    separating 3x3 subgrids with lines.
    """
    for row in range(NUMBERS):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")

        for col in range(NUMBERS):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")

            if col != 8:
                print(board[row][col], end=" ")
            else:
                print(board[row][col])

# Display the original board
print("Original Board:\n")
print_board(sudoku)

# Solve the Sudoku puzzle
solve(sudoku)

# Display the solved board
(print("\nHere's your solved sudoku board:\n"))
print_board(sudoku)

(print("\nThis will be marked as my first ever coding individual project (as of January 7th, 2025) so I hope you enjoyed using it!\n"))
