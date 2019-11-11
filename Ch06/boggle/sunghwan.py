"""Boggle problem in exhaustive search

:input:
    1
    URLPM
    XPRET
    GIAET
    XTNZY
    XOQRS
    6
    PRETTY
    GIRL
    REPEAT
    KARA
    PANDORA
    GIAZAPX

:return:
    PRETTY YES
    GIRL YES
    REPEAT YES
    KARA NO
    PANDORA NO
    GIAZAPX YES

url : https://algospot.com/judge/problem/read/BOGGLE
"""
def has_word(board, word):
    N = len(board)
    DELTAS = {(r, c) for r in range(-1, 2) for c in range(-1, 2)} - {(0, 0)}
    YES_MSG, NO_MSG = 'YES', 'NO'
    ans = False

    def find(idx, r, c):
        # 현재 idx번 글자까지 찾았고,
        # 그 좌표가 (r, c)일 때
        # 다음 글자를 찾아보자
        nonlocal ans
        if ans:
            return
        if idx == len(word) - 1:
            ans = True
            return

        for dr, dc in DELTAS:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < N and 0 <= new_c < N \
               and board[new_r][new_c] == word[idx+1]:
                find(idx+1, new_r, new_c)


    for r in range(N):
        for c in range(N):
            if board[r][c] == word[0]:
                find(0, r, c)

    return YES_MSG if ans else NO_MSG


if __name__ == '__main__':
    board = [
          ["U", "R", "L", "P", "M"],
          ["X", "P", "R", "E", "T"],
          ["G", "I", "A", "E", "T"],
          ["X", "T", "N", "Z", "Y"],
          ["X", "O", "Q", "R", "S"],
    ]
    words_to_find = ['PRETTY', 'GIRL', 'REPEAT', 'KARA', 'PANDORA', 'GIAZAPX']

    for word in words_to_find:
        print(word, has_word(board, word))
