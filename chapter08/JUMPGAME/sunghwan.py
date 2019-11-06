"""Return if I can reach the right bottom side of the board

:input:
2
7
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 2
3 3 1 2 3 4 1
1 5 2 9 4 7 0
7
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 2
4 1 2 3 4 1 3
3 3 1 2 3 4 1
1 5 2 9 4 7 0

:return:
YES
NO

url: https://algospot.com/judge/problem/read/JUMPGAME
ID : JUMPGAME
"""
def jumpgame(board):
    N = len(board)
    YES_MSG, NO_MSG = 'YES', 'NO'
    NOT_CHECKED = -1

    cache = [[NOT_CHECKED] * N for _ in range(N)]

    def can_reach(r, c):
        if r == 0 and c == 0:
            return True

        if cache[r][c] != NOT_CHECKED:
            return cache[r][c]

        ret = False
        for dr in range(1, r+1):
            if board[r-dr][c] == dr and can_reach(r-dr, c):
                ret = True
                break

        if not ret:
            for dc in range(1, c+1):
                if board[r][c-dc] == dc and can_reach(r, c-dc):
                    ret = True
                    break

        cache[r][c] = ret
        return ret

    return YES_MSG if can_reach(N-1, N-1) else NO_MSG


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N = int(input())
        board = [[int(n) for n in input().split()] for _ in range(N)]
        ans.append(jumpgame(board))

    for n in ans:
        print(n)
