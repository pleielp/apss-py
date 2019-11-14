"""Get least sum of quantized arrays

url: https://algospot.com/judge/problem/read/QUANTIZE
ID : QUANTIZE
"""
# No satisfaction, let's go dynamic search boy~
# room for overlapping subproblems:
#   1. sum of partial sequences in array
#   2. middle process of move_on function like `move_on(2, 2)` is duplicated onto next processes
#
# So we memoize these two subproblems, got it?
#
# Time complexity is O(SN^2)
def quantize(arr, S):
    N = len(arr)
    INF = float('inf')
    NOT_CHECKED = -1

    arr.sort()

    p_sums = [arr[0]] * N
    p_squares = [[-1] * N for _ in range(N)]
    cache = [[-1] * (S+1) for _ in range(N)]

    for i in range(1, N):
        p_sums[i] = p_sums[i-1] + arr[i]

    def get_psum(lo, hi):
        if lo == 0:
            return p_sums[hi]
        else:
            return p_sums[hi] - p_sums[lo-1]

    for i in range(N):
        for j in range(i, N):
            mean = round(get_psum(i, j) / (j - i + 1))
            p_squares[i][j] = sum((n - mean) ** 2 for n in arr[i:j+1])

    def move_on(last_idx, chosen):
        c_idx = len(chosen)

        if last_idx == N - 1:
            return 0
        elif c_idx == S:
            return INF
        elif cache[last_idx][c_idx] != NOT_CHECKED:
            return cache[last_idx][c_idx]

        lo = last_idx + 1
        ans = INF

        for hi in range(lo, N):
            mean = round(get_psum(lo, hi) / (hi - lo + 1))
            if mean not in chosen:
                chosen.add(mean)
                ans = min(ans,
                          p_squares[lo][hi] + move_on(hi, chosen))
                chosen.remove(mean)

        cache[last_idx][c_idx] = ans
        return ans

    return move_on(-1, set())


if __name__ == "__main__":
    C = int(input())
    ans = []

    for _ in range(C):
        _, S = (int(n) for n in input().split())
        arr = [int(n) for n in input().split()]
        ans.append(quantize(arr, S))

    for n in ans:
        print(n)
