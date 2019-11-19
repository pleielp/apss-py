"""Karatsuba multiplication algorithm with humanized one too

"""
# 이런 `정규화`라는 이름의 기가막힌 작명법은 좀 보고 배우고 싶다...
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


# O(N ^ 2)
def multiply_naive(arr1, arr2):
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]
    ret = [0] * (len(arr1) + len(arr2))

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            ret[i+j] += arr1[i] * arr2[j]

    normalize(ret)
    ret = ret[::-1]
    return ret


def karatsuba_multiply(arr1, arr2, to_string=False):
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]

    def add_to(arr1, arr2, k=0):
        for idx, n2 in enumerate(arr2):
            if idx + k >= len(arr1):
                arr1.append(n2)
            else:
                arr1[idx+k] += n2

    def sub_from(arr1, arr2):
        for i in range(len(arr2)):
            arr1[i] -= arr2[i]

    def multiply(a, b):
        AN, BN = len(a), len(b)

        # base cases
        if AN < BN:
            return multiply(b, a)
        elif AN == 0 or BN == 0:
            return []
        elif AN <= 50:
            ret = [0] * (AN + BN)

            for i in range(AN):
                for j in range(BN):
                    ret[i+j] += a[i] * b[j]

            return ret

        # do your job
        half = AN // 2
        a0, a1 = a[:half], a[half:]
        b0, b1 = b[:min(BN, half)], b[min(BN, half):]
        # 사실 여기는 그냥 half 써도 됨.
        # 파이썬 슬라이싱의 특징: 인덱스 넘겨도 에러 안 난다.

        z2 = multiply(a1, b1)
        z0 = multiply(a0, b0)

        add_to(a0, a1)
        add_to(b0, b1)

        z1 = multiply(a0, b0)

        sub_from(z1, z0)
        sub_from(z1, z2)

        ret = []
        add_to(ret, z0)
        add_to(ret, z1, half)
        add_to(ret, z2, half+half)
        return ret


    ret = multiply(arr1, arr2)
    normalize(ret)
    ret = ret[::-1]

    if to_string:
        return ''.join(str(n) for n in ret)
    else:
        return ret
