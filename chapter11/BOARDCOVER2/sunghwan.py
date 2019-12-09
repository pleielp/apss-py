"""Return how many blocks I can put in board now

url: https://algospot.com/judge/problem/read/BOARDCOVER2
ID : BOARDCOVER2
"""
SET, EMPTY = '#.'


def rotate(arr):
    ret = [[None] * len(arr) for _ in range(len(arr[0]))]

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            ret[c][len(arr)-1-r] = arr[r][c]
    return ret


def generate_rotations(block):
    rotations = [[] for _ in range(4)]

    for i in range(4):
        origin_r = origin_c = -1

        for r in range(len(block)):
            for c in range(len(block[0])):
                if block[r][c] == SET:
                    if origin_r == -1:
                        origin_r = r
                        origin_c = c

                    rotations[i].append((r - origin_r, c - origin_c))

        rotations[i].sort()
        block = rotate(block)

    rotations.sort()

    i = 0
    while i + 1 < len(rotations):
        if rotations[i] == rotations[i+1]:
            rotations.pop(i+1)
        else:
            i += 1

    return rotations


def max_blocks(board, block):
    R, C = len(board), len(board[0])
    rotations = generate_rotations(block)
    BLOCK_SIZE = len(rotations[0])
    best = -1

    empty_cells = sum(board[r][c] == EMPTY for r in range(R) for c in range(C))

    def set_block(start_r, start_c, block):
        for dr, dc in block:
            board[start_r+dr][start_c+dc] = SET

    def unset_block(start_r, start_c, block):
        for dr, dc in block:
            board[start_r+dr][start_c+dc] = EMPTY

    def is_in_range(r, c, block):
        return all(0 <= r + dr < R and 0 <= c + dc < C for dr, dc in block)

    def can_set_block(r, c, block):
        if not is_in_range(r, c, block):
            return False

        for dr, dc in block:
            if board[r+dr][c+dc] == SET:
                return False
        return True

    def search(placed, left_cells):
        nonlocal best

        if (left_cells // BLOCK_SIZE) + placed <= best:
            return

        start_r = start_c = -1

        for r in range(R):
            for c in range(C):
                if board[r][c] == EMPTY:
                    start_r, start_c = r, c
                    break
            if start_r != -1:
                break

        if start_r == -1:
            best = max(best, placed)
            return

        for block in rotations:
            if can_set_block(start_r, start_c, block):
                set_block(start_r, start_c, block)
                search(placed+1, left_cells - BLOCK_SIZE)
                unset_block(start_r, start_c, block)

        board[start_r][start_c] = SET
        search(placed, left_cells-1)
        board[start_r][start_c] = EMPTY

    search(0, empty_cells)
    return best


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        H, _, BH, __ = (int(n) for n in input().split())
        board = []
        block = []
        for _ in range(H):
            board.append(list(input()))

        for _ in range(BH):
            block.append(list(input()))

        ans.append(max_blocks(board, block))

    for n in ans:
        print(n)
