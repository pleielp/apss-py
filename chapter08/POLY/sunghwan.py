"""Get number of monotone polynomios of N squares

url: https://algospot.com/judge/problem/read/POLY
ID : POLY
"""
MOD = int(1e7)
MAX_SIZE = 100
CACHE = [[-1] * (MAX_SIZE + 1) for _ in range(MAX_SIZE+1)]


def generate(N, last):  # 총 N개를 쓰는데 마지막은 last를 쓴 경우
    global CACHE

    if N < last:
        return 0
    elif N == last:
        return 1
    elif CACHE[N][last] != -1:
        return CACHE[N][last]

    ret = 0
    for l in range(1, N+1):
        ret += generate(N-last, l) * (last + l - 1)
    ret %= MOD

    CACHE[N][last] = ret
    return ret


def get_monotone_polys(N):
    return sum(generate(N, l) for l in range(1, N+1)) % MOD


if __name__ == "__main__":
    C = int(input())
    ans = []

    for _ in range(C):
        ans.append(get_monotone_polys(int(input())))

    for n in ans:
        print(n)
