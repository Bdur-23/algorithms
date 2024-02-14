def is_valid_move(puzzle, rw, cl, n):
    for i in range(9):
        if puzzle[rw][i] == n or puzzle[i][cl] == n:
            return False

    srw, scl = 3 * (rw // 3), 3 * (cl // 3)
    for i in range(3):
        for j in range(3):
            if puzzle[srw + i][scl + j] == n:
                return False

    return True

def solve(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve(puzzle):
                            return True
                        puzzle[row][col] = 0
                return False
    return True

def sudoku(puzzle):
    if not solve(puzzle):
        raise ValueError("Puzzle cannot be solved")
    return puzzle
