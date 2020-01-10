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


def get_prefix_suffix(s):
    ret = list()
    pi = get_partial_match(s)
    k = len(s)

    while k > 0:
        ret.append(k)
        k = pi[k-1]

    return ret


if __name__ == '__main__':
    s = input().strip() + input().strip()
    print(' '.join(map(str, get_prefix_suffix(s)[::-1])))
