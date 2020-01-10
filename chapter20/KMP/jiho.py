def get_partial_match(N: str):
    # N의 문자열에서 ret[matched] matched까지 매칭이 됐을 때 접두사와 접미사가 같은 부분문자열의 최대 길이
    ret = [0] * len(N)
    for begin in range(1, len(N)):
        for i in range(len(N) - begin):
            if N[begin + i] != N[i]:
                break
            ret[begin + i] = max(ret[begin + i], i + 1)

    return ret


def get_partial_match_kmp(N: str):
    ret = [0] * len(N)

    begin = 1
    matched = 0
    while begin + matched < len(N):
        if N[begin + matched] == N[matched]:
            matched += 1
            ret[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - ret[matched - 1]
                matched = ret[matched - 1]
    return ret


def kmp_search(dummy: str, target: str):
    ret = []
    length_of_dummy = len(dummy)
    length_of_target = len(target)

    begin = 0
    matched = 0

    match_table = get_partial_match_kmp(target)

    while begin <= length_of_dummy - length_of_target:
        if matched < length_of_target and dummy[begin + matched] == target[matched]:
            matched += 1
            if matched == length_of_target:
                ret.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - match_table[matched - 1]
                matched = match_table[matched - 1]

    return ret


print(kmp_search("aabcaaba", "aaba"))
