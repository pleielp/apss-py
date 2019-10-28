

def boardcover(board):
    fragements = [
        [(0, 0), (1, 0), (1, -1)],
        [(0, 0), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (0, 1), (1, 0)],
    ]
    row_n = len(board)
    col_n = len(board[0])

    def get_free():
        for r in range(row_n):
            for c in range(col_n):
                if board[r][c] == '.':
                    return (r, c)
        return None

    def is_cover(r: int, c: int, f: int):
        for dr, dc in fragements[f]:
            nr, nc = dr + r, dc + c
            if not (0 <= nr < row_n and 0 <= nc < col_n):
                return False
            if board[nr][nc] == '#':
                return False

        return True

    def set_cover(r: int, c: int, f: int, char):
        for dr, dc in fragements[f]:
            nr, nc = dr + r, dc + c
            board[nr][nc] = char

    def cover():
        pos = get_free()
        if pos is None:
            return 1
        r, c = pos
        ret = 0
        for f in range(len(fragements)):
            if is_cover(r, c, f):
                set_cover(r, c, f, '#')
                ret += cover()
                set_cover(r, c, f, '.')
        return ret

    return cover()


C = int(input())
for _ in range(C):
    row, col = tuple(map(int, input().split()))

    board = [[c for c in input()] for _ in range(row)]
    # print(board)
    print(boardcover(board))
