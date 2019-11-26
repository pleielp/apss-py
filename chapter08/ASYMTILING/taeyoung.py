def tiling(n):
    if n <= 2:
        return n

    if cache[n] == -1:
        cache[n] = (tiling(n - 1) + tiling(n - 2)) % 1000000007

    return cache[n]


def asymtiling(n):
    if n % 2 == 0:
        a = tiling(n // 2)
        b = tiling(n // 2 - 1)
        return (a * (a - 1) + b * (b - 1)) % 1000000007
    else:
        a = tiling((n - 1) // 2)
        b = tiling(n // 2 - 1)
        c = tiling(n // 2 + 1)
        return (a * (a - 1) + 2 * b * c) % 1000000007
    return asymtiling


case_num = int(input())
for _ in range(case_num):
    n = int(input())
    cache = [-1] * (n + 1)
    print(asymtiling(n))