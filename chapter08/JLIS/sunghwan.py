"""Get joined LIS from 2 number arrays

url: https://algospot.com/judge/problem/read/JLIS
ID : JLIS
"""
import sys

input = sys.stdin.readline


def jlis(arr1, arr2):
    N1, N2 = len(arr1), len(arr2)
    NEG_INF = float('-inf')
    cache = [[-1] * (N2+1) for _ in range(N1+1)]

    def find(i1, i2):
        if cache[i1+1][i2+1] != -1:
            return cache[i1+1][i2+1]

        a = NEG_INF if i1 == -1 else arr1[i1]
        b = NEG_INF if i2 == -1 else arr2[i2]
        max_value = max(a, b)

        ret = 0
        for nxt in range(i1+1, N1):
            if max_value < arr1[nxt]:
                ret = max(ret, find(nxt, i2) + 1)

        for nxt in range(i2+1, N2):
            if max_value < arr2[nxt]:
                print(max_value, arr2[nxt])
                ret = max(ret, find(i1, nxt) + 1)

        cache[i1+1][i2+1] = ret
        return ret

    return find(-1, -1)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        input()
        arr1 = [int(n) for n in input().split()]
        arr2 = [int(n) for n in input().split()]
        ans.append(jlis(arr1, arr2))

    for n in ans:
        print(n)
