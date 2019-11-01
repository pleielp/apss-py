def summation(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
    return ret


def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)


N = 100
print(summation(N))
print(recursive_sum(N))
