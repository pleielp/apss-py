import sys
sys.setrecursionlimit(10000)

def precalc():
    psum = [sequence[0]]
    psqsum = [sequence[0] ** 2]

    for i in range(1, len(sequence)):
        psum.append(psum[i - 1] + sequence[i])
        psqsum.append(psqsum[i - 1] + sequence[i] ** 2)

    return psum, psqsum


def min_error(lo, hi):
    tsum = psum[hi] - (0 if lo == 0 else psum[lo - 1])
    tsqsum = psqsum[hi] - (0 if lo == 0 else psqsum[lo - 1])

    m = int(0.5 + tsum / (hi - lo + 1))
    ret = tsqsum - 2 * m * tsum + m ** 2 * (hi - lo + 1)
    return ret


def quantize(start, parts):
    if start == len(sequence):
        return 0
    if parts == 0:
        return float('inf')

    if cache[start][parts] == float('inf'):
        for part_size in range(1, len(sequence) - start + 1):
            cache[start][parts] = min(cache[start][parts], min_error(start, start + part_size - 1) + quantize(start + part_size, parts - 1))

    return cache[start][parts]


case_num = int(input())
for _ in range(case_num):
    sequence_size, quantization_num = map(int, input().strip().split())
    sequence = sorted(map(int, input().strip().split()))

    cache = [[float('inf')] * 11 for _ in range(101)]
    psum, psqsum = precalc()
    print(quantize(0, quantization_num))