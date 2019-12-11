from itertools import combinations
from sys import setrecursionlimit

setrecursionlimit(10000)
C = int(input())
N = int(input())


def get_bit(n):
    return 1 << n


def get_size(mask):
    return bin(mask).count("1")


def get_sum(mask):
    ret = 0
    for idx, v in enumerate(reversed(bin(mask))):
        if v == "1":
            ret += idx
    return ret


candidates = [[[0 for _ in range(1024)] for _ in range(46)] for _ in range(10)]


def generateCandidates():
    for s in range(0, 1024, 2):
        lenght = get_size(s)
        Sum = get_sum(s)
        subset = s
        while True:
            candidates[lenght][Sum][subset] |= s & ~subset
            if subset == 0:
                break
            subset = (subset - 1) & s


board_value = [[0 for _ in range(N)] for _ in range(N)]
board_hint = [[[-1 for _ in range(2)] for _ in range(N)] for _ in range(N)]
board_color = [[0 for _ in range(N)] for _ in range(N)]

# hints
hint_sum = [0] * N ** 2
hint_length = [0] * N ** 2
hint_known = [0] * N ** 2


def put(r, c, val):
    for h in range(2):
        hint_known[board_hint[r][c][h]] += 1 << val
    board_value[r][c] = val


def remove(r, c, val):
    for h in range(2):
        hint_known[board_hint[r][c][h]] -= 1 << val
    board_value[r][c] = 0


def get_cand_hint(hint):
    return candidates[hint_length[hint]][hint_sum[hint]][hint_known[hint]]


def get_cand_coord(r, c):
    return get_cand_hint(board_hint[r][c][0]) & get_cand_hint(board_hint[r][c][1])


WHITE = 1
BLACK = 0


def solution(kakuro, hints):
    generateCandidates()
    board_color = kakuro

    for idx, hint in enumerate(hints):
        r, c, direction, line_sum = hint
        r, c = r - 1, c - 1
        hint_sum[idx] = line_sum
        length = 0
        if direction == 0:
            c += 1
            while c < N and board_color[r][c] == 1:
                board_hint[r][c][direction] = idx
                length += 1
                c += 1
        else:
            r += 1
            while r < N and board_color[r][c] == 1:
                board_hint[r][c][direction] = idx
                length += 1
                r += 1
        hint_length[idx] = length

    def search():
        print("----------------------")
        for line in board_value:
            print(line)

        r = -1
        c = -1
        minCands = 1023
        for i in range(N):
            for j in range(N):
                if board_color[i][j] == WHITE and board_value[i][j] == 0:
                    cands = get_cand_coord(i, j)
                    if get_size(minCands) > get_size(cands):
                        minCands = cands
                        r = i
                        c = j
        if minCands == 0:
            return False
        if y == -1:
            for line in board_value:
                print(line)
            return True

        for val in range(1, 10):
            if minCands & (1 << val):
                put(r, c, val)
                if search():
                    return True
                remove(r, c, val)
        return False

    search()


for _ in range(C):
    kakuro = []
    for _ in range(N):
        kakuro.append(list(map(int, input().split())))

    Q = int(input())
    hints = []
    for _ in range(Q):
        y, x, direction, line_sum = map(int, input().split())
        hints.append((y, x, direction, line_sum))

    solution(kakuro, hints)

