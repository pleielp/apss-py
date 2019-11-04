
switchs = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]


def rotate(clocks, switch):
    for c in switchs[switch]:
        clock = clocks[c] + 3
        clocks[c] = clock % 12


def is_finish(clocks):
    for clock in clocks:
        if clock % 12 != 0:
            return False
    return True


def clocksync(clocks, switch, count):
    if is_finish(clocks):
        return count

    if switch == 10:
        return float('inf')

    ret = float('inf')

    for r in range(4):
        ret = min(ret, clocksync(clocks, switch + 1, count + r))
        rotate(clocks, switch)
    return ret


C = int(input())
for _ in range(C):
    clocks = list(map(int, input().split()))
    print(clocksync(clocks, 0, 0))
