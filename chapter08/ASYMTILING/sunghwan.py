"""Get the number of cases to cover tile asymmetrically

URL: https://algospot.com/judge/problem/read/ASYMTILING?c=17311
ID : ASYMTILING
"""
def get_ways(lengths):
    MOD = int(1e9 + 7)
    MAX_LEN = max(lengths)

    ans = []
    fibo_cache = [-1] * (MAX_LEN+1)
    sym_cache = [-1] * (MAX_LEN+1)

    def fibo(n):
        if fibo_cache[n] != -1:
            return fibo_cache[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        fibo_cache[n] = (fibo(n-1) + fibo(n-2)) % MOD
        return fibo_cache[n]

    def get_sym_ways(n):
        if sym_cache[n] != -1:
            return sym_cache[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 1
        elif n == 4:
            return 3

        sym_cache[n] = (get_sym_ways(n-2) + get_sym_ways(n-4)) % MOD
        return sym_cache[n]


    for l in lengths:
        ans.append((fibo(l) - get_sym_ways(l)) % MOD)

    return ans


if __name__ == '__main__':
    C = int(input())
    lengths = []

    for _ in range(C):
        lengths.append(int(input()))

    ans = get_ways(lengths)
    for n in ans:
        print(n)
