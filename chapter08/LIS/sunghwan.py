"""Get length of LIS in an integer sequence

:input:
3
4
1 2 3 4
8
5 4 3 2 1 6 7 8
8
5 6 7 8 1 2 3 4

:return:
4
4
4

url: https://algospot.com/judge/problem/read/LIS
ID : LIS
"""
# Exhaustive search
def lis(arr):
    if not arr:
        return 0

    ret = 0
    for i in range(len(arr)):
        nxt = []
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])

        ret = max(ret, 1 + lis(nxt))


# dynamic programming
def lis(arr):
    N = len(arr)
    cache = [-1] * N

    def find(start):
        if cache[start] != -1:
            return cache[start]

        ret = 1
        for nxt in range(start+1, N):
            if arr[start] < arr[nxt]:
                ret = max(ret, find(nxt) + 1)

        cache[start] = ret
        return ret

    return max(find(i) for i in range(N))


# Optimized one(n log n) V2.
def lis(arr):
    if not arr:
        return 0

    N = len(arr)
    INF = float('inf')
    # C[i] means smallest last number of lis subsequences whose length are i
    C = [INF] * N

    # Find i that matches C[i-1] < n <= C[i]
    def search(lo, hi, n):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if C[lo] >= n else hi

        mid = (lo + hi) // 2
        if C[mid] == n:
            return mid
        elif C[mid] < n:
            return search(mid+1, hi, n)
        else:
            return search(lo, mid, n)


    for n in arr:
        next_loc = search(0, N-1, n)
        C[next_loc] = n

    for i in range(N-1, -1, -1):
        if C[i] != INF:
            return i + 1


# Optimized one(n log k)
def lis(arr):
    # C[i] means smallest last number of lis subsequences whose length are i
    C = [float('inf')] * (len(arr)+1)
    C[0] = float('-inf')
    C[1] = arr[0]
    tmp_longest = 1

    # Find i that matches C[i-1] < n <= C[i]
    def search(lo, hi, n):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if C[lo] >= n else hi

        mid = (lo + hi) // 2
        if C[mid] == n:
            return mid
        elif C[mid] < n:
            return search(mid+1, hi, n)
        else:
            return search(lo, mid, n)


    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            next_loc = search(0, tmp_longest, n)
            C[next_loc] = n

    return tmp_longest


if __name__ == "__main__":
    C = int(input())
    ans = []

    for _ in range(C):
        input()
        ans.append(lis([int(n) for n in input().split()]))

    for n in ans:
        print(n)
