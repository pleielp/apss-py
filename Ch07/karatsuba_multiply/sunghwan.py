# O(N ^ 2)
def normalize(num):
    num.append(0)
    for i in range(len(num)-1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) // 10
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] // 10
            num[i] %= 10

    while len(num) > 1 and num[-1] == 0:
        num.pop()


def normal_multiply(arr1, arr2):
    arr1, arr2 = arr1[::-1], arr2[::-1]
    ret = [0] * (len(arr1) + len(arr2))

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            ret[i+j] += arr1[i] * arr2[j]

    normalize(ret)
    return ret[::-1]


# O(N^log3)
def karatsuba_multiply(arr1, arr2):
    N1, N2 = len(arr1), len(arr2)

    def add_to(a, b, k):
        for i in range(len(b)):
            if i + k >= len(a):
                a.append(b[i])
            else:
                a[i+k] += b[i]

    def sub_from(a, b):
        print(len(a), len(b))
        for i in range(len(b)):
            a[i] -= b[i]

    # base cases
    if N1 < N2:
        return karatsuba_multiply(arr2, arr1)
    if N1 == 0 or N2 == 0:
        return []
    if N1 <= 50:
        return normal_multiply(arr1, arr2)

    half = N1 // 2
    a0, a1 = arr1[:half], arr1[half:]
    b0 = arr2[:min(N2, half)]
    b1 = arr2[min(N2, half):]

    z2 = karatsuba_multiply(a1, b1)
    z0 = karatsuba_multiply(a0, b0)

    add_to(a0, a1, 0)
    add_to(b0, b1, 0)

    z1 = karatsuba_multiply(a0, b0)
    sub_from(z1, z0)
    sub_from(z1, z2)

    ret = [0] * (N1 + N2)
    add_to(ret, z0, 0)
    add_to(ret, z1, half)
    add_to(ret, z2, half * 2)
    normalize(ret)
    return ret
