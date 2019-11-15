"""Get the number of longest paths in triangle path

url: https://algospot.com/judge/problem/read/TRIPATHCNT
ID : TRIPATHCNT
"""
def max_path(path):
    N = len(path)
    max_length_cache = [[-1] * N for _ in range(N)]
    cnt_cache = [[-1] * N for _ in range(N)]
    max_length_cache[0][0] = path[0][0]
    cnt_cache[0][0] = 1

    def get_max_length(r, c):
        if max_length_cache[r][c] != -1:
            return max_length_cache[r][c]
        elif not (0 <= r < N) or not (0 <= c < N) or c > r:
            return float('-inf')

        ans = path[r][c]

        if c == 0:
            ans += get_max_length(r-1, 0)
        else:
            ans += max(
                get_max_length(r-1, c),
                get_max_length(r-1, c-1)
            )
        max_length_cache[r][c] = ans
        return ans

    def count_ways(r, c):
        if cnt_cache[r][c] != -1:
            return cnt_cache[r][c]
        elif not (0 <= r < N) or not (0 <= c < N) or c > r:
            return 0

        if c == 0:
            cnt_cache[r][c] = 1
        else:
            if get_max_length(r-1, c) == get_max_length(r-1, c-1):
                cnt_cache[r][c] = count_ways(r-1, c) + count_ways(r-1, c-1)
            elif get_max_length(r-1, c) > get_max_length(r-1, c-1):
                cnt_cache[r][c] = count_ways(r-1, c)
            elif get_max_length(r-1, c) < get_max_length(r-1, c-1):
                cnt_cache[r][c] = count_ways(r-1, c-1)

        return cnt_cache[r][c]


    max_len = max(get_max_length(N-1, c) for c in range(N))
    return sum(count_ways(N-1, c) for c in range(N) if get_max_length(N-1, c) == max_len)


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N = int(input())
        path = []

        for _ in range(N):
            path.append([int(n) for n in input().split()])

        ans.append(max_path(path))

    for n in ans:
        print(n)
