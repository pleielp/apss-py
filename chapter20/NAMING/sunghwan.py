def kmp(haystack, needle):
    H, N = len(haystack), len(needle)
    begin = matched = 0
    pi = get_partial_match(needle)
    ret = []

    while begin <= H - N:
        if matched < N and haystack[begin + matched] == needle[matched]:
            matched += 1
            if matched == N:
                ret.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return ret


def get_partial_match(needle):
    N = len(needle)
    pi = [0] * N
    begin, matched = 1, 0

    while begin + matched < N:
        if needle[matched] == needle[begin + matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return pi


def get_name_lengths(joint):
    ret = [len(joint)]
    pi = get_partial_match(joint)
    idx = len(joint)

    while pi[idx-1] != 0:
        ret.append(pi[idx-1])
        idx = pi[idx-1]

    return ret[::-1]


if __name__ == '__main__':
    print(*get_name_lengths(input().strip() + input().strip()))
