def is_safe(board, row, col, n):
    # Check same column
    for r in range(n):
        if board[r][col] == 1:
            return False

    # Check all four diagonal directions
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < n and 0 <= c < n:
            if board[r][c] == 1:
                return False
            r += dr
            c += dc

    return True


def solve(board, row, n, fixed_row):
    if row == n:
        return True

    # skip the fixed-row (it already has a queen placed)
    if row == fixed_row:
        return solve(board, row + 1, n, fixed_row)

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row + 1, n, fixed_row):
                return True
            board[row][col] = 0

    return False


# -----------------------
# USER INPUT
# -----------------------
n = int(input("Enter number of queens (n): "))
fr = int(input("Enter first queen row (0 to n-1): "))
fc = int(input("Enter first queen column (0 to n-1): "))

board = [[0] * n for _ in range(n)]
board[fr][fc] = 1  # place the fixed queen

if solve(board, 0, n, fr):
    print("\nFinal N-Queens Board:")
    for r in board:
        print(" ".join("Q" if x == 1 else "." for x in r))
else:
    print("No solution exists with the first queen fixed there.")
