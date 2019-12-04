def tiling(n):
    if n <= 2:
        return n

    if cache[n] == -1:
        cache[n] = (tiling(n - 1) + tiling(n - 2)) % 1000000007

    return cache[n]


case_num = int(input())
for _ in range(case_num):
    n = int(input())
    cache = [-1] * (n + 1)
    print(tiling(n))