def preprocess(block):
    new_block = list()
    original_y = -1
    for r in range(len(block)):
        for c in range(len(block[0])):
            if block[r][c] == '#':
                if original_y == -1:
                    original_y, original_x = r, c
                new_block.append((r - original_y, c - original_x))
    return tuple(new_block)


def generate_rotations(block):
    blocks = set()
    blocks.add(preprocess(block))
    for _ in range(3):
        block = list(zip(*block[::-1]))
        blocks.add(preprocess(block))
    return blocks


def search(placed):
    global best

    blank_num = sum((row.count(0) for row in covered))
    if best - placed >= blank_num // block_real_size:
        return

    y, x = -1, -1
    for r in range(len(board)):
        for c in range(len(board[0])):
            if covered[r][c] == 0:
                y, x = r, c
                break
        if y != -1:
            break
    
    if y == -1:
        best = max(best, placed)
        return

    for rotation in rotations:
        if set_block(y, x, rotation, 1):
            search(placed + 1)
        set_block(y, x, rotation, -1)

    covered[y][x] = 1
    search(placed)
    covered[y][x] = 0

    return best

def set_block(y, x, rotation, delta):
    enable = True

    for dy, dx in rotation:
        new_y = y + dy
        new_x = x + dx

        if -1 < new_y < len(board) and -1 < new_x < len(board[0]):
            covered[new_y][new_x] += delta
            if covered[new_y][new_x] > 1:
                enable = False
        else:
            enable = False

    return enable


HEIGHT, WIDTH = 0, 1

case_num = int(input())
for _ in range(case_num):
    input_temp = tuple(map(int, input().strip().split()))
    board_size, block_size = input_temp[:2], input_temp[2:]
    board = [list(input()) for _ in range(board_size[HEIGHT])]
    block = [list(input()) for _ in range(block_size[HEIGHT])]
    block_real_size = sum((row.count('#') for row in block))
    covered = [[1 if column == '#' else 0 for column in row] for row in board]

    rotations = generate_rotations(block)

    best = 0
    best = search(0)
    print(best)
