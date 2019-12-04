"""Get minimum cost to concatenate all strings into single one

url: https://algospot.com/judge/problem/read/STRJOIN
ID : STRJOIN
"""
from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline


def min_cost_to_concatenate(lens): # time complexity: O(N log N), maybe
    heapify(lens)
    ans = 0

    while len(lens) >= 2:
        l1 = heappop(lens)
        l2 = heappop(lens)
        ans += (l1 + l2)
        heappush(lens, l1 + l2)

    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        input()
        str_lens = [int(n) for n in input().split()]
        ans.append(min_cost_to_concatenate(str_lens))

    for cost in ans:
        print(cost)
