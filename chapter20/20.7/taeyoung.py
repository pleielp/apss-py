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


def kmp_search_2(H, N):
    ret = list()
    pi = get_partial_match(N)
    matched = 0

    for i in range(len(H)):
        while matched > 0 and H[i] != N[matched]:
            matched = pi[matched-1]
        if H[i] == N[matched]:
            matched += 1
            if matched == len(N):
                ret.append(i - len(N) + 1)
                matched = pi[matched-1]

    return ret


print(kmp_search_2('aabaabaabac', 'aabaabac'))
