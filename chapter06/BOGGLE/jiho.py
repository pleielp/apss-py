def has_word(board, r, c, word):
    delta = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1)
    ]

    stack = [(r, c, word)]
    while stack:
        r, c, word = stack.pop()
        if board[r][c] != word[0]:
            continue

        if len(word) == 1:
            return True

        for dr, dc in delta:
            nr, nc = dr+r, dc+c
            if 0 <= nr < 5 and 0 <= nc < 5:
                stack.append((nr, nc, word[1:]))
    return False


C = int(input())
for _ in range(C):
    board = [input() for _ in range(5)]
    keywords_count = int(input())
    keywords = [input() for _ in range(keywords_count)]
    all_point = [(r, c) for r in range(5) for c in range(5)]
    for keyword in keywords:
        print("{}".format(keyword), end=" ")
        has_flag = False
        for r, c in all_point:
            if has_word(board, r, c, keyword):
                has_flag = True
                break
        if has_flag:
            print("YES")
        else:
            print("NO")
