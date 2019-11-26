def make_poly(n, before=0):
    if cache[n][before] == -1:
        if n == 0:
            return 1

        result = 0
        for first in range(1, n + 1):
            m = make_poly(n - first, first)
            result += m if before == 0 else (before + first - 1) * m
            result %= MOD
        cache[n][before] = result
    
    return cache[n][before]


MOD = 10000000
case_num = int(input())
for _ in range(case_num):
    n = int(input())
    cache = [[-1] * (n + 1) for _ in range(n + 1)]

    print(make_poly(n))