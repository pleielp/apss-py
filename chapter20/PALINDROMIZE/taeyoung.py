def get_partial_match(N):
    pi = [0] * len(N)
    begin, matched = 1, 0
    while begin + matched < len(N):
        if N[begin+matched] == N[matched]:
            matched += 1
            pi[begin+matched-1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return pi


def max_overlap(a, b):
    pi = get_partial_match(b)
    begin, matched = 0, 0

    while begin < len(a):
        if matched < len(b) and a[begin + matched] == b[matched]:
            matched += 1
            if begin + matched == len(a):
                return matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]


if __name__ == '__main__':
    case_num = int(input())    
    for _ in range(case_num):
        s = input().strip()
        print(2 * len(s) - max_overlap(s, s[::-1]))
