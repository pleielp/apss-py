def kmp(haystack, needle):
    H, N = len(haystack), len(needle)
    ret = []
    pi = get_partial_match(needle)
    begin = matched = 0

    while begin <= H - N:
        if matched < N and haystack[begin+matched] == needle[matched]:
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
        if needle[begin+matched] == needle[matched]:
            matched += 1
            pi[begin + matched -1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return pi
