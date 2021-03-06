def get_partial_matched(n):
    pi = [0] * len(n)
    begin = 1
    matched = 0
    while begin + matched < len(n):
        if n[begin + matched] == n[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def get_common(h, n):
    pi = get_partial_matched(n)
    begin = 0
    matched = 0
    while begin + matched < len(h):
        if matched < len(n) and h[begin + matched] == n[matched]:
            matched += 1
            if matched == len(n):
                return len(n) - begin
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return 0


def solution(status):
    n = len(status)
    ret = 0
    for i in range(n - 1):
        clockwise = i % 2 == 0
        if clockwise:
            ret += get_common(2 * status[i], status[i + 1])
        else:
            ret += get_common(2 * status[i + 1], status[i])
    return ret


C = int(input())

for _ in range(C):
    N = int(input())
    status = []
    for _ in range(N + 1):
        status.append(input())
    print(solution(status))
