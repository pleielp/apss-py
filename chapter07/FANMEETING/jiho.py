

def solution(members, fans):
    M = len(members)

    def meeting(fans):
        fans_num = len(fans)
        if fans_num < M:
            return 0

        mid = fans_num // 2

        ret = 0
        ret += meeting(fans[:mid]) + meeting(fans[mid+1:])

        for start_idx in range(mid - M + 1, mid+1):
            if start_idx < 0 or (start_idx + M) > fans_num:
                continue

            for i in range(M):
                if fans[start_idx + i] == 'M' and members[i] == 'M':
                    break
            else:
                ret += 1
        return ret

    return meeting(fans)


if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        members = input()
        fans = input()
        print(solution(members, fans))
