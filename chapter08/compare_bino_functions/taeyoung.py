from myfunctions import measure_time

REPEAT_NUM = 1


@measure_time(repeat_num=REPEAT_NUM)
def test_bino(n ,r):
    def bino(n, r):
        if r == 0 or n == r:
            return 1
        return bino(n - 1, r - 1) + bino(n - 1, r)

    return bino(n, r)


@measure_time(repeat_num=REPEAT_NUM)
def test_bino2(n, r):
    cache = [[-1] * (r + 1) for _ in range(n)]

    def bino2(n, r):
        if r == 0 or n == r:
            return 1
        
        if cache[n-1][r] != -1:
            return cache[n-1][r]

        cache[n-1][r] = bino2(n - 1, r - 1) + bino2(n - 1, r)

        return cache[n-1][r]

    return bino2(n, r)


n, r = 26, 13
print(test_bino(n ,r))
print(test_bino2(n, r))