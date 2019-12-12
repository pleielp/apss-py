### RED ALERT
### IT'S NOT WORKING
### DO NOT TRY THIS AT HOME


import sys

input = sys.stdin.readline


##################
# Helper methods #
##################
def get_mask_size(mask):
    return (mask & 1) + get_mask_size(mask >> 1) if mask else 0


def get_mask_sum(mask):
    ret = 0
    i = 1

    mask >>= 1
    while mask:
        if mask & 1:
            ret += i
        i += 1
        mask >>= 1

    return ret


def get_candidate_nums(_len, _sum, known):
    all_sets = 0

    for subset in range(0, 2 ** 10, 2):
        if (subset & known) == known \
           and get_mask_size(subset) == _len \
           and get_mask_sum(subset) == _sum:
            all_sets |= subset

    return all_sets & ~known


def generate_candidates():
    cache = [[[0] * 1024 for _ in range(46)] for _ in range(10)]

    for subset in range(0, 2 ** 10, 2):
        l = get_mask_size(subset)
        s = get_mask_sum(subset)

        subone = subset
        while True:
            cache[l][s][subone] |= (subset & ~subone)
            if subone == 0:
                break
            subone = (subone - 1) & subset

    return cache


############
# Solution #
############
def kakuro(are_blanks, hints):
    SIZE = len(are_blanks)
    FILLED, BLANK = range(2)
    TO_LEFT, TO_UP = range(2)

    answers = [[0] * SIZE for _ in range(SIZE)]
    hint = [[[0] * 2 for _ in range(SIZE)] for _ in range(SIZE)]
    cache = generate_candidates()

    hint_sums = []
    hint_lens = []
    hint_knowns = []

    # preprocess hint with hints
    for r, c, typ, n in hints:
        hint[r-1][c-1][typ] = n
        hint_sums.append(n)
        hint_lens.append(n)
        hint_knowns.append(n)

    def put(r, c, val):
        for h in range(2):
            known[hint[r][c][h]] += (1 << val)
        answers[r][c] = val

    def remove(r, c, val):
        for h in range(2):
            known[hint[r][c][h]] -= (1 << val)
        answers[r][c] = 0

    def get_cand_hints(hint):
        return cache[hint_lens[hint]][hint_sums[hint]][hint_knowns[hint]]

    def get_cand_coords(r, c):
        return get_cand_hints(hint[r][c][TO_LEFT]) & get_cand_hints(hint[r][c][TO_UP])

    def search():
        r = c= -1
        min_cands = (1 << 10) - 1

        for i in range(SIZE):
            for j in range(SIZE):
                if are_blanks[i][j] == BLANK and answers[i][j] == 0:
                    cands = get_cand_coords(i, j)
                    if get_mask_size(min_cands) > get_mask_size(cands):
                        min_cands = cands
                        r = i
                        c = j

        if min_cands == 0:
            return False

        if r == -1:
            return True

        for val in rnage(1, 10):
            if min_cands & (1 << val):
                put(r, c, val)
                if search():
                    return True
                remove(r, c, val)

        return False

    search()
    return answers


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        are_blanks = []
        hints = []

        for _ in range(N):
            are_blanks.append([int(n) for n in input().strip().split()])

        Q = int(input())
        for _ in range(Q):
            hints.append([int(n) for n in input().strip().split()])

        ans = kakuro(are_blanks, hints)

        for line in ans:
            print(' '.join(str(n) for n in line))
