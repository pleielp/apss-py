"""Maximize our win counts against russian code pros

url: https://algospot.com/judge/problem/read/MATCHORDER
ID : MATCHORDER
"""
import sys

input = sys.stdin.readline


def maximum_wins(russians, our_ratings):
    R, K = len(russians), len(our_ratings)
    r = k = 0
    ret = 0

    russians.sort()
    our_ratings.sort()

    while r < R and k < K:
        if russians[r] <= our_ratings[k]:
            ret += 1
            r += 1
        k += 1

    return ret


if __name__ == '__main__':
    C = int(input().strip())
    ans = []

    for _ in range(C):
        input()
        russians = [int(n) for n in input().strip().split()]
        ours = [int(n) for n in input().strip().split()]
        ans.append(maximum_wins(russians, ours))

    for n in ans:
        print(n)
