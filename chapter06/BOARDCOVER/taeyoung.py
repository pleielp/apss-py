from pprint import pprint

def setting(board, row, column, cover_type, behavior):
    ok = True
    for type_idx in cover_type:
        new_row = row + type_idx[0]
        new_column = column + type_idx[1]
        if not (-1 < new_row < len(board)) or not (-1 < new_column < len(board[0])):
            ok = False
        elif board[new_row][new_column] == '#':
            ok = False

    for type_idx in cover_type:
        new_row = row + type_idx[0]
        new_column = column + type_idx[1]
        if behavior == 'set' and ok == True:
            board[new_row][new_column] = '#'
        if behavior == 'unset':
            board[new_row][new_column] = '.'

    return ok


def cover(board, level=1):
    y = -1
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == '.':
                y = column
                break
        if y != -1:
            break
    if y == -1:
        return 1
    ret = 0
    for cover_type in COVER_TYPES:
        if setting(board, row, column, cover_type, 'set'):
            ret += cover(board, level=level+1)
            setting(board, row, column, cover_type, 'unset')
    return ret
                    

COVER_TYPES = (((0, 0), (0, 1), (1, 0)),
               ((0, 0), (0, 1), (1, 1)),
               ((0, 0), (1, 0), (1, 1)),
               ((0, 0), (1, 0), (1, -1)))

case_num = int(input())
for _ in range(case_num):
    height, width = map(int, input().split())
    board = [list(input().strip()) for _ in range(height)]

    blank_num = sum([board_row.count('.') for board_row in board])
    if blank_num % 3 != 0:
        print(0)
        continue

    # pprint(board)
    print(cover(board))