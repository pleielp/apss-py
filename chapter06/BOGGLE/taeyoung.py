def has_word(x, y, word):
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for direction in range(8):
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if has_word(next_x, next_y, word[1:]):
            return True
    return False

def search_word(word):
    for x in range(5):
        for y in range(5):
            if has_word(x, y, word):
                return True
    return False


case_num = int(input())
for _ in range(case_num):
    board = list()
    for _ in range(5):
        board.append(input())
    words_num = int(input())
    words = list()
    for _ in range(words_num):
        words.append(input())

    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)

    for _ in range(case_num):
        for word in words:
            print(word, 'YES' if search_word(word) else 'NO')
