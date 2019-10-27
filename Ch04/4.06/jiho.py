def factor(n):
    primes = []
    div = 2
    while n > 1:
        if n % div == 0:
            n = n // div
            primes.append(div)
            continue
        div += 1
    return primes


if __name__ == "__main__":

    print(factor(9999))
