def multiply(a, b):
    c = [0] * (len(a) + len(b) + 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    return c


def add_to(a, b, k):
    b = [0] * k + b
    for i in range(k, min(len(a), len(b))):
        a[i] += b[i]
    a += b[len(a):]


def sub_from(a, b):
    for i in range(min(len(a), len(b))):
        a[i] -= b[i]


def karatsuba(a, b):
    an, bn = len(a), len(b)
    if an < bn:
        return karatsuba(b, a)
    if an == 0 or bn == 0:
        return list()
    if an <= 50:
        return multiply(a, b)

    half = an // 2
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:half]
    b1 = b[half:]

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)

    add_to(a0, a1, 0)
    add_to(b0, b1, 0)

    z1 = karatsuba(a0, b0)
    sub_from(z1, z0)
    sub_from(z1, z2)

    ret = list()
    add_to(ret, z0, 0)
    add_to(ret, z1, half)
    add_to(ret, z2, half + half)
    return ret

    
case_num = int(input())
for _ in range(case_num):
    members = list(map(int, list(input().strip().replace('F', '0').replace('M', '1'))))
    fans = list(map(int, list(input().strip().replace('F', '0').replace('M', '1')[::-1])))

    print(karatsuba(members, fans)[len(members)-1:len(fans)].count(0))