def rotate(block):
    ROWS = len(block)
    COLS = len(block[0])
    new_block = [[None for _ in range(ROWS)] for _ in range(COLS)]
    for r in range(ROWS):
        for c in range(COLS):
            new_block[c][ROWS - r - 1] = block[r][c]
    return new_block


def solution(board, origin_block):
    # preprocess
    rotations = []

    def generateRotations(block):
        for i in range(4):
            rotation = []
            origin_x, origin_y = -1, -1
            for i in range(len(block)):
                for j in range(len(block[0])):
                    if block[i][j] == "#":
                        if origin_y == -1:
                            origin_x = i
                            origin_y = j
                        rotation.append((i - origin_x, j - origin_y))
            rotations.append(tuple(sorted(rotation)))
            block = rotate(block)

    # remove duplicate
    generateRotations(origin_block)
    block_size = len(rotations[0])
    rotations = list(set(rotations))
    boardHeight, boardWidth = len(board), len(board[0])

    covered = [
        [1 if board[r][c] == "#" else 0 for c in range(boardWidth)]
        for r in range(boardHeight)
    ]

    def set_block(r, c, block, delta):

        for dr, dc in block:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < boardHeight and 0 <= nc < boardWidth):
                return False

            if covered[nr][nc] == delta:
                return False

        for dr, dc in block:
            nr, nc = r + dr, c + dc
            covered[nr][nc] = 1 if delta == 1 else 0
        return True

    best = 0
    emptys = 0

    for i in range(boardHeight):
        for j in range(boardWidth):
            if covered[i][j] == 0:
                emptys += 1

    def search(placed):
        nonlocal best, emptys

        if best - placed >= emptys // block_size:
            return

        r, c = -1, -1
        for i in range(boardHeight):
            for j in range(boardWidth):
                if covered[i][j] == 0:
                    r, c = i, j
                    break
            if r != -1:
                break

        if r == -1:
            best = max(best, placed)
            return

        for i in range(len(rotations)):
            if set_block(r, c, rotations[i], 1):
                emptys -= block_size
                search(placed + 1)
                set_block(r, c, rotations[i], -1)
                emptys += block_size

        covered[r][c] = 1
        emptys -= 1
        search(placed)
        covered[r][c] = 0
        emptys += 1

    search(0)
    return best


C = int(input())

for _ in range(C):
    board = []
    block = []
    H, W, R, C = map(int, input().split())

    for _ in range(H):
        line = list(input())
        board.append(line)

    for _ in range(R):
        line = list(input())
        block.append(line)

    print(solution(board, block))
