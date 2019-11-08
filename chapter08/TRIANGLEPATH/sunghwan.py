"""Get smallest sum of numbers in pathes from top to bottom

:input:
2
5
6
1  2
3  7  4
9  4  1  7
2  7  5  9  4
5
1
2 4
8 16 8
32 64 32 64
128 256 128 256 128

:return:
28
341

url: https://algospot.com/judge/problem/read/TRIANGLEPATH
ID : TRIANGLEPATH
"""
def triangle_path(board):
    NEGA_INF = float('-inf')
    N = len(board)
    cache = [[-1] * n for n in range(1, N+1)]

    def least_cost(r, c):
        if r == 0 and c == 0:
            return board[r][c]
        elif c > r or r < 0 or c < 0:
            return NEGA_INF

        if cache[r][c] != -1:
            return cache[r][c]

        cache[r][c] = board[r][c] + max(least_cost(r-1, c), least_cost(r-1, c-1))
        return cache[r][c]

    return max(least_cost(N-1, c) for c in range(N))


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N = int(input())
        board = []
        for _ in range(N):
            board.append([int(n) for n in input().split()])
        ans.append(triangle_path(board))

    for n in ans:
        print(n)
