"""

:input:
3 
3 7 
#.....# 
#.....# 
##...## 
3 7 
#.....# 
#.....# 
##..### 
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 

:return:
0
2
1514
"""
def ways_to_cover(board):
    R, C = len(board), len(board[0])
    BLACK, WHITE = '#.'
    BLOCK_TYPES = (
        ((0, 0), (0, 1), (1, 1)),
        ((0, 0), (1, 0), (1, 1)),
        ((0, 0), (1, 0), (1, -1)),
        ((0, 0), (1, 0), (0, 1))
    )

    def is_in_range(r, c):
        return 0 <= r < R and 0 <= c < C

    def can_i_put_this_here(r, c, btype):
        block = BLOCK_TYPES[btype]

        for dr, dc in block:
            new_r, new_c = r + dr, c + dc
            if not is_in_range(new_r, new_c) or board[new_r][new_c] == BLACK:
                return False
        return True

    def set_block(r, c, btype, value):
        block = BLOCK_TYPES[btype]
        for dr, dc in block:
            new_r, new_c = r + dr, c + dc
            board[new_r][new_c] = value

    def cover_board(blocks_left):
        if blocks_left == 0:
            return 1

        ret = 0

        for r in range(R):
            for c in range(C):
                chosen = False
                if board[r][c] == WHITE:
                    chosen = True
                    break
            if chosen:
                break

        for d in range(len(BLOCK_TYPES)):
            if can_i_put_this_here(r, c, d):
                set_block(r, c, d, BLACK)
                ret += cover_board(blocks_left-1)
                set_block(r, c, d, WHITE)

        return ret


    white_cells = sum(board[r][c] == WHITE for r in range(R) for c in range(C))
    if white_cells % 3 != 0:
        return 0

    blocks_left = white_cells // 3
    return cover_board(blocks_left)



if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        R, _ = (int(n) for n in input().split())
        board = []
        for _ in range(R):
            board.append(list(input().strip()))
        print(ways_to_cover(board))
