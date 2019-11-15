"""Get least difficulties to memoize pi prefixes

url: https://algospot.com/judge/problem/read/PI
ID : PI
"""
import sys

sys.setrecursionlimit(10 ** 4)

MIN_LEN, MAX_LEN = 3, 5
INF = float('inf')


def judge(pi, lo, hi):
    if not MIN_LEN <= hi - lo + 1 <= MAX_LEN:
        return INF
    delta = ord(pi[lo+1]) - ord(pi[lo])

    if all(pi[lo] == pi[lo+d] for d in range(hi-lo+1)):
        return 1
    elif all( (ord(pi[i]) - ord(pi[i-1])) == delta for i in range(lo+1, hi+1) ) \
       and (delta == 1 or delta == -1):
        return 2
    elif all( (ord(pi[i]) - ord(pi[i-1])) == delta for i in range(lo+1, hi+1) ):
        return 5
    else:
        i = lo
        d = 2
        while i + d <= hi:
            if pi[lo+d] != pi[lo]:
                return 10
            d += 2

        d = 2
        while i + 1 + d <= hi:
            if pi[lo+1+d] != pi[lo+1]:
                return 10
            d += 2

        return 4


def calculate_difficulty(pi):
    P = len(pi)
    cache = [-1] * P

    def until_i(i):
        if i < 0:
            return 0
        elif i < MIN_LEN - 1:
            return INF
        elif cache[i] != -1:
            return cache[i]

        ret = INF
        for d in range(MIN_LEN, min(MAX_LEN, i+1) + 1):
            ret = min(ret, until_i(i-d) + judge(pi, i-d+1, i))
        cache[i] = ret

        return ret

    return until_i(P-1)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        ans.append(calculate_difficulty(input().strip()))

    for n in ans:
        print(n)
