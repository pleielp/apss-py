"""Get number of times that all members hugged fans

url: https://algospot.com/judge/problem/read/FANMEETING
ID : FANMEETING
"""
def normalize(num):
    for i in range(len(num)-1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) // 10
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] // 10
            num[i] %= 10


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


# O(MF - M^2). maybe unhappy
def naive_way(members, fans):
    M, F = len(members), len(fans)
    members = [0 if m == 'M' else 1 for m in members]
    fans = [0 if f == 'M' else 1 for f in fans]
    ans = 0

    for i in range(F-M+1):
        ans += all(f | m for f, m in zip(fans[i:i+M], members))

    return ans


# O(n ^ lg3) way. Happy, merry, joy
def fan_meeting(members, fans):
    M, F = len(members), len(fans)

    members_processed = [m == 'M' for m in members]
    fans_processed = [f == 'M' for f in fans[::-1]]
    ret = karatsuba_multiply(members_processed, fans_processed)

    return sum(ret[i] == 0 for i in range(M-1, F))


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        members = input()
        fans = input()
        ans.append(fan_meeting(members, fans))

    for n in ans:
        print(n)
