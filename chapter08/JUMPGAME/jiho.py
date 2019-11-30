def solution(board, size):
    cache = [[-1 for _ in range(size)]for _ in range(size)]
    deltas = [(1, 0), (0, 1)]

    def is_access(r, c):
        if r == size-1 and c == size-1:
            return True

        if cache[r][c] != -1:
            return cache[r][c]

        jump = board[r][c]
        for dr, dc in deltas:
            nr, nc = jump*dr + r, jump*dc + c
            if not (0 <= nr < size and 0 <= nc < size):
                continue

            if is_access(nr, nc):
                return True

        cache[r][c] = False
        return False

    if is_access(0, 0):
        return 'YES'
    else:
        return 'NO'


C = int(input())

for _ in range(C):
    size = int(input())
    board = []
    for _ in range(size):
        board.append(list(map(int, input().split())))
    print(solution(board, size))
