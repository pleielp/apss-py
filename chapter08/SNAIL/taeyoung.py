# 재귀
def recursive(days, climbed):
    if days == total_days:
        return 1 if climbed >= depth else 0

    if cache[days][climbed] == -1:
        cache[days][climbed] = (1 - P) * recursive(days + 1, climbed + 1) + P * recursive(days + 1, climbed + 2)

    return cache[days][climbed]


def combination(m, n):
    n = min(n, m - n)
    result = 1
    for i in range(n):
        result *= m - i
        result //= i + 1
    return result

# 이항계수의 합
def binomial_dist(depth, total_days):
    if total_days >= depth:
        return 1
    elif 2 * total_days < depth:
        return 0

    answer = 0
    for sunny_days in range(2 * total_days - depth + 1):
        answer += combination(total_days, sunny_days) * (1 - P) ** sunny_days * P ** (total_days - sunny_days)
    return answer


# 정규분포에 근사시켜서 적분
from numpy import sqrt, pi, inf, e
from scipy.integrate import quad
def normal_dist(depth, total_days):
    if total_days >= depth:
        return 1
    elif 2 * total_days < depth:
        return 0

    mean = total_days * P
    deviation = sqrt(total_days * P * (1 - P))
    boundary = ((depth - total_days) - mean) / deviation
    return quad(lambda x: e ** (-x ** 2 / 2) / sqrt(2 * pi), boundary, inf)[0]

P = 0.75
case_num = int(input())
for _ in range(case_num):
    depth, total_days = map(int, input().strip().split())
    cache = [[-1] * (2 * total_days + 1) for _ in range(total_days)]

    # print(recursive(0, 0))
    print(binomial_dist(depth, total_days))
    # print(normal_dist(depth, total_days))