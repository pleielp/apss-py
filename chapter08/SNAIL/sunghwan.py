"""Get possibility of snail to get ouf ot well

url: https://algospot.com/judge/problem/read/SNAIL
ID : SNAIL
"""
import sys

sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline


def get_possibility(N, M, p):
    cache = [[-1] * N for _ in range(M)]

    def move_on(days, dist):
        if dist >= N:
            return 1
        elif days == M:
            return 0

        if cache[days][dist] != -1:
            return cache[days][dist]

        ret = p * move_on(days+1, dist+2) + (1 - p) * move_on(days+1, dist+1)
        cache[days][dist] = ret
        return ret

    if N <= M:
        return 1
    else:
        return move_on(0, 0)


if __name__ == "__main__":
    C = int(input())
    ans = []

    for _ in range(C):
        N, M = (int(n) for n in input().strip().split())
        ans.append(get_possibility(N, M, 0.75))

    for p in ans:
        print(p)
