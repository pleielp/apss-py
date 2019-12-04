def solve(row, column):
    if row >= board_size or column >= board_size:
        return False
    elif row == board_size - 1 and column == board_size - 1:
        return True

    return solve(row + board[row][column], column) or solve(row, column + board[row][column])


case_num = int(input())
for _ in range(case_num):
    board_size = int(input())
    board = tuple(tuple(map(int, input().strip().split())) for _ in range(board_size))

    print(solve(0, 0))