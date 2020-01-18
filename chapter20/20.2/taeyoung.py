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


def kmp_search(H, N):
    ret = list()
    pi = get_partial_match(N)
    begin, matched = 0, 0

    # for문?
    while begin < len(H) - len(N) + 1:
        if matched < len(N) and H[begin + matched] == N[matched]:
            matched += 1
            if matched == len(N):
                ret.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return ret


print(kmp_search('aabaabaabac', 'aabaabac'))
print(kmp_search('abcde', 'eabcd'))
print(kmp_search('abbab', 'babab'))
