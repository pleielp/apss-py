def normalize(num):
    num.append(0)
    for i in range(len(num) - 1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) // 10  # borrow = 1
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] // 10
            num[i] %= 10

    while len(num) > 1 and num[-1] == 0:
        num.pop()


def multiply(a, b):
    c = [0] * (len(a) + len(b) + 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    normalize(c)
    return c


print(multiply([7,1], [2,1]))