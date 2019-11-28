def get_max_path(board):
    LENGHT = len(board)
    cache = [[-1 for _ in range(LENGHT)] for _ in range(LENGHT)]
    deltas = [(1, 0), (1, 1)]

    def max_path(r, c):
        if cache[r][c] != -1:
            return cache[r][c]

        if r == LENGHT - 1:
            return board[r][c]

        max_sum = 0
        for dr, dc in deltas:
            nr = dr + r
            nc = dc + c
            max_sum = max(max_sum, max_path(nr, nc))

        cache[r][c] = board[r][c] + max_sum
        return cache[r][c]

    return max_path(0, 0)


C = int(input())

for _ in range(C):
    board = []
    LENGHT = int(input())
    for _ in range(LENGHT):
        board.append(tuple(map(int, input().split())))

    print(get_max_path(board))
