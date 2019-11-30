def solution(num):
    mod = 10000000
    cache = [[-1 for _ in range(num+1)] for _ in range(num+1)]

    def poly(ceil, n):
        
        if cache[ceil][n] != -1:
            return cache[ceil][n]
        
        if n == 0:
            return 1
        ret = 0
        for new_ceil in range(1, n+1):
            case = ceil + new_ceil - 1 if ceil != 0 else 1
            ret += case * poly(new_ceil, n - new_ceil) 
            ret %= mod
        cache[ceil][n] = ret % mod
        return ret

    return poly(0, num)
C = int(input())
for _ in range(C):
    n = int(input())
    print(solution(n))