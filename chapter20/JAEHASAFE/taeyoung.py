def get_partial_match(N):
    pi = [0] * len(N)
    begin, matched = 1, 0

    while begin + matched < len(N):
        if N[begin + matched] == N[matched]:
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

    while begin < len(H) - len(N) + 1:
        if matched < len(N) and H[begin+matched] == N[matched]:
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


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):

        ans = 0
        states_num = int(input())
        state_now = input().strip()
        is_clockwise = True

        for _ in range(states_num):
            state_next = input().strip()
            diff = kmp_search(state_next * 2, state_now)[0]
            if is_clockwise:
                ans += diff 
            else:
                ans += len(state_now) - diff

            is_clockwise = not is_clockwise
            state_now = state_next

        print(ans)
