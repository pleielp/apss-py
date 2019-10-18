def factor(n):
    if n == 1:
        return [1]
    ret = list()
    for div in range(2, n + 1):
        while n % div == 0:
            n //= div
            ret.append(div)
    return ret


print(factor(12))