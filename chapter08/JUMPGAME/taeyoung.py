def solve(row, column):
    if row >= board_size or column >= board_size:
        return 0
    elif row == board_size - 1 and column == board_size - 1:
        return 1

    ret = cache[row][column]

    if ret != -1:
        return ret

    jump_size = board[row][column]

    cache[row][column] = solve(row + jump_size, column) or solve(row, column + jump_size)

    return cache[row][column]


case_num = int(input())
for _ in range(case_num):
    board_size = int(input())
    board = tuple(tuple(map(int, input().strip().split())) for _ in range(board_size))

    cache = [[-1] * board_size for _ in range(board_size)]

    print('YES' if solve(0, 0) else 'NO')