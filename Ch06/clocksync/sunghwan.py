SWITCH = (
    (0, 1, 2), (3, 7, 9, 11), (4, 10, 14, 15),
    (0, 4, 5, 6, 7), (6, 7, 8, 10, 12), (0, 2, 14, 15), (3, 14, 15),
    (4, 5, 7, 14, 15), (1, 2, 3, 4, 5), (3, 4, 5, 9, 13)
)


def synchronize_flips(clocks):
    N = len(clocks)
    ALL_SYNCED = [0] * N
    CANNOT_SYNC = -1
    INF = float('inf')

    # preprocess time from {12,3,6,9} to {0..3}
    for i in range(N):
        clocks[i] = (clocks[i] // 3) % 4

    def push(clocks, s):
        for c in SWITCH[s]:
            clocks[c] = (clocks[c] + 1) % 4

    def flip(clocks, switch):
        if switch == len(SWITCH):
            return 0 if clocks == ALL_SYNCED else INF

        ret = INF
        for cnt in range(4):
            ret = min(ret, flip(clocks, switch+1) + cnt)
            push(clocks, switch)

        return ret

    ans = flip(clocks, 0)
    return ans if ans != INF else CANNOT_SYNC


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        clocks = [int(n) for n in input().split()]
        ans.append(synchronize_flips(clocks))

    for n in ans:
        print(n)
