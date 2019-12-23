from collections import Counter

MOD = 20091101


def solve_two_problems(doll_boxes, K):
    cumul_dolls = [0]
    for doll in doll_boxes:
        cumul_dolls.append((cumul_dolls[-1] + doll) % K)

    # 1. Count total number of ways to buy dolls
    counter = Counter(cumul_dolls)
    total_ways = 0

    for way in counter.values():
        if way >= 2:
            total_ways += way * (way - 1) // 2

    total_ways %= MOD


    # 2. Maximum number of consecutive buys
    ret = [0] * len(cumul_dolls)
    prev = [-1] * K

    for i in range(len(cumul_dolls)):
        if i > 0:
            ret[i] = ret[i-1]
        else:
            ret[i] = 0

        loc = prev[cumul_dolls[i]]
        if loc != -1:
            ret[i] = max(ret[i], ret[loc] + 1)

        prev[cumul_dolls[i]] = i

    max_buys = ret[-1]

    return total_ways, max_buys


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        _, K = (int(n) for n in input().split())
        doll_boxes = [int(n) for n in input().split()]
        ans.append(solve_two_problems(doll_boxes, K))

    for total_ways, max_buys in ans:
        print(total_ways, max_buys)
